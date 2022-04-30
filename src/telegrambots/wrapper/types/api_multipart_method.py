from typing import Any, Generic, final
from .api_method import TelegramBotsMethod, TResult


class TelegramBotsMultipartMethod(
        Generic[TResult], TelegramBotsMethod[TResult]):
    def __init__(self, endpoint: str, return_type: list[type[Any]]) -> None:
        super().__init__(endpoint, return_type)

    @final
    def get_request_body(self):
        return self.serialize(True, self)

    def __enter__(self):
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any):
        to_dispose = self.get_list_metadata('dispose_these')
        for obj in to_dispose:
            obj.close()
