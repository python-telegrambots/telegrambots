from dataclasses import dataclass

from .bot_command_scope import BotCommandScope


@dataclass(init=True, repr=True, slots=True)
class BotCommandScopeDefault(BotCommandScope):
    # --- description here ---
    """Represents the default [scope](https://core.telegram.org/bots/api/#botcommandscope) of bot commands. Default commands are used if no commands with a [narrower scope](https://core.telegram.org/bots/api/#determining-list-of-commands) are specified for the user.

    More info at: https://core.telegram.org/bots/api/#botcommandscopedefault
    """

    # --- properties here ---
    @property
    def type(self) -> str:
        return self._type
