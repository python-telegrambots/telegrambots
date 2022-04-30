from abc import ABC
from typing import Any, Generic, final

from .objects.message import Message
from .api_result import TelegramBotsApiResult
from .api_object import TelegramBotsObject, TResult


class TelegramBotsMethod(Generic[TResult], ABC, TelegramBotsObject):
    def __init__(self, endpoint: str, return_type: list[type[Any]]) -> None:
        self._endpoint = endpoint
        self._return_type = return_type

    @final
    @property
    def endpoint(self) -> str:
        return self._endpoint

    def get_request_body(self):
        return self.serialize(False, self, None)

    @final
    def get_request_result(
            self, response: dict[str, Any], client: Any) -> TResult:
        return TelegramBotsApiResult.deserialize(
            response, {
                'result': self._return_type,
                'pinned_message': [Message],  # in Chat object
                'reply_to_message': [Message]
            }, client)  # type: ignore
