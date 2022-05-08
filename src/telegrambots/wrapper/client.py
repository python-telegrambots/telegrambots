import io
import json
from typing import Any, Optional, cast, overload

import aiohttp

from .api_response_exception import ApiResponseException
from .types.api_method import TelegramBotsMethod, TelegramBotsMethodNoOutput, TResult
from .types.api_result import TelegramBotsApiResult


class TelegramBotsClient:
    def __init__(self, token: str, session: Optional[aiohttp.ClientSession] = None):
        if not TelegramBotsClient._validate_token(token):
            raise ValueError("Token invalid")

        self._token = token
        self._base_url = "https://api.telegram.org/bot{}/".format(token)
        self._session: Optional[aiohttp.ClientSession] = session

    @overload
    async def __call__(
        self, method: TelegramBotsMethod[TelegramBotsApiResult[TResult]]
    ) -> TResult:
        """Call the method and return the result"""
        ...

    @overload
    async def __call__(self, method: TelegramBotsMethodNoOutput) -> None:
        """Call the method which returns no result"""
        ...

    async def __call__(
        self,
        method: TelegramBotsMethodNoOutput
        | TelegramBotsMethod[TelegramBotsApiResult[TResult]],
    ) -> TResult | None:
        return await self._send(method)  # type: ignore

    async def __aenter__(self):
        if self._session is None:
            self._session = aiohttp.ClientSession()
            return self

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any):
        if self._session:
            await self._session.close()
            self._session = None

    @property
    def session(self) -> Optional[aiohttp.ClientSession]:
        """Get the session"""
        return self._session

    @overload
    async def _send(
        self, method: TelegramBotsMethod[TelegramBotsApiResult[TResult]]
    ) -> TResult:
        ...

    @overload
    async def _send(self, method: TelegramBotsMethodNoOutput) -> None:
        ...

    async def _send(
        self,
        method: TelegramBotsMethodNoOutput
        | TelegramBotsMethod[TelegramBotsApiResult[TResult]],
    ) -> TResult | None:

        body = method.get_request_body()
        files: list[tuple[str, str, io.BufferedReader]] = method.get_list_metadata(
            "files"
        )

        data = aiohttp.FormData(quote_fields=False)

        for key, value in body.items():
            data.add_field(
                key, json.dumps(value) if not isinstance(value, str) else value
            )

        for file in files:
            data.add_field(file[0], file[2], filename=file[1])

        assert self._session is not None
        assert not self._session.closed

        try:
            resp = await self._session.post(self._base_url + method.endpoint, data=data)
            json_respone = await resp.json()

            if resp.ok:
                if isinstance(method, TelegramBotsMethodNoOutput):
                    return None
                else:
                    object_response = method.get_request_result(json_respone, self)
                    if object_response.ok:
                        return cast(TResult, object_response.result)
                    raise ApiResponseException(-1, "Wired error")
            else:
                object_response = TelegramBotsApiResult.deserialize(json_respone)
                raise ApiResponseException.from_result(object_response)  # type: ignore
        except aiohttp.ClientError as e:
            raise e

    @staticmethod
    def _validate_token(token: str):
        if not token:
            return False
        parts = token.split(":")
        if len(parts) != 2:
            return False
        return parts[0].isnumeric()
