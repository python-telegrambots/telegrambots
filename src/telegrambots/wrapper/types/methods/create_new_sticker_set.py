from dataclasses import dataclass, field
from typing import Any, Optional

from ..api_multipart_method import TelegramBotsMultipartMethod
from ..api_result import TelegramBotsApiResult
from ..objects.mask_position import MaskPosition
from ..objects.input_file import InputFile


@dataclass(init=True, repr=True, slots=True)
class CreateNewStickerSet(TelegramBotsMultipartMethod[TelegramBotsApiResult[bool]]):
    # --- description here ---
    """Use this method to create a new sticker set owned by a user. The bot will be able to edit the sticker set thus created. You **must** use exactly one of the fields *png\\_sticker*, *tgs\\_sticker*, or *webm\\_sticker*. Returns *True* on success.
    
    More info at: https://core.telegram.org/bots/api/#createnewstickerset
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMultipartMethod.__init__(  # type: ignore
            obj, "createNewStickerSet", [bool])
        return obj


    # --- arguments here ---
    user_id: int = field(metadata={"ac_type": [int], "ac_name": "user_id"})
    """User identifier of created sticker set owner
    """

    name: str = field(metadata={"ac_type": [str], "ac_name": "name"})
    """Short name of sticker set, to be used in `t.me/addstickers/` URLs (e.g., *animals*). Can contain only english letters, digits and underscores. Must begin with a letter, can't contain consecutive underscores and must end in `"_by_<bot_username>"`. `<bot_username>` is case insensitive. 1-64 characters.
    """

    title: str = field(metadata={"ac_type": [str], "ac_name": "title"})
    """Sticker set title, 1-64 characters
    """

    emojis: str = field(metadata={"ac_type": [str], "ac_name": "emojis"})
    """One or more emoji corresponding to the sticker
    """

    png_sticker: Optional[InputFile | str] = field(default=None, metadata={"ac_type": [InputFile, str], "ac_name": "png_sticker"})
    """**PNG** image with the sticker, must be up to 512 kilobytes in size, dimensions must not exceed 512px, and either width or height must be exactly 512px. Pass a *file\\_id* as a String to send a file that already exists on the Telegram servers, pass an HTTP URL as a String for Telegram to get a file from the Internet, or upload a new one using multipart/form-data. [More info on Sending Files »](https://core.telegram.org/bots/api/#sending-files)
    """

    tgs_sticker: Optional[InputFile] = field(default=None, metadata={"ac_type": [InputFile], "ac_name": "tgs_sticker"})
    """**TGS** animation with the sticker, uploaded using multipart/form-data. See [https://core.telegram.org/stickers#animated-sticker-requirements](https://core.telegram.org/stickers#animated-sticker-requirements) for technical requirements
    """

    webm_sticker: Optional[InputFile] = field(default=None, metadata={"ac_type": [InputFile], "ac_name": "webm_sticker"})
    """**WEBM** video with the sticker, uploaded using multipart/form-data. See [https://core.telegram.org/stickers#video-sticker-requirements](https://core.telegram.org/stickers#video-sticker-requirements) for technical requirements
    """

    contains_masks: Optional[bool] = field(default=None, metadata={"ac_type": [bool], "ac_name": "contains_masks"})
    """Pass *True*, if a set of mask stickers should be created
    """

    mask_position: Optional[MaskPosition] = field(default=None, metadata={"ac_type": [MaskPosition], "ac_name": "mask_position"})
    """A JSON-serialized object for position where the mask should be placed on faces
    """

