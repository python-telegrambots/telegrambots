from dataclasses import dataclass, field
from typing import Optional

from .inline_query_result import InlineQueryResult
from .input_message_content import InputMessageContent
from .inline_keyboard_markup import InlineKeyboardMarkup
from .message_entity import MessageEntity


@dataclass(init=True, repr=True, slots=True)
class InlineQueryResultCachedDocument(InlineQueryResult):
    # --- description here ---
    """Represents a link to a file stored on the Telegram servers. By default, this file will be sent by the user with an optional caption. Alternatively, you can use *input\\_message\\_content* to send a message with the specified content instead of the file.

    More info at: https://core.telegram.org/bots/api/#inlinequeryresultcacheddocument
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

    document_file_id: str = field(
        metadata={"ac_type": [str], "ac_name": "document_file_id"})
    """A valid file identifier for the file
    """

    description: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "description"})
    """*Optional*. Short description of the result
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

    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None, metadata={
                                                         "ac_type": [InlineKeyboardMarkup], "ac_name": "reply_markup"})
    """*Optional*. [Inline keyboard](https://core.telegram.org/bots#inline-keyboards-and-on-the-fly-updating) attached to the message
    """

    input_message_content: Optional[InputMessageContent] = field(default=None, metadata={
                                                                 "ac_type": [InputMessageContent], "ac_name": "input_message_content"})
    """*Optional*. Content of the message to be sent instead of the file
    """
