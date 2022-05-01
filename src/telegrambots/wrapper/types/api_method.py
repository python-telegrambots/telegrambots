from abc import ABC
from typing import Any, Generic, final

from .objects.message import Message
from .api_result import TelegramBotsApiResult
from .api_object import TelegramBotsObject, TResult


class TelegramBotsMethod(Generic[TResult], ABC, TelegramBotsObject):
    """This class is used to represent the result of an API call."""

    def __init__(self, endpoint: str, return_type: list[type[Any]]) -> None:
        """This class is used to represent the result of an API call."""
        self._endpoint = endpoint
        self._return_type = return_type

    @final
    @property
    def endpoint(self) -> str:
        return self._endpoint

    @final
    def get_request_body(self):
        return self.serialize(self)

    def get_request_result(self, response: dict[str, Any], client: Any) -> TResult:
        return TelegramBotsApiResult.deserialize(
            response,
            custom_types={
                "result": self._return_type,
                "pinned_message": [Message],  # in Chat object
                "reply_to_message": [Message],
            },
            client=client,
        )  # type: ignore


class TelegramBotsMethodNoOutput(TelegramBotsMethod[None]):
    """This class is used to represent the result of an API call. It has no output."""

    def __init__(self, endpoint: str) -> None:
        """This class is used to represent the result of an API call. It has no output."""
        super().__init__(endpoint, [None])  # type: ignore

    @final
    def get_request_result(self, response: dict[str, Any], client: Any):
        return None
