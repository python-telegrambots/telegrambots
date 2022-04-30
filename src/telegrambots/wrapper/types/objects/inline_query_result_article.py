from dataclasses import dataclass, field
from typing import Optional

from .inline_query_result import InlineQueryResult
from .inline_keyboard_markup import InlineKeyboardMarkup
from .input_message_content import InputMessageContent


@dataclass(init=True, repr=True, slots=True)
class InlineQueryResultArticle(InlineQueryResult):
    # --- description here ---
    """Represents a link to an article or web page.

    More info at: https://core.telegram.org/bots/api/#inlinequeryresultarticle
    """

    # --- properties here ---
    @property
    def type(self) -> str:
        self._type = 'article'
        return self._type

    id: str = field(metadata={"ac_type": [str], "ac_name": "id"})
    """Unique identifier for this result, 1-64 Bytes
    """

    title: str = field(metadata={"ac_type": [str], "ac_name": "title"})
    """Title of the result
    """

    input_message_content: InputMessageContent = field(
        metadata={"ac_type": [InputMessageContent], "ac_name": "input_message_content"})
    """Content of the message to be sent
    """

    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None, metadata={
                                                         "ac_type": [InlineKeyboardMarkup], "ac_name": "reply_markup"})
    """*Optional*. [Inline keyboard](https://core.telegram.org/bots#inline-keyboards-and-on-the-fly-updating) attached to the message
    """

    url: Optional[str] = field(default=None, metadata={
                               "ac_type": [str], "ac_name": "url"})
    """*Optional*. URL of the result
    """

    hide_url: Optional[bool] = field(
        default=None, metadata={"ac_type": [bool], "ac_name": "hide_url"})
    """*Optional*. Pass *True*, if you don't want the URL to be shown in the message
    """

    description: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "description"})
    """*Optional*. Short description of the result
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
