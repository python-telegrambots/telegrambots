from dataclasses import dataclass, field
from typing import Any

from ..api_method import TelegramBotsMethodNoOutput


@dataclass(init=True, repr=True, slots=True)
class UnbanChatSenderChat(TelegramBotsMethodNoOutput):
    # --- description here ---
    """Use this method to unban a previously banned channel chat in a supergroup or channel. The bot must be an administrator for this to work and must have the appropriate administrator rights. Returns *True* on success.

    More info at: https://core.telegram.org/bots/api/#unbanchatsenderchat
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMethodNoOutput.__init__(obj, "unbanChatSenderChat")  # type: ignore
        return obj

    # --- arguments here ---
    chat_id: int | str = field(metadata={"ac_type": [int, str], "ac_name": "chat_id"})
    """Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
    """

    sender_chat_id: int = field(
        metadata={"ac_type": [int], "ac_name": "sender_chat_id"}
    )
    """Unique identifier of the target sender chat
    """
