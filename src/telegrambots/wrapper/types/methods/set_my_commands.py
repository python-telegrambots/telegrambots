from dataclasses import dataclass, field
from typing import Any, Optional

from ..api_method import TelegramBotsMethod
from ..api_result import TelegramBotsApiResult
from ..objects.bot_command_scope import BotCommandScope
from ..objects.bot_command import BotCommand


@dataclass(init=True, repr=True, slots=True)
class SetMyCommands(TelegramBotsMethod[TelegramBotsApiResult[bool]]):
    # --- description here ---
    """Use this method to change the list of the bot's commands. See [https://core.telegram.org/bots#commands](https://core.telegram.org/bots#commands) for more details about bot commands. Returns *True* on success.
    
    More info at: https://core.telegram.org/bots/api/#setmycommands
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMethod.__init__(  # type: ignore
            obj, "setMyCommands", [bool])
        return obj


    # --- arguments here ---
    commands: list[BotCommand] = field(metadata={"ac_type": [BotCommand], "ac_name": "commands"})
    """A JSON-serialized list of bot commands to be set as the list of the bot's commands. At most 100 commands can be specified.
    """

    scope: Optional[BotCommandScope] = field(default=None, metadata={"ac_type": [BotCommandScope], "ac_name": "scope"})
    """A JSON-serialized object, describing scope of users for which the commands are relevant. Defaults to [BotCommandScopeDefault](https://core.telegram.org/bots/api/#botcommandscopedefault).
    """

    language_code: Optional[str] = field(default=None, metadata={"ac_type": [str], "ac_name": "language_code"})
    """A two-letter ISO 639-1 language code. If empty, commands will be applied to all users from the given scope, for whose language there are no dedicated commands
    """

