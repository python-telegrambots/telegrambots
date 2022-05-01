from typing import Any, Generic
from .api_method import TelegramBotsMethod, TelegramBotsMethodNoOutput, TResult


class TelegramBotsMultipartMethod(Generic[TResult], TelegramBotsMethod[TResult]):
    def __init__(self, endpoint: str, return_type: list[type[Any]]) -> None:
        super().__init__(endpoint, return_type)

    def __enter__(self):
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any):
        to_dispose = self.get_list_metadata("dispose_these")
        for obj in to_dispose:
            obj.close()


class TelegramBotsMultipartMethodNoOutput(TelegramBotsMethodNoOutput):
    """This class is used to represent the result of an API call. It has no output."""

    def __init__(self, endpoint: str) -> None:
        """This class is used to represent the result of an API call. It has no output."""
        super().__init__(endpoint, [None])  # type: ignore

    def __enter__(self):
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any):
        to_dispose = self.get_list_metadata("dispose_these")
        for obj in to_dispose:
            obj.close()
