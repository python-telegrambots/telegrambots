from dataclasses import dataclass, field
from typing import Any, Optional

from ..api_multipart_method import TelegramBotsMultipartMethod
from ..api_result import TelegramBotsApiResult
from ..objects.message import Message
from ..objects.input_media_video import InputMediaVideo
from ..objects.input_media_document import InputMediaDocument
from ..objects.input_media_audio import InputMediaAudio
from ..objects.input_media_photo import InputMediaPhoto


@dataclass(init=True, repr=True, slots=True)
class SendMediaGroup(TelegramBotsMultipartMethod[TelegramBotsApiResult[list[Message]]]):
    # --- description here ---
    """Use this method to send a group of photos, videos, documents or audios as an album. Documents and audio files can be only grouped in an album with messages of the same type. On success, an array of [Messages](https://core.telegram.org/bots/api/#message) that were sent is returned.
    
    More info at: https://core.telegram.org/bots/api/#sendmediagroup
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMultipartMethod.__init__(  # type: ignore
            obj, "sendMediaGroup", [Message])
        return obj


    # --- arguments here ---
    chat_id: int | str = field(metadata={"ac_type": [int, str], "ac_name": "chat_id"})
    """Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
    """

    media: list[InputMediaAudio | InputMediaDocument | InputMediaPhoto | InputMediaVideo] = field(metadata={"ac_type": [InputMediaAudio, InputMediaDocument, InputMediaPhoto, InputMediaVideo], "ac_name": "media"})
    """A JSON-serialized array describing messages to be sent, must include 2-10 items
    """

    disable_notification: Optional[bool] = field(default=None, metadata={"ac_type": [bool], "ac_name": "disable_notification"})
    """Sends messages [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound.
    """

    protect_content: Optional[bool] = field(default=None, metadata={"ac_type": [bool], "ac_name": "protect_content"})
    """Protects the contents of the sent messages from forwarding and saving
    """

    reply_to_message_id: Optional[int] = field(default=None, metadata={"ac_type": [int], "ac_name": "reply_to_message_id"})
    """If the messages are a reply, ID of the original message
    """

    allow_sending_without_reply: Optional[bool] = field(default=None, metadata={"ac_type": [bool], "ac_name": "allow_sending_without_reply"})
    """Pass *True*, if the message should be sent even if the specified replied-to message is not found
    """

