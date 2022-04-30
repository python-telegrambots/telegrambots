from dataclasses import dataclass, field
from typing import Literal, Optional

from .inline_query_result import InlineQueryResult
from .input_message_content import InputMessageContent
from .inline_keyboard_markup import InlineKeyboardMarkup
from .message_entity import MessageEntity


@dataclass(init=True, repr=True, slots=True)
class InlineQueryResultDocument(InlineQueryResult):
    # --- description here ---
    """Represents a link to a file. By default, this file will be sent by the user with an optional caption. Alternatively, you can use *input\\_message\\_content* to send a message with the specified content instead of the file. Currently, only **.PDF** and **.ZIP** files can be sent using this method.

    More info at: https://core.telegram.org/bots/api/#inlinequeryresultdocument
    """

    # --- properties here ---
    @property
    def type(self) -> str:
        self._type = 'document'
        return self._type

    id: str = field(metadata={"ac_type": [str], "ac_name": "id"})
    """Unique identifier for this result, 1-64 bytes
    """

    title: str = field(metadata={"ac_type": [str], "ac_name": "title"})
    """Title for the result
    """

    document_url: str = field(
        metadata={"ac_type": [str], "ac_name": "document_url"})
    """A valid URL for the file
    """

    mime_type: Literal["application/pdf", "application/zip"] = field(
        metadata={"ac_type": [str], "ac_name": "mime_type"})
    """Mime type of the content of the file, either “application/pdf” or “application/zip”
    """

    caption: Optional[str] = field(default=None, metadata={
                                   "ac_type": [str], "ac_name": "caption"})
    """*Optional*. Caption of the document to be sent, 0-1024 characters after entities parsing
    """

    parse_mode: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "parse_mode"})
    """*Optional*. Mode for parsing entities in the document caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details.
    """

    caption_entities: Optional[list[MessageEntity]] = field(
        default=None, metadata={"ac_type": [MessageEntity], "ac_name": "caption_entities"})
    """*Optional*. List of special entities that appear in the caption, which can be specified instead of *parse\\_mode*
    """

    description: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "description"})
    """*Optional*. Short description of the result
    """

    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None, metadata={
                                                         "ac_type": [InlineKeyboardMarkup], "ac_name": "reply_markup"})
    """*Optional*. Inline keyboard attached to the message
    """

    input_message_content: Optional[InputMessageContent] = field(default=None, metadata={
                                                                 "ac_type": [InputMessageContent], "ac_name": "input_message_content"})
    """*Optional*. Content of the message to be sent instead of the file
    """

    thumb_url: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "thumb_url"})
    """*Optional*. URL of the thumbnail (JPEG only) for the file
    """

    thumb_width: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "thumb_width"})
    """*Optional*. Thumbnail width
    """

    thumb_height: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "thumb_height"})
    """*Optional*. Thumbnail height
    """
