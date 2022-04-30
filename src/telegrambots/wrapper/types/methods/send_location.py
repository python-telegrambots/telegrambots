from dataclasses import dataclass, field
from typing import Any, Optional

from ..api_method import TelegramBotsMethod
from ..api_result import TelegramBotsApiResult
from ..objects.force_reply import ForceReply
from ..objects.message import Message
from ..objects.reply_keyboard_remove import ReplyKeyboardRemove
from ..objects.inline_keyboard_markup import InlineKeyboardMarkup
from ..objects.reply_keyboard_markup import ReplyKeyboardMarkup


@dataclass(init=True, repr=True, slots=True)
class SendLocation(TelegramBotsMethod[TelegramBotsApiResult[Message]]):
    # --- description here ---
    """Use this method to send point on the map. On success, the sent [Message](https://core.telegram.org/bots/api/#message) is returned.
    
    More info at: https://core.telegram.org/bots/api/#sendlocation
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMethod.__init__(  # type: ignore
            obj, "sendLocation", [Message])
        return obj


    # --- arguments here ---
    chat_id: int | str = field(metadata={"ac_type": [int, str], "ac_name": "chat_id"})
    """Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
    """

    latitude: float = field(metadata={"ac_type": [float], "ac_name": "latitude"})
    """Latitude of the location
    """

    longitude: float = field(metadata={"ac_type": [float], "ac_name": "longitude"})
    """Longitude of the location
    """

    horizontal_accuracy: Optional[float] = field(default=None, metadata={"ac_type": [float], "ac_name": "horizontal_accuracy"})
    """The radius of uncertainty for the location, measured in meters; 0-1500
    """

    live_period: Optional[int] = field(default=None, metadata={"ac_type": [int], "ac_name": "live_period"})
    """Period in seconds for which the location will be updated (see [Live Locations](https://telegram.org/blog/live-locations), should be between 60 and 86400.
    """

    heading: Optional[int] = field(default=None, metadata={"ac_type": [int], "ac_name": "heading"})
    """For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.
    """

    proximity_alert_radius: Optional[int] = field(default=None, metadata={"ac_type": [int], "ac_name": "proximity_alert_radius"})
    """For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.
    """

    disable_notification: Optional[bool] = field(default=None, metadata={"ac_type": [bool], "ac_name": "disable_notification"})
    """Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound.
    """

    protect_content: Optional[bool] = field(default=None, metadata={"ac_type": [bool], "ac_name": "protect_content"})
    """Protects the contents of the sent message from forwarding and saving
    """

    reply_to_message_id: Optional[int] = field(default=None, metadata={"ac_type": [int], "ac_name": "reply_to_message_id"})
    """If the message is a reply, ID of the original message
    """

    allow_sending_without_reply: Optional[bool] = field(default=None, metadata={"ac_type": [bool], "ac_name": "allow_sending_without_reply"})
    """Pass *True*, if the message should be sent even if the specified replied-to message is not found
    """

    reply_markup: Optional[InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply] = field(default=None, metadata={"ac_type": [InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply], "ac_name": "reply_markup"})
    """Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots#inline-keyboards-and-on-the-fly-updating), [custom reply keyboard](https://core.telegram.org/bots#keyboards), instructions to remove reply keyboard or to force a reply from the user.
    """

