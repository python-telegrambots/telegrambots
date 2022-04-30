from dataclasses import dataclass, field
from typing import Any, Optional

from ..api_method import TelegramBotsMethod
from ..api_result import TelegramBotsApiResult



@dataclass(init=True, repr=True, slots=True)
class UnpinChatMessage(TelegramBotsMethod[TelegramBotsApiResult[bool]]):
    # --- description here ---
    """Use this method to remove a message from the list of pinned messages in a chat. If the chat is not a private chat, the bot must be an administrator in the chat for this to work and must have the 'can\\_pin\\_messages' administrator right in a supergroup or 'can\\_edit\\_messages' administrator right in a channel. Returns *True* on success.
    
    More info at: https://core.telegram.org/bots/api/#unpinchatmessage
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMethod.__init__(  # type: ignore
            obj, "unpinChatMessage", [bool])
        return obj


    # --- arguments here ---
    chat_id: int | str = field(metadata={"ac_type": [int, str], "ac_name": "chat_id"})
    """Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
    """

    message_id: Optional[int] = field(default=None, metadata={"ac_type": [int], "ac_name": "message_id"})
    """Identifier of a message to unpin. If not specified, the most recent pinned message (by sending date) will be unpinned.
    """

