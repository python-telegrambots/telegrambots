from dataclasses import dataclass, field

from .bot_command_scope import BotCommandScope


@dataclass(init=True, repr=True, slots=True)
class BotCommandScopeChatAdministrators(BotCommandScope):
    # --- description here ---
    """Represents the [scope](https://core.telegram.org/bots/api/#botcommandscope) of bot commands, covering all administrators of a specific group or supergroup chat.

    More info at: https://core.telegram.org/bots/api/#botcommandscopechatadministrators
    """

    # --- properties here ---
    chat_id: int | str = field(
        metadata={"ac_type": [int, str], "ac_name": "chat_id"})
    """Unique identifier for the target chat or username of the target supergroup (in the format `@supergroupusername`)
    """

    @property
    def type(self) -> str:
        self._type = 'chat_administrators'
        return self._type
