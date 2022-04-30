from dataclasses import dataclass, field
from typing import Any

from ..api_multipart_method import TelegramBotsMultipartMethod
from ..api_result import TelegramBotsApiResult
from ..objects.file import File
from ..objects.input_file import InputFile


@dataclass(init=True, repr=True, slots=True)
class UploadStickerFile(TelegramBotsMultipartMethod[TelegramBotsApiResult[File]]):
    # --- description here ---
    """Use this method to upload a .PNG file with a sticker for later use in *createNewStickerSet* and *addStickerToSet* methods (can be used multiple times). Returns the uploaded [File](https://core.telegram.org/bots/api/#file) on success.
    
    More info at: https://core.telegram.org/bots/api/#uploadstickerfile
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMultipartMethod.__init__(  # type: ignore
            obj, "uploadStickerFile", [File])
        return obj


    # --- arguments here ---
    user_id: int = field(metadata={"ac_type": [int], "ac_name": "user_id"})
    """User identifier of sticker file owner
    """

    png_sticker: InputFile = field(metadata={"ac_type": [InputFile], "ac_name": "png_sticker"})
    """**PNG** image with the sticker, must be up to 512 kilobytes in size, dimensions must not exceed 512px, and either width or height must be exactly 512px. [More info on Sending Files »](https://core.telegram.org/bots/api/#sending-files)
    """

