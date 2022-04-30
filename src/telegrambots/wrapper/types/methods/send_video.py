from dataclasses import dataclass, field
from typing import Any, Optional

from ..api_multipart_method import TelegramBotsMultipartMethod
from ..api_result import TelegramBotsApiResult
from ..objects.force_reply import ForceReply
from ..objects.reply_keyboard_remove import ReplyKeyboardRemove
from ..objects.message import Message
from ..objects.input_file import InputFile
from ..objects.message_entity import MessageEntity
from ..objects.inline_keyboard_markup import InlineKeyboardMarkup
from ..objects.reply_keyboard_markup import ReplyKeyboardMarkup


@dataclass(init=True, repr=True, slots=True)
class SendVideo(TelegramBotsMultipartMethod[TelegramBotsApiResult[Message]]):
    # --- description here ---
    """Use this method to send video files, Telegram clients support mp4 videos (other formats may be sent as [Document](https://core.telegram.org/bots/api/#document)). On success, the sent [Message](https://core.telegram.org/bots/api/#message) is returned. Bots can currently send video files of up to 50 MB in size, this limit may be changed in the future.
    
    More info at: https://core.telegram.org/bots/api/#sendvideo
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMultipartMethod.__init__(  # type: ignore
            obj, "sendVideo", [Message])
        return obj


    # --- arguments here ---
    chat_id: int | str = field(metadata={"ac_type": [int, str], "ac_name": "chat_id"})
    """Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
    """

    video: InputFile | str = field(metadata={"ac_type": [InputFile, str], "ac_name": "video"})
    """Video to send. Pass a file\\_id as String to send a video that exists on the Telegram servers (recommended), pass an HTTP URL as a String for Telegram to get a video from the Internet, or upload a new video using multipart/form-data. [More info on Sending Files »](https://core.telegram.org/bots/api/#sending-files)
    """

    duration: Optional[int] = field(default=None, metadata={"ac_type": [int], "ac_name": "duration"})
    """Duration of sent video in seconds
    """

    width: Optional[int] = field(default=None, metadata={"ac_type": [int], "ac_name": "width"})
    """Video width
    """

    height: Optional[int] = field(default=None, metadata={"ac_type": [int], "ac_name": "height"})
    """Video height
    """

    thumb: Optional[InputFile | str] = field(default=None, metadata={"ac_type": [InputFile, str], "ac_name": "thumb"})
    """Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file\\_attach\\_name>” if the thumbnail was uploaded using multipart/form-data under <file\\_attach\\_name>. [More info on Sending Files »](https://core.telegram.org/bots/api/#sending-files)
    """

    caption: Optional[str] = field(default=None, metadata={"ac_type": [str], "ac_name": "caption"})
    """Video caption (may also be used when resending videos by *file\\_id*), 0-1024 characters after entities parsing
    """

    parse_mode: Optional[str] = field(default=None, metadata={"ac_type": [str], "ac_name": "parse_mode"})
    """Mode for parsing entities in the video caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details.
    """

    caption_entities: Optional[list[MessageEntity]] = field(default=None, metadata={"ac_type": [MessageEntity], "ac_name": "caption_entities"})
    """A JSON-serialized list of special entities that appear in the caption, which can be specified instead of *parse\\_mode*
    """

    supports_streaming: Optional[bool] = field(default=None, metadata={"ac_type": [bool], "ac_name": "supports_streaming"})
    """Pass *True*, if the uploaded video is suitable for streaming
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

