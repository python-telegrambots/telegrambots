from dataclasses import dataclass
from typing import Any

from ..api_method import TelegramBotsMethod
from ..api_result import TelegramBotsApiResult
from ..objects.user import User


@dataclass(init=True, repr=True, slots=True)
class GetMe(TelegramBotsMethod[TelegramBotsApiResult[User]]):
    # --- description here ---
    """A simple method for testing your bot's authentication token. Requires no parameters. Returns basic information about the bot in form of a [User](https://core.telegram.org/bots/api/#user) object.

    More info at: https://core.telegram.org/bots/api/#getme
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMethod.__init__(  # type: ignore
            obj, "getMe", [User])
        return obj

    # --- arguments here ---
