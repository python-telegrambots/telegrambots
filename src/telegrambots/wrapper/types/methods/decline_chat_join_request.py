from dataclasses import dataclass, field
from typing import Any

from ..api_method import TelegramBotsMethodNoOutput


@dataclass(init=True, repr=True, slots=True)
class DeclineChatJoinRequest(TelegramBotsMethodNoOutput):
    # --- description here ---
    """Use this method to decline a chat join request. The bot must be an administrator in the chat for this to work and must have the *can\\_invite\\_users* administrator right. Returns *True* on success.

    More info at: https://core.telegram.org/bots/api/#declinechatjoinrequest
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMethodNoOutput.__init__(  # type: ignore
            obj, "declineChatJoinRequest"
        )
        return obj

    # --- arguments here ---
    chat_id: int | str = field(metadata={"ac_type": [int, str], "ac_name": "chat_id"})
    """Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
    """

    user_id: int = field(metadata={"ac_type": [int], "ac_name": "user_id"})
    """Unique identifier of the target user
    """
