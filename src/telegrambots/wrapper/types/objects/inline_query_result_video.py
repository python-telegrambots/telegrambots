from dataclasses import dataclass, field
from typing import Literal, Optional

from .inline_query_result import InlineQueryResult
from .input_message_content import InputMessageContent
from .inline_keyboard_markup import InlineKeyboardMarkup
from .message_entity import MessageEntity


@dataclass(init=True, repr=True, slots=True)
class InlineQueryResultVideo(InlineQueryResult):
    # --- description here ---
    """Represents a link to a page containing an embedded video player or a video file. By default, this video file will be sent by the user with an optional caption. Alternatively, you can use *input\\_message\\_content* to send a message with the specified content instead of the video.

    If an InlineQueryResultVideo message contains an embedded video (e.g., YouTube), you **must** replace its content using *input\\_message\\_content*.

    More info at: https://core.telegram.org/bots/api/#inlinequeryresultvideo
    """

    # --- properties here ---
    @property
    def type(self) -> str:
        self._type = 'video'
        return self._type

    id: str = field(metadata={"ac_type": [str], "ac_name": "id"})
    """Unique identifier for this result, 1-64 bytes
    """

    video_url: str = field(metadata={"ac_type": [str], "ac_name": "video_url"})
    """A valid URL for the embedded video player or video file
    """

    mime_type: Literal["text/html", "video/mp4"] = field(
        metadata={"ac_type": [str], "ac_name": "mime_type"})
    """Mime type of the content of video url, “text/html” or “video/mp4”
    """

    thumb_url: str = field(metadata={"ac_type": [str], "ac_name": "thumb_url"})
    """URL of the thumbnail (JPEG only) for the video
    """

    title: str = field(metadata={"ac_type": [str], "ac_name": "title"})
    """Title for the result
    """

    caption: Optional[str] = field(default=None, metadata={
                                   "ac_type": [str], "ac_name": "caption"})
    """*Optional*. Caption of the video to be sent, 0-1024 characters after entities parsing
    """

    parse_mode: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "parse_mode"})
    """*Optional*. Mode for parsing entities in the video caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details.
    """

    caption_entities: Optional[list[MessageEntity]] = field(
        default=None, metadata={"ac_type": [MessageEntity], "ac_name": "caption_entities"})
    """*Optional*. List of special entities that appear in the caption, which can be specified instead of *parse\\_mode*
    """

    video_width: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "video_width"})
    """*Optional*. Video width
    """

    video_height: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "video_height"})
    """*Optional*. Video height
    """

    video_duration: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "video_duration"})
    """*Optional*. Video duration in seconds
    """

    description: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "description"})
    """*Optional*. Short description of the result
    """

    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None, metadata={
                                                         "ac_type": [InlineKeyboardMarkup], "ac_name": "reply_markup"})
    """*Optional*. [Inline keyboard](https://core.telegram.org/bots#inline-keyboards-and-on-the-fly-updating) attached to the message
    """

    input_message_content: Optional[InputMessageContent] = field(default=None, metadata={
                                                                 "ac_type": [InputMessageContent], "ac_name": "input_message_content"})
    """*Optional*. Content of the message to be sent instead of the video. This field is **required** if InlineQueryResultVideo is used to send an HTML-page as a result (e.g., a YouTube video).
    """
