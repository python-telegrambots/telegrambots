from dataclasses import dataclass, field
from typing import Any

from ..api_method import TelegramBotsMethod
from ..api_result import TelegramBotsApiResult



@dataclass(init=True, repr=True, slots=True)
class DeleteMessage(TelegramBotsMethod[TelegramBotsApiResult[bool]]):
    # --- description here ---
    """Use this method to delete a message, including service messages, with the following limitations:  
    \\- A message can only be deleted if it was sent less than 48 hours ago.  
    \\- A dice message in a private chat can only be deleted if it was sent more than 24 hours ago.  
    \\- Bots can delete outgoing messages in private chats, groups, and supergroups.  
    \\- Bots can delete incoming messages in private chats.  
    \\- Bots granted *can\\_post\\_messages* permissions can delete outgoing messages in channels.  
    \\- If the bot is an administrator of a group, it can delete any message there.  
    \\- If the bot has *can\\_delete\\_messages* permission in a supergroup or a channel, it can delete any message there.  
    Returns *True* on success.
    
    More info at: https://core.telegram.org/bots/api/#deletemessage
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMethod.__init__(  # type: ignore
            obj, "deleteMessage", [bool])
        return obj


    # --- arguments here ---
    chat_id: int | str = field(metadata={"ac_type": [int, str], "ac_name": "chat_id"})
    """Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
    """

    message_id: int = field(metadata={"ac_type": [int], "ac_name": "message_id"})
    """Identifier of the message to delete
    """

