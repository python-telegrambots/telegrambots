from dataclasses import dataclass, field
from typing import Any

from ..api_method import TelegramBotsMethod
from ..api_result import TelegramBotsApiResult
from ..objects.chat_member import ChatMember


@dataclass(init=True, repr=True, slots=True)
class GetChatMember(TelegramBotsMethod[TelegramBotsApiResult[ChatMember]]):
    # --- description here ---
    """Use this method to get information about a member of a chat. Returns a [ChatMember](https://core.telegram.org/bots/api/#chatmember) object on success.
    
    More info at: https://core.telegram.org/bots/api/#getchatmember
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMethod.__init__(  # type: ignore
            obj, "getChatMember", [ChatMember])
        return obj


    # --- arguments here ---
    chat_id: int | str = field(metadata={"ac_type": [int, str], "ac_name": "chat_id"})
    """Unique identifier for the target chat or username of the target supergroup or channel (in the format `@channelusername`)
    """

    user_id: int = field(metadata={"ac_type": [int], "ac_name": "user_id"})
    """Unique identifier of the target user
    """

