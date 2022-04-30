from dataclasses import dataclass, field
from typing import Any, Optional

from ..api_multipart_method import TelegramBotsMultipartMethod
from ..api_result import TelegramBotsApiResult
from ..objects.input_file import InputFile


@dataclass(init=True, repr=True, slots=True)
class SetStickerSetThumb(TelegramBotsMultipartMethod[TelegramBotsApiResult[bool]]):
    # --- description here ---
    """Use this method to set the thumbnail of a sticker set. Animated thumbnails can be set for animated sticker sets only. Video thumbnails can be set only for video sticker sets only. Returns *True* on success.
    
    More info at: https://core.telegram.org/bots/api/#setstickersetthumb
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMultipartMethod.__init__(  # type: ignore
            obj, "setStickerSetThumb", [bool])
        return obj


    # --- arguments here ---
    name: str = field(metadata={"ac_type": [str], "ac_name": "name"})
    """Sticker set name
    """

    user_id: int = field(metadata={"ac_type": [int], "ac_name": "user_id"})
    """User identifier of the sticker set owner
    """

    thumb: Optional[InputFile | str] = field(default=None, metadata={"ac_type": [InputFile, str], "ac_name": "thumb"})
    """A **PNG** image with the thumbnail, must be up to 128 kilobytes in size and have width and height exactly 100px, or a **TGS** animation with the thumbnail up to 32 kilobytes in size; see [https://core.telegram.org/stickers#animated-sticker-requirements](https://core.telegram.org/stickers#animated-sticker-requirements) for animated sticker technical requirements, or a **WEBM** video with the thumbnail up to 32 kilobytes in size; see [https://core.telegram.org/stickers#video-sticker-requirements](https://core.telegram.org/stickers#video-sticker-requirements) for video sticker technical requirements. Pass a *file\\_id* as a String to send a file that already exists on the Telegram servers, pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. [More info on Sending Files »](https://core.telegram.org/bots/api/#sending-files). Animated sticker set thumbnails can't be uploaded via HTTP URL.
    """

