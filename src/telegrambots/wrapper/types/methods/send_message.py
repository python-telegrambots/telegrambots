from dataclasses import dataclass, field
from typing import Any, Optional

from ..api_method import TelegramBotsMethod
from ..api_result import TelegramBotsApiResult
from ..objects.force_reply import ForceReply
from ..objects.reply_keyboard_remove import ReplyKeyboardRemove
from ..objects.message import Message
from ..objects.message_entity import MessageEntity
from ..objects.inline_keyboard_markup import InlineKeyboardMarkup
from ..objects.reply_keyboard_markup import ReplyKeyboardMarkup


@dataclass(init=True, repr=True, slots=True)
class SendMessage(TelegramBotsMethod[TelegramBotsApiResult[Message]]):
    # --- description here ---
    """Use this method to send text messages. On success, the sent [Message](https://core.telegram.org/bots/api/#message) is returned.
    
    More info at: https://core.telegram.org/bots/api/#sendmessage
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMethod.__init__(  # type: ignore
            obj, "sendMessage", [Message])
        return obj


    # --- arguments here ---
    chat_id: int | str = field(metadata={"ac_type": [int, str], "ac_name": "chat_id"})
    """Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
    """

    text: str = field(metadata={"ac_type": [str], "ac_name": "text"})
    """Text of the message to be sent, 1-4096 characters after entities parsing
    """

    parse_mode: Optional[str] = field(default=None, metadata={"ac_type": [str], "ac_name": "parse_mode"})
    """Mode for parsing entities in the message text. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details.
    """

    entities: Optional[list[MessageEntity]] = field(default=None, metadata={"ac_type": [MessageEntity], "ac_name": "entities"})
    """A JSON-serialized list of special entities that appear in message text, which can be specified instead of *parse\\_mode*
    """

    disable_web_page_preview: Optional[bool] = field(default=None, metadata={"ac_type": [bool], "ac_name": "disable_web_page_preview"})
    """Disables link previews for links in this message
    """

    disable_notification: Optional[bool] = field(default=None, metadata={"ac_type": [bool], "ac_name": "disable_notification"})
    """Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound.
    """

    protect_content: Optional[bool] = field(default=None, metadata={"ac_type": [bool], "ac_name": "protect_content"})
    """Protects the contents of the sent message from forwarding and saving
    """

    reply_to_message_id: Optional[int] = field(default=None, metadata={"ac_type": [int], "ac_name": "reply_to_message_id"})
    """If the message is a reply, ID of the original message
    """

    allow_sending_without_reply: Optional[bool] = field(default=None, metadata={"ac_type": [bool], "ac_name": "allow_sending_without_reply"})
    """Pass *True*, if the message should be sent even if the specified replied-to message is not found
    """

    reply_markup: Optional[InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply] = field(default=None, metadata={"ac_type": [InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply], "ac_name": "reply_markup"})
    """Additional interface options. A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots#inline-keyboards-and-on-the-fly-updating), [custom reply keyboard](https://core.telegram.org/bots#keyboards), instructions to remove reply keyboard or to force a reply from the user.
    """

