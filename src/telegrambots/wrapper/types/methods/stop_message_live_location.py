from dataclasses import dataclass, field
from typing import Any, Optional

from ..api_method import TelegramBotsMethod
from ..api_result import TelegramBotsApiResult
from ..objects.message import Message
from ..objects.inline_keyboard_markup import InlineKeyboardMarkup


@dataclass(init=True, repr=True, slots=True)
class StopMessageLiveLocation(
    TelegramBotsMethod[TelegramBotsApiResult[Optional[Message]]]
):
    # --- description here ---
    """Use this method to stop updating a live location message before *live\\_period* expires. On success, if the message is not an inline message, the edited [Message](https://core.telegram.org/bots/api/#message) is returned, otherwise *True* is returned.

    More info at: https://core.telegram.org/bots/api/#stopmessagelivelocation
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMethod.__init__(  # type: ignore
            obj, "stopMessageLiveLocation", [Message, bool]
        )
        return obj

    # --- arguments here ---
    chat_id: Optional[int | str] = field(
        default=None, metadata={"ac_type": [int, str], "ac_name": "chat_id"}
    )
    """Required if *inline\\_message\\_id* is not specified. Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
    """

    message_id: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "message_id"}
    )
    """Required if *inline\\_message\\_id* is not specified. Identifier of the message with live location to stop
    """

    inline_message_id: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "inline_message_id"}
    )
    """Required if *chat\\_id* and *message\\_id* are not specified. Identifier of the inline message
    """

    reply_markup: Optional[InlineKeyboardMarkup] = field(
        default=None,
        metadata={"ac_type": [InlineKeyboardMarkup], "ac_name": "reply_markup"},
    )
    """A JSON-serialized object for a new [inline keyboard](https://core.telegram.org/bots#inline-keyboards-and-on-the-fly-updating).
    """
