from dataclasses import dataclass, field
from typing import Optional

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject

from .photo_size import PhotoSize
from .mask_position import MaskPosition


@dataclass(init=True, repr=True, slots=True)
class Sticker(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object represents a sticker.

    More info at: https://core.telegram.org/bots/api/#sticker
    """

    # --- properties here ---
    file_id: str = field(metadata={"ac_type": [str], "ac_name": "file_id"})
    """Identifier for this file, which can be used to download or reuse the file
    """

    file_unique_id: str = field(
        metadata={"ac_type": [str], "ac_name": "file_unique_id"}
    )
    """Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    """

    width: int = field(metadata={"ac_type": [int], "ac_name": "width"})
    """Sticker width
    """

    height: int = field(metadata={"ac_type": [int], "ac_name": "height"})
    """Sticker height
    """

    is_animated: bool = field(metadata={"ac_type": [bool], "ac_name": "is_animated"})
    """*True*, if the sticker is [animated](https://telegram.org/blog/animated-stickers)
    """

    is_video: bool = field(metadata={"ac_type": [bool], "ac_name": "is_video"})
    """*True*, if the sticker is a [video sticker](https://telegram.org/blog/video-stickers-better-reactions)
    """

    thumb: Optional[PhotoSize] = field(
        default=None, metadata={"ac_type": [PhotoSize], "ac_name": "thumb"}
    )
    """*Optional*. Sticker thumbnail in the .WEBP or .JPG format
    """

    emoji: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "emoji"}
    )
    """*Optional*. Emoji associated with the sticker
    """

    set_name: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "set_name"}
    )
    """*Optional*. Name of the sticker set to which the sticker belongs
    """

    mask_position: Optional[MaskPosition] = field(
        default=None, metadata={"ac_type": [MaskPosition], "ac_name": "mask_position"}
    )
    """*Optional*. For mask stickers, the position where the mask should be placed
    """

    file_size: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "file_size"}
    )
    """*Optional*. File size in bytes
    """
