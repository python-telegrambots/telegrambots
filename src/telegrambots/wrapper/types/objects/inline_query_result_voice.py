from dataclasses import dataclass, field
from typing import Optional

from .inline_query_result import InlineQueryResult
from .input_message_content import InputMessageContent
from .inline_keyboard_markup import InlineKeyboardMarkup
from .message_entity import MessageEntity


@dataclass(init=True, repr=True, slots=True)
class InlineQueryResultVoice(InlineQueryResult):
    # --- description here ---
    """Represents a link to a voice recording in an .OGG container encoded with OPUS. By default, this voice recording will be sent by the user. Alternatively, you can use *input\\_message\\_content* to send a message with the specified content instead of the the voice message.

    More info at: https://core.telegram.org/bots/api/#inlinequeryresultvoice
    """

    # --- properties here ---
    @property
    def type(self) -> str:
        self._type = 'voice'
        return self._type

    id: str = field(metadata={"ac_type": [str], "ac_name": "id"})
    """Unique identifier for this result, 1-64 bytes
    """

    voice_url: str = field(metadata={"ac_type": [str], "ac_name": "voice_url"})
    """A valid URL for the voice recording
    """

    title: str = field(metadata={"ac_type": [str], "ac_name": "title"})
    """Recording title
    """

    caption: Optional[str] = field(default=None, metadata={
                                   "ac_type": [str], "ac_name": "caption"})
    """*Optional*. Caption, 0-1024 characters after entities parsing
    """

    parse_mode: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "parse_mode"})
    """*Optional*. Mode for parsing entities in the voice message caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details.
    """

    caption_entities: Optional[list[MessageEntity]] = field(
        default=None, metadata={"ac_type": [MessageEntity], "ac_name": "caption_entities"})
    """*Optional*. List of special entities that appear in the caption, which can be specified instead of *parse\\_mode*
    """

    voice_duration: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "voice_duration"})
    """*Optional*. Recording duration in seconds
    """

    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None, metadata={
                                                         "ac_type": [InlineKeyboardMarkup], "ac_name": "reply_markup"})
    """*Optional*. [Inline keyboard](https://core.telegram.org/bots#inline-keyboards-and-on-the-fly-updating) attached to the message
    """

    input_message_content: Optional[InputMessageContent] = field(default=None, metadata={
                                                                 "ac_type": [InputMessageContent], "ac_name": "input_message_content"})
    """*Optional*. Content of the message to be sent instead of the voice recording
    """
