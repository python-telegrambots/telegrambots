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
class SendVenue(TelegramBotsMethod[TelegramBotsApiResult[Message]]):
    # --- description here ---
    """Use this method to send information about a venue. On success, the sent [Message](https://core.telegram.org/bots/api/#message) is returned.
    
    More info at: https://core.telegram.org/bots/api/#sendvenue
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMethod.__init__(  # type: ignore
            obj, "sendVenue", [Message])
        return obj


    # --- arguments here ---
    chat_id: int | str = field(metadata={"ac_type": [int, str], "ac_name": "chat_id"})
    """Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
    """

    latitude: float = field(metadata={"ac_type": [float], "ac_name": "latitude"})
    """Latitude of the venue
    """

    longitude: float = field(metadata={"ac_type": [float], "ac_name": "longitude"})
    """Longitude of the venue
    """

    title: str = field(metadata={"ac_type": [str], "ac_name": "title"})
    """Name of the venue
    """

    address: str = field(metadata={"ac_type": [str], "ac_name": "address"})
    """Address of the venue
    """

    foursquare_id: Optional[str] = field(default=None, metadata={"ac_type": [str], "ac_name": "foursquare_id"})
    """Foursquare identifier of the venue
    """

    foursquare_type: Optional[str] = field(default=None, metadata={"ac_type": [str], "ac_name": "foursquare_type"})
    """Foursquare type of the venue, if known. (For example, “arts\\_entertainment/default”, “arts\\_entertainment/aquarium” or “food/icecream”.)
    """

    google_place_id: Optional[str] = field(default=None, metadata={"ac_type": [str], "ac_name": "google_place_id"})
    """Google Places identifier of the venue
    """

    google_place_type: Optional[str] = field(default=None, metadata={"ac_type": [str], "ac_name": "google_place_type"})
    """Google Places type of the venue. (See [supported types](https://developers.google.com/places/web-service/supported_types).)
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

