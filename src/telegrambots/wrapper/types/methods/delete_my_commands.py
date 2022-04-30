from dataclasses import dataclass, field
from typing import Any, Optional

from ..api_method import TelegramBotsMethod
from ..api_result import TelegramBotsApiResult
from ..objects.bot_command_scope import BotCommandScope


@dataclass(init=True, repr=True, slots=True)
class DeleteMyCommands(TelegramBotsMethod[TelegramBotsApiResult[bool]]):
    # --- description here ---
    """Use this method to delete the list of the bot's commands for the given scope and user language. After deletion, [higher level commands](https://core.telegram.org/bots/api/#determining-list-of-commands) will be shown to affected users. Returns *True* on success.
    
    More info at: https://core.telegram.org/bots/api/#deletemycommands
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMethod.__init__(  # type: ignore
            obj, "deleteMyCommands", [bool])
        return obj


    # --- arguments here ---
    scope: Optional[BotCommandScope] = field(default=None, metadata={"ac_type": [BotCommandScope], "ac_name": "scope"})
    """A JSON-serialized object, describing scope of users for which the commands are relevant. Defaults to [BotCommandScopeDefault](https://core.telegram.org/bots/api/#botcommandscopedefault).
    """

    language_code: Optional[str] = field(default=None, metadata={"ac_type": [str], "ac_name": "language_code"})
    """A two-letter ISO 639-1 language code. If empty, commands will be applied to all users from the given scope, for whose language there are no dedicated commands
    """

