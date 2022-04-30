from dataclasses import dataclass, field
from typing import Optional

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject
from .input_message_content import InputMessageContent
from .message_entity import MessageEntity


@dataclass(init=True, repr=True, slots=True)
class InputTextMessageContent(InputMessageContent):
    # --- description here ---
    """Represents the [content](https://core.telegram.org/bots/api/#inputmessagecontent) of a text message to be sent as the result of an inline query.

    More info at: https://core.telegram.org/bots/api/#inputtextmessagecontent
    """

    # --- properties here ---
    message_text: str = field(metadata={"ac_type": [str], "ac_name": "message_text"})
    """Text of the message to be sent, 1-4096 characters
    """

    parse_mode: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "parse_mode"}
    )
    """*Optional*. Mode for parsing entities in the message text. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details.
    """

    entities: Optional[list[MessageEntity]] = field(
        default=None, metadata={"ac_type": [MessageEntity], "ac_name": "entities"}
    )
    """*Optional*. List of special entities that appear in message text, which can be specified instead of *parse\\_mode*
    """

    disable_web_page_preview: Optional[bool] = field(
        default=None,
        metadata={"ac_type": [bool], "ac_name": "disable_web_page_preview"},
    )
    """*Optional*. Disables link previews for links in the sent message
    """
