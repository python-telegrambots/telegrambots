from dataclasses import dataclass, field
from typing import Any

from ..api_method import TelegramBotsMethod
from ..api_result import TelegramBotsApiResult



@dataclass(init=True, repr=True, slots=True)
class GetChatMemberCount(TelegramBotsMethod[TelegramBotsApiResult[int]]):
    # --- description here ---
    """Use this method to get the number of members in a chat. Returns *Int* on success.
    
    More info at: https://core.telegram.org/bots/api/#getchatmembercount
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMethod.__init__(  # type: ignore
            obj, "getChatMemberCount", [int])
        return obj


    # --- arguments here ---
    chat_id: int | str = field(metadata={"ac_type": [int, str], "ac_name": "chat_id"})
    """Unique identifier for the target chat or username of the target supergroup or channel (in the format `@channelusername`)
    """

