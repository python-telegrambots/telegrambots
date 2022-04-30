from dataclasses import dataclass, field
from typing import Literal, Optional

from .inline_query_result import InlineQueryResult
from .input_message_content import InputMessageContent
from .inline_keyboard_markup import InlineKeyboardMarkup
from .message_entity import MessageEntity


@dataclass(init=True, repr=True, slots=True)
class InlineQueryResultMpeg4Gif(InlineQueryResult):
    # --- description here ---
    """Represents a link to a video animation (H.264/MPEG-4 AVC video without sound). By default, this animated MPEG-4 file will be sent by the user with optional caption. Alternatively, you can use *input\\_message\\_content* to send a message with the specified content instead of the animation.

    More info at: https://core.telegram.org/bots/api/#inlinequeryresultmpeg4gif
    """

    # --- properties here ---
    @property
    def type(self) -> str:
        self._type = 'mpeg4_gif'
        return self._type

    id: str = field(metadata={"ac_type": [str], "ac_name": "id"})
    """Unique identifier for this result, 1-64 bytes
    """

    mpeg4_url: str = field(metadata={"ac_type": [str], "ac_name": "mpeg4_url"})
    """A valid URL for the MP4 file. File size must not exceed 1MB
    """

    thumb_url: str = field(metadata={"ac_type": [str], "ac_name": "thumb_url"})
    """URL of the static (JPEG or GIF) or animated (MPEG4) thumbnail for the result
    """

    mpeg4_width: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "mpeg4_width"})
    """*Optional*. Video width
    """

    mpeg4_height: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "mpeg4_height"})
    """*Optional*. Video height
    """

    mpeg4_duration: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "mpeg4_duration"})
    """*Optional*. Video duration in seconds
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
    """*Optional*. Caption of the MPEG-4 file to be sent, 0-1024 characters after entities parsing
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
    """*Optional*. Content of the message to be sent instead of the video animation
    """
