from dataclasses import dataclass, field
from typing import Any, Optional

from ..api_method import TelegramBotsMethod
from ..api_result import TelegramBotsApiResult
from ..objects.message import Message


@dataclass(init=True, repr=True, slots=True)
class ForwardMessage(TelegramBotsMethod[TelegramBotsApiResult[Message]]):
    # --- description here ---
    """Use this method to forward messages of any kind. Service messages can't be forwarded. On success, the sent [Message](https://core.telegram.org/bots/api/#message) is returned.
    
    More info at: https://core.telegram.org/bots/api/#forwardmessage
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMethod.__init__(  # type: ignore
            obj, "forwardMessage", [Message])
        return obj


    # --- arguments here ---
    chat_id: int | str = field(metadata={"ac_type": [int, str], "ac_name": "chat_id"})
    """Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
    """

    from_chat_id: int | str = field(metadata={"ac_type": [int, str], "ac_name": "from_chat_id"})
    """Unique identifier for the chat where the original message was sent (or channel username in the format `@channelusername`)
    """

    message_id: int = field(metadata={"ac_type": [int], "ac_name": "message_id"})
    """Message identifier in the chat specified in *from\\_chat\\_id*
    """

    disable_notification: Optional[bool] = field(default=None, metadata={"ac_type": [bool], "ac_name": "disable_notification"})
    """Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound.
    """

    protect_content: Optional[bool] = field(default=None, metadata={"ac_type": [bool], "ac_name": "protect_content"})
    """Protects the contents of the forwarded message from forwarding and saving
    """

