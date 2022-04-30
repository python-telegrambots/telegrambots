from dataclasses import dataclass, field
from typing import Optional

from .inline_query_result import InlineQueryResult
from .inline_keyboard_markup import InlineKeyboardMarkup
from .input_message_content import InputMessageContent


@dataclass(init=True, repr=True, slots=True)
class InlineQueryResultVenue(InlineQueryResult):
    # --- description here ---
    """Represents a venue. By default, the venue will be sent by the user. Alternatively, you can use *input\\_message\\_content* to send a message with the specified content instead of the venue.

    More info at: https://core.telegram.org/bots/api/#inlinequeryresultvenue
    """

    # --- properties here ---
    @property
    def type(self) -> str:
        self._type = 'venue'
        return self._type

    id: str = field(metadata={"ac_type": [str], "ac_name": "id"})
    """Unique identifier for this result, 1-64 Bytes
    """

    latitude: float = field(
        metadata={"ac_type": [float], "ac_name": "latitude"})
    """Latitude of the venue location in degrees
    """

    longitude: float = field(
        metadata={"ac_type": [float], "ac_name": "longitude"})
    """Longitude of the venue location in degrees
    """

    title: str = field(metadata={"ac_type": [str], "ac_name": "title"})
    """Title of the venue
    """

    address: str = field(metadata={"ac_type": [str], "ac_name": "address"})
    """Address of the venue
    """

    foursquare_id: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "foursquare_id"})
    """*Optional*. Foursquare identifier of the venue if known
    """

    foursquare_type: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "foursquare_type"})
    """*Optional*. Foursquare type of the venue, if known. (For example, “arts\\_entertainment/default”, “arts\\_entertainment/aquarium” or “food/icecream”.)
    """

    google_place_id: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "google_place_id"})
    """*Optional*. Google Places identifier of the venue
    """

    google_place_type: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "google_place_type"})
    """*Optional*. Google Places type of the venue. (See [supported types](https://developers.google.com/places/web-service/supported_types).)
    """

    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None, metadata={
                                                         "ac_type": [InlineKeyboardMarkup], "ac_name": "reply_markup"})
    """*Optional*. [Inline keyboard](https://core.telegram.org/bots#inline-keyboards-and-on-the-fly-updating) attached to the message
    """

    input_message_content: Optional[InputMessageContent] = field(default=None, metadata={
                                                                 "ac_type": [InputMessageContent], "ac_name": "input_message_content"})
    """*Optional*. Content of the message to be sent instead of the venue
    """

    thumb_url: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "thumb_url"})
    """*Optional*. Url of the thumbnail for the result
    """

    thumb_width: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "thumb_width"})
    """*Optional*. Thumbnail width
    """

    thumb_height: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "thumb_height"})
    """*Optional*. Thumbnail height
    """
