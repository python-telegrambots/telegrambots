from dataclasses import dataclass, field
from typing import Optional

from .inline_query_result import InlineQueryResult
from .input_message_content import InputMessageContent
from .inline_keyboard_markup import InlineKeyboardMarkup
from .message_entity import MessageEntity


@dataclass(init=True, repr=True, slots=True)
class InlineQueryResultPhoto(InlineQueryResult):
    # --- description here ---
    """Represents a link to a photo. By default, this photo will be sent by the user with optional caption. Alternatively, you can use *input\\_message\\_content* to send a message with the specified content instead of the photo.

    More info at: https://core.telegram.org/bots/api/#inlinequeryresultphoto
    """

    # --- properties here ---
    @property
    def type(self) -> str:
        self._type = 'photo'
        return self._type

    id: str = field(metadata={"ac_type": [str], "ac_name": "id"})
    """Unique identifier for this result, 1-64 bytes
    """

    photo_url: str = field(metadata={"ac_type": [str], "ac_name": "photo_url"})
    """A valid URL of the photo. Photo must be in **JPEG** format. Photo size must not exceed 5MB
    """

    thumb_url: str = field(metadata={"ac_type": [str], "ac_name": "thumb_url"})
    """URL of the thumbnail for the photo
    """

    photo_width: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "photo_width"})
    """*Optional*. Width of the photo
    """

    photo_height: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "photo_height"})
    """*Optional*. Height of the photo
    """

    title: Optional[str] = field(default=None, metadata={
                                 "ac_type": [str], "ac_name": "title"})
    """*Optional*. Title for the result
    """

    description: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "description"})
    """*Optional*. Short description of the result
    """

    caption: Optional[str] = field(default=None, metadata={
                                   "ac_type": [str], "ac_name": "caption"})
    """*Optional*. Caption of the photo to be sent, 0-1024 characters after entities parsing
    """

    parse_mode: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "parse_mode"})
    """*Optional*. Mode for parsing entities in the photo caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details.
    """

    caption_entities: Optional[list[MessageEntity]] = field(
        default=None, metadata={"ac_type": [MessageEntity], "ac_name": "caption_entities"})
    """*Optional*. List of special entities that appear in the caption, which can be specified instead of *parse\\_mode*
    """

    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None, metadata={
                                                         "ac_type": [InlineKeyboardMarkup], "ac_name": "reply_markup"})
    """*Optional*. [Inline keyboard](https://core.telegram.org/bots#inline-keyboards-and-on-the-fly-updating) attached to the message
    """

    input_message_content: Optional[InputMessageContent] = field(default=None, metadata={
                                                                 "ac_type": [InputMessageContent], "ac_name": "input_message_content"})
    """*Optional*. Content of the message to be sent instead of the photo
    """
