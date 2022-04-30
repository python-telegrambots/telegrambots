from dataclasses import dataclass, field
from typing import Optional

from .inline_query_result import InlineQueryResult
from .inline_keyboard_markup import InlineKeyboardMarkup
from .input_message_content import InputMessageContent


@dataclass(init=True, repr=True, slots=True)
class InlineQueryResultLocation(InlineQueryResult):
    # --- description here ---
    """Represents a location on a map. By default, the location will be sent by the user. Alternatively, you can use *input\\_message\\_content* to send a message with the specified content instead of the location.

    More info at: https://core.telegram.org/bots/api/#inlinequeryresultlocation
    """

    # --- properties here ---
    @property
    def type(self) -> str:
        self._type = 'locations'
        return self._type


    id: str = field(metadata={"ac_type": [str], "ac_name": "id"})
    """Unique identifier for this result, 1-64 Bytes
    """

    latitude: float = field(
        metadata={"ac_type": [float], "ac_name": "latitude"})
    """Location latitude in degrees
    """

    longitude: float = field(
        metadata={"ac_type": [float], "ac_name": "longitude"})
    """Location longitude in degrees
    """

    title: str = field(metadata={"ac_type": [str], "ac_name": "title"})
    """Location title
    """

    horizontal_accuracy: Optional[float] = field(
        default=None, metadata={"ac_type": [float], "ac_name": "horizontal_accuracy"})
    """*Optional*. The radius of uncertainty for the location, measured in meters; 0-1500
    """

    live_period: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "live_period"})
    """*Optional*. Period in seconds for which the location can be updated, should be between 60 and 86400.
    """

    heading: Optional[int] = field(default=None, metadata={
                                   "ac_type": [int], "ac_name": "heading"})
    """*Optional*. For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.
    """

    proximity_alert_radius: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "proximity_alert_radius"})
    """*Optional*. For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.
    """

    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None, metadata={
                                                         "ac_type": [InlineKeyboardMarkup], "ac_name": "reply_markup"})
    """*Optional*. [Inline keyboard](https://core.telegram.org/bots#inline-keyboards-and-on-the-fly-updating) attached to the message
    """

    input_message_content: Optional[InputMessageContent] = field(default=None, metadata={
                                                                 "ac_type": [InputMessageContent], "ac_name": "input_message_content"})
    """*Optional*. Content of the message to be sent instead of the location
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
