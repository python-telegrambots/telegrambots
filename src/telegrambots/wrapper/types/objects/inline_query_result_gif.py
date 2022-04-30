from dataclasses import dataclass, field
from typing import Literal, Optional

from .inline_query_result import InlineQueryResult
from .input_message_content import InputMessageContent
from .inline_keyboard_markup import InlineKeyboardMarkup
from .message_entity import MessageEntity


@dataclass(init=True, repr=True, slots=True)
class InlineQueryResultGif(InlineQueryResult):
    # --- description here ---
    """Represents a link to an animated GIF file. By default, this animated GIF file will be sent by the user with optional caption. Alternatively, you can use *input\\_message\\_content* to send a message with the specified content instead of the animation.

    More info at: https://core.telegram.org/bots/api/#inlinequeryresultgif
    """

    # --- properties here ---
    @property
    def type(self) -> str:
        self._type = 'gif'
        return self._type

    id: str = field(metadata={"ac_type": [str], "ac_name": "id"})
    """Unique identifier for this result, 1-64 bytes
    """

    gif_url: str = field(metadata={"ac_type": [str], "ac_name": "gif_url"})
    """A valid URL for the GIF file. File size must not exceed 1MB
    """

    thumb_url: str = field(metadata={"ac_type": [str], "ac_name": "thumb_url"})
    """URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result
    """

    gif_width: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "gif_width"})
    """*Optional*. Width of the GIF
    """

    gif_height: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "gif_height"})
    """*Optional*. Height of the GIF
    """

    gif_duration: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "gif_duration"})
    """*Optional*. Duration of the GIF in seconds
    """

    thumb_mime_type: Literal["image/jpeg", "image/gif", "video/mp4"] = field(
        default='image/jpeg', metadata={"ac_type": [str], "ac_name": "thumb_mime_type"})
    """*Optional*. MIME type of the thumbnail, must be one of “image/jpeg”, “image/gif”, or “video/mp4”. Defaults to “image/jpeg”
    """

    title: Optional[str] = field(default=None, metadata={
                                 "ac_type": [str], "ac_name": "title"})
    """*Optional*. Title for the result
    """

    caption: Optional[str] = field(default=None, metadata={
                                   "ac_type": [str], "ac_name": "caption"})
    """*Optional*. Caption of the GIF file to be sent, 0-1024 characters after entities parsing
    """

    parse_mode: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "parse_mode"})
    """*Optional*. Mode for parsing entities in the caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details.
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
    """*Optional*. Content of the message to be sent instead of the GIF animation
    """
