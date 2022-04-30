from dataclasses import dataclass, field
from typing import Optional

from .inline_query_result import InlineQueryResult
from .inline_keyboard_markup import InlineKeyboardMarkup
from .input_message_content import InputMessageContent


@dataclass(init=True, repr=True, slots=True)
class InlineQueryResultCachedSticker(InlineQueryResult):
    # --- description here ---
    """Represents a link to a sticker stored on the Telegram servers. By default, this sticker will be sent by the user. Alternatively, you can use *input\\_message\\_content* to send a message with the specified content instead of the sticker.

    More info at: https://core.telegram.org/bots/api/#inlinequeryresultcachedsticker
    """

    # --- properties here ---
    @property
    def type(self) -> str:
        self._type = 'sticker'
        return self._type

    id: str = field(metadata={"ac_type": [str], "ac_name": "id"})
    """Unique identifier for this result, 1-64 bytes
    """

    sticker_file_id: str = field(
        metadata={"ac_type": [str], "ac_name": "sticker_file_id"})
    """A valid file identifier of the sticker
    """

    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None, metadata={
                                                         "ac_type": [InlineKeyboardMarkup], "ac_name": "reply_markup"})
    """*Optional*. [Inline keyboard](https://core.telegram.org/bots#inline-keyboards-and-on-the-fly-updating) attached to the message
    """

    input_message_content: Optional[InputMessageContent] = field(default=None, metadata={
                                                                 "ac_type": [InputMessageContent], "ac_name": "input_message_content"})
    """*Optional*. Content of the message to be sent instead of the sticker
    """
