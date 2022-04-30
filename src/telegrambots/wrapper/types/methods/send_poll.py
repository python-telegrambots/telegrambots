from dataclasses import dataclass, field
from typing import Optional, Any, Literal

from ..api_method import TelegramBotsMethod
from ..api_result import TelegramBotsApiResult
from ..objects.force_reply import ForceReply
from ..objects.reply_keyboard_remove import ReplyKeyboardRemove
from ..objects.message import Message
from ..objects.message_entity import MessageEntity
from ..objects.inline_keyboard_markup import InlineKeyboardMarkup
from ..objects.reply_keyboard_markup import ReplyKeyboardMarkup


@dataclass(init=True, repr=True, slots=True)
class SendPoll(TelegramBotsMethod[TelegramBotsApiResult[Message]]):
    # --- description here ---
    """Use this method to send a native poll. On success, the sent [Message](https://core.telegram.org/bots/api/#message) is returned.
    
    More info at: https://core.telegram.org/bots/api/#sendpoll
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMethod.__init__(  # type: ignore
            obj, "sendPoll", [Message])
        return obj


    # --- arguments here ---
    chat_id: int | str = field(metadata={"ac_type": [int, str], "ac_name": "chat_id"})
    """Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
    """

    question: str = field(metadata={"ac_type": [str], "ac_name": "question"})
    """Poll question, 1-300 characters
    """

    options: list[str] = field(metadata={"ac_type": [str], "ac_name": "options"})
    """A JSON-serialized list of answer options, 2-10 strings 1-100 characters each
    """

    is_anonymous: bool = field(default=True, metadata={"ac_type": [bool], "ac_name": "is_anonymous"})
    """*True*, if the poll needs to be anonymous, defaults to *True*
    """

    type: Literal["quiz","regular"] = field(default='regular', metadata={"ac_type": [str], "ac_name": "type"})
    """Poll type, “quiz” or “regular”, defaults to “regular”
    """

    allows_multiple_answers: bool = field(default=False, metadata={"ac_type": [bool], "ac_name": "allows_multiple_answers"})
    """*True*, if the poll allows multiple answers, ignored for polls in quiz mode, defaults to *False*
    """

    correct_option_id: Optional[int] = field(default=None, metadata={"ac_type": [int], "ac_name": "correct_option_id"})
    """0-based identifier of the correct answer option, required for polls in quiz mode
    """

    explanation: Optional[str] = field(default=None, metadata={"ac_type": [str], "ac_name": "explanation"})
    """Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters with at most 2 line feeds after entities parsing
    """

    explanation_parse_mode: Optional[str] = field(default=None, metadata={"ac_type": [str], "ac_name": "explanation_parse_mode"})
    """Mode for parsing entities in the explanation. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details.
    """

    explanation_entities: Optional[list[MessageEntity]] = field(default=None, metadata={"ac_type": [MessageEntity], "ac_name": "explanation_entities"})
    """A JSON-serialized list of special entities that appear in the poll explanation, which can be specified instead of *parse\\_mode*
    """

    open_period: Optional[int] = field(default=None, metadata={"ac_type": [int], "ac_name": "open_period"})
    """Amount of time in seconds the poll will be active after creation, 5-600. Can't be used together with *close\\_date*.
    """

    close_date: Optional[int] = field(default=None, metadata={"ac_type": [int], "ac_name": "close_date"})
    """Point in time (Unix timestamp) when the poll will be automatically closed. Must be at least 5 and no more than 600 seconds in the future. Can't be used together with *open\\_period*.
    """

    is_closed: Optional[bool] = field(default=None, metadata={"ac_type": [bool], "ac_name": "is_closed"})
    """Pass *True*, if the poll needs to be immediately closed. This can be useful for poll preview.
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

