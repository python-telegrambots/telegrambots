from dataclasses import dataclass, field
from typing import Any, Optional

from ..api_method import TelegramBotsMethod
from ..api_result import TelegramBotsApiResult
from ..objects.message import Message
from ..objects.message_entity import MessageEntity
from ..objects.inline_keyboard_markup import InlineKeyboardMarkup


@dataclass(init=True, repr=True, slots=True)
class EditMessageCaption(TelegramBotsMethod[TelegramBotsApiResult[Message | bool]]):
    # --- description here ---
    """Use this method to edit captions of messages. On success, if the edited message is not an inline message, the edited [Message](https://core.telegram.org/bots/api/#message) is returned, otherwise *True* is returned.
    
    More info at: https://core.telegram.org/bots/api/#editmessagecaption
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMethod.__init__(  # type: ignore
            obj, "editMessageCaption", [Message,bool])
        return obj


    # --- arguments here ---
    chat_id: Optional[int | str] = field(default=None, metadata={"ac_type": [int, str], "ac_name": "chat_id"})
    """Required if *inline\\_message\\_id* is not specified. Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
    """

    message_id: Optional[int] = field(default=None, metadata={"ac_type": [int], "ac_name": "message_id"})
    """Required if *inline\\_message\\_id* is not specified. Identifier of the message to edit
    """

    inline_message_id: Optional[str] = field(default=None, metadata={"ac_type": [str], "ac_name": "inline_message_id"})
    """Required if *chat\\_id* and *message\\_id* are not specified. Identifier of the inline message
    """

    caption: Optional[str] = field(default=None, metadata={"ac_type": [str], "ac_name": "caption"})
    """New caption of the message, 0-1024 characters after entities parsing
    """

    parse_mode: Optional[str] = field(default=None, metadata={"ac_type": [str], "ac_name": "parse_mode"})
    """Mode for parsing entities in the message caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details.
    """

    caption_entities: Optional[list[MessageEntity]] = field(default=None, metadata={"ac_type": [MessageEntity], "ac_name": "caption_entities"})
    """A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse\\_mode*
    """

    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None, metadata={"ac_type": [InlineKeyboardMarkup], "ac_name": "reply_markup"})
    """A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots#inline-keyboards-and-on-the-fly-updating).
    """

