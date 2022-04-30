from typing import TYPE_CHECKING, cast, Any

if TYPE_CHECKING:
    from .types.api_result import TelegramBotsApiResult


class ApiResponseException(Exception):
    """
    This exception is raised when the Telegram API returns a
    response with a non-OK status code.
    """

    def __init__(self, error_code: int, description: str):
        super().__init__(f"({error_code}): {description}")
        self.error_code = error_code
        self.description = description

    @staticmethod
    def from_result(result: "TelegramBotsApiResult[Any]"):
        return ApiResponseException(
            cast(int, result.error_code), cast(str, result.description)
        )
