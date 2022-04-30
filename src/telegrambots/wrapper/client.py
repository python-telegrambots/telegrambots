import io
import json
from typing import Any, Optional, cast

import aiohttp

from .api_response_exception import ApiResponseException
from .types.api_multipart_method import TelegramBotsMethod, TResult
from .types.api_result import TelegramBotsApiResult


class TelegramBotsClient:
    def __init__(self, token: str):
        if not TelegramBotsClient._validate_token(token):
            raise ValueError('Token invalid')

        self._token = token
        self._base_url = "https://api.telegram.org/bot{}/".format(token)
        self._session: Optional[aiohttp.ClientSession] = None

    async def __call__(
            self,
            method: TelegramBotsMethod[
                TelegramBotsApiResult[TResult]]) -> TResult:
        """ Call the method and return the result """
        return await self._send(method)

    async def __aenter__(self):
        self._session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any):
        if self._session:
            await self._session.close()
            self._session = None

    async def _send(
            self,
            method: TelegramBotsMethod[
                TelegramBotsApiResult[TResult]]) -> TResult:

        body = method.get_request_body()
        files: list[tuple[str, str, io.BufferedReader]
                    ] = method.get_list_metadata('files')

        data = aiohttp.FormData(quote_fields=False)

        for key, value in body.items():
            data.add_field(
                key, json.dumps(value) if not isinstance(value, str) else value)

        for file in files:
            data.add_field(file[0], file[2], filename=file[1])

        session = self._session or aiohttp.ClientSession()

        try:
            resp = await session.post(
                self._base_url + method.endpoint, data=data)
            json_respone = await resp.json()

            object_response = method.get_request_result(
                json_respone, self)
            if object_response.ok:
                if self._session is None:
                    await session.close()

                return cast(TResult, object_response.result)
            else:
                await session.close()
                raise ApiResponseException.from_result(object_response)
        except aiohttp.ClientError as e:
            await session.close()
            raise e

    @staticmethod
    def _validate_token(token: str):
        if not token:
            return False
        parts = token.split(':')
        if len(parts) != 2:
            return False
        return parts[0].isnumeric()
