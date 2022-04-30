from dataclasses import dataclass, field

from .bot_command_scope import BotCommandScope


@dataclass(init=True, repr=True, slots=True)
class BotCommandScopeChatMember(BotCommandScope):
    # --- description here ---
    """Represents the [scope](https://core.telegram.org/bots/api/#botcommandscope) of bot commands, covering a specific member of a group or supergroup chat.

    More info at: https://core.telegram.org/bots/api/#botcommandscopechatmember
    """

    # --- properties here ---
    chat_id: int | str = field(
        metadata={"ac_type": [int, str], "ac_name": "chat_id"})
    """Unique identifier for the target chat or username of the target supergroup (in the format `@supergroupusername`)
    """

    user_id: int = field(metadata={"ac_type": [int], "ac_name": "user_id"})
    """Unique identifier of the target user
    """

    @property
    def type(self) -> str:
        self._type = 'chat_member'
        return self._type
