from dataclasses import dataclass, field
from typing import Optional

from .inline_query_result import InlineQueryResult
from .inline_keyboard_markup import InlineKeyboardMarkup
from .input_message_content import InputMessageContent


@dataclass(init=True, repr=True, slots=True)
class InlineQueryResultContact(InlineQueryResult):
    # --- description here ---
    """Represents a contact with a phone number. By default, this contact will be sent by the user. Alternatively, you can use *input\\_message\\_content* to send a message with the specified content instead of the contact.

    More info at: https://core.telegram.org/bots/api/#inlinequeryresultcontact
    """

    # --- properties here ---
    @property
    def type(self) -> str:
        self._type = 'contact'
        return self._type

    id: str = field(metadata={"ac_type": [str], "ac_name": "id"})
    """Unique identifier for this result, 1-64 Bytes
    """

    phone_number: str = field(
        metadata={"ac_type": [str], "ac_name": "phone_number"})
    """Contact's phone number
    """

    first_name: str = field(
        metadata={"ac_type": [str], "ac_name": "first_name"})
    """Contact's first name
    """

    last_name: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "last_name"})
    """*Optional*. Contact's last name
    """

    vcard: Optional[str] = field(default=None, metadata={
                                 "ac_type": [str], "ac_name": "vcard"})
    """*Optional*. Additional data about the contact in the form of a [vCard](https://en.wikipedia.org/wiki/VCard), 0-2048 bytes
    """

    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None, metadata={
                                                         "ac_type": [InlineKeyboardMarkup], "ac_name": "reply_markup"})
    """*Optional*. [Inline keyboard](https://core.telegram.org/bots#inline-keyboards-and-on-the-fly-updating) attached to the message
    """

    input_message_content: Optional[InputMessageContent] = field(default=None, metadata={
                                                                 "ac_type": [InputMessageContent], "ac_name": "input_message_content"})
    """*Optional*. Content of the message to be sent instead of the contact
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
