from dataclasses import dataclass

from .bot_command_scope import BotCommandScope


@dataclass(init=True, repr=True, slots=True)
class BotCommandScopeAllGroupChats(BotCommandScope):
    # --- description here ---
    """Represents the [scope](https://core.telegram.org/bots/api/#botcommandscope) of bot commands, covering all group and supergroup chats.

    More info at: https://core.telegram.org/bots/api/#botcommandscopeallgroupchats
    """

    # --- properties here ---
    @property
    def type(self) -> str:
        self._type = 'all_group_chats'
        return self._type
