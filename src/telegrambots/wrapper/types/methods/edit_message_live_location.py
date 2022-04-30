from dataclasses import dataclass, field
from typing import Any, Optional

from ..api_method import TelegramBotsMethod
from ..api_result import TelegramBotsApiResult
from ..objects.message import Message
from ..objects.inline_keyboard_markup import InlineKeyboardMarkup


@dataclass(init=True, repr=True, slots=True)
class EditMessageLiveLocation(TelegramBotsMethod[TelegramBotsApiResult[Message | bool]]):
    # --- description here ---
    """Use this method to edit live location messages. A location can be edited until its *live\\_period* expires or editing is explicitly disabled by a call to [stopMessageLiveLocation](https://core.telegram.org/bots/api/#stopmessagelivelocation). On success, if the edited message is not an inline message, the edited [Message](https://core.telegram.org/bots/api/#message) is returned, otherwise *True* is returned.
    
    More info at: https://core.telegram.org/bots/api/#editmessagelivelocation
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMethod.__init__(  # type: ignore
            obj, "editMessageLiveLocation", [Message,bool])
        return obj


    # --- arguments here ---
    latitude: float = field(metadata={"ac_type": [float], "ac_name": "latitude"})
    """Latitude of new location
    """

    longitude: float = field(metadata={"ac_type": [float], "ac_name": "longitude"})
    """Longitude of new location
    """

    chat_id: Optional[int | str] = field(default=None, metadata={"ac_type": [int, str], "ac_name": "chat_id"})
    """Required if *inline\\_message\\_id* is not specified. Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
    """

    message_id: Optional[int] = field(default=None, metadata={"ac_type": [int], "ac_name": "message_id"})
    """Required if *inline\\_message\\_id* is not specified. Identifier of the message to edit
    """

    inline_message_id: Optional[str] = field(default=None, metadata={"ac_type": [str], "ac_name": "inline_message_id"})
    """Required if *chat\\_id* and *message\\_id* are not specified. Identifier of the inline message
    """

    horizontal_accuracy: Optional[float] = field(default=None, metadata={"ac_type": [float], "ac_name": "horizontal_accuracy"})
    """The radius of uncertainty for the location, measured in meters; 0-1500
    """

    heading: Optional[int] = field(default=None, metadata={"ac_type": [int], "ac_name": "heading"})
    """Direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.
    """

    proximity_alert_radius: Optional[int] = field(default=None, metadata={"ac_type": [int], "ac_name": "proximity_alert_radius"})
    """Maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.
    """

    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None, metadata={"ac_type": [InlineKeyboardMarkup], "ac_name": "reply_markup"})
    """A JSON-serialized object for a new [inline keyboard](https://core.telegram.org/bots#inline-keyboards-and-on-the-fly-updating).
    """

