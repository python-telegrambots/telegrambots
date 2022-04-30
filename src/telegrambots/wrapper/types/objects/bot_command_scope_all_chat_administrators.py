from dataclasses import dataclass

from .bot_command_scope import BotCommandScope


@dataclass(init=True, repr=True, slots=True)
class BotCommandScopeAllChatAdministrators(BotCommandScope):
    # --- description here ---
    """Represents the [scope](https://core.telegram.org/bots/api/#botcommandscope) of bot commands, covering all group and supergroup chat administrators.

    More info at: https://core.telegram.org/bots/api/#botcommandscopeallchatadministrators
    """

    # --- properties here ---
    @property
    def type(self) -> str:
        self._type = 'all_chat_administrators'
        return self._type
