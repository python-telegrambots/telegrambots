from dataclasses import dataclass, field
from typing import Any, Optional

from ..api_method import TelegramBotsMethod
from ..api_result import TelegramBotsApiResult
from ..objects.bot_command_scope import BotCommandScope
from ..objects.bot_command import BotCommand


@dataclass(init=True, repr=True, slots=True)
class GetMyCommands(TelegramBotsMethod[TelegramBotsApiResult[list[BotCommand]]]):
    # --- description here ---
    """Use this method to get the current list of the bot's commands for the given scope and user language. Returns Array of [BotCommand](https://core.telegram.org/bots/api/#botcommand) on success. If commands aren't set, an empty list is returned.
    
    More info at: https://core.telegram.org/bots/api/#getmycommands
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMethod.__init__(  # type: ignore
            obj, "getMyCommands", [BotCommand])
        return obj


    # --- arguments here ---
    scope: Optional[BotCommandScope] = field(default=None, metadata={"ac_type": [BotCommandScope], "ac_name": "scope"})
    """A JSON-serialized object, describing scope of users. Defaults to [BotCommandScopeDefault](https://core.telegram.org/bots/api/#botcommandscopedefault).
    """

    language_code: Optional[str] = field(default=None, metadata={"ac_type": [str], "ac_name": "language_code"})
    """A two-letter ISO 639-1 language code or an empty string
    """

