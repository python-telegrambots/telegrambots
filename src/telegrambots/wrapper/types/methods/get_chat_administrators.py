from dataclasses import dataclass, field
from typing import Any

from ..api_method import TelegramBotsMethod
from ..api_result import TelegramBotsApiResult
from ..objects.chat_member import ChatMember


@dataclass(init=True, repr=True, slots=True)
class GetChatAdministrators(TelegramBotsMethod[TelegramBotsApiResult[list[ChatMember]]]):
    # --- description here ---
    """Use this method to get a list of administrators in a chat. On success, returns an Array of [ChatMember](https://core.telegram.org/bots/api/#chatmember) objects that contains information about all chat administrators except other bots. If the chat is a group or a supergroup and no administrators were appointed, only the creator will be returned.
    
    More info at: https://core.telegram.org/bots/api/#getchatadministrators
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMethod.__init__(  # type: ignore
            obj, "getChatAdministrators", [ChatMember])
        return obj


    # --- arguments here ---
    chat_id: int | str = field(metadata={"ac_type": [int, str], "ac_name": "chat_id"})
    """Unique identifier for the target chat or username of the target supergroup or channel (in the format `@channelusername`)
    """

