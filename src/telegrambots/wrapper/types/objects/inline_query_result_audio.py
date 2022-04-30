from dataclasses import dataclass, field
from typing import Optional

from .inline_query_result import InlineQueryResult
from .input_message_content import InputMessageContent
from .inline_keyboard_markup import InlineKeyboardMarkup
from .message_entity import MessageEntity


@dataclass(init=True, repr=True, slots=True)
class InlineQueryResultAudio(InlineQueryResult):
    # --- description here ---
    """Represents a link to an MP3 audio file. By default, this audio file will be sent by the user. Alternatively, you can use *input\\_message\\_content* to send a message with the specified content instead of the audio.

    More info at: https://core.telegram.org/bots/api/#inlinequeryresultaudio
    """

    # --- properties here ---
    @property
    def type(self) -> str:
        self._type = 'audio'
        return self._type

    id: str = field(metadata={"ac_type": [str], "ac_name": "id"})
    """Unique identifier for this result, 1-64 bytes
    """

    audio_url: str = field(metadata={"ac_type": [str], "ac_name": "audio_url"})
    """A valid URL for the audio file
    """

    title: str = field(metadata={"ac_type": [str], "ac_name": "title"})
    """Title
    """

    caption: Optional[str] = field(default=None, metadata={
                                   "ac_type": [str], "ac_name": "caption"})
    """*Optional*. Caption, 0-1024 characters after entities parsing
    """

    parse_mode: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "parse_mode"})
    """*Optional*. Mode for parsing entities in the audio caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details.
    """

    caption_entities: Optional[list[MessageEntity]] = field(
        default=None, metadata={"ac_type": [MessageEntity], "ac_name": "caption_entities"})
    """*Optional*. List of special entities that appear in the caption, which can be specified instead of *parse\\_mode*
    """

    performer: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "performer"})
    """*Optional*. Performer
    """

    audio_duration: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "audio_duration"})
    """*Optional*. Audio duration in seconds
    """

    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None, metadata={
                                                         "ac_type": [InlineKeyboardMarkup], "ac_name": "reply_markup"})
    """*Optional*. [Inline keyboard](https://core.telegram.org/bots#inline-keyboards-and-on-the-fly-updating) attached to the message
    """

    input_message_content: Optional[InputMessageContent] = field(default=None, metadata={
                                                                 "ac_type": [InputMessageContent], "ac_name": "input_message_content"})
    """*Optional*. Content of the message to be sent instead of the audio
    """
