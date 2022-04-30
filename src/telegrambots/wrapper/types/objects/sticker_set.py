from dataclasses import dataclass, field
from typing import Optional

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject

from .sticker import Sticker
from .photo_size import PhotoSize


@dataclass(init=True, repr=True, slots=True)
class StickerSet(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object represents a sticker set.

    More info at: https://core.telegram.org/bots/api/#stickerset
    """

    # --- properties here ---
    name: str = field(metadata={"ac_type": [str], "ac_name": "name"})
    """Sticker set name
    """

    title: str = field(metadata={"ac_type": [str], "ac_name": "title"})
    """Sticker set title
    """

    is_animated: bool = field(metadata={"ac_type": [bool], "ac_name": "is_animated"})
    """*True*, if the sticker set contains [animated stickers](https://telegram.org/blog/animated-stickers)
    """

    is_video: bool = field(metadata={"ac_type": [bool], "ac_name": "is_video"})
    """*True*, if the sticker set contains [video stickers](https://telegram.org/blog/video-stickers-better-reactions)
    """

    contains_masks: bool = field(
        metadata={"ac_type": [bool], "ac_name": "contains_masks"}
    )
    """*True*, if the sticker set contains masks
    """

    stickers: list[Sticker] = field(
        metadata={"ac_type": [Sticker], "ac_name": "stickers"}
    )
    """List of all set stickers
    """

    thumb: Optional[PhotoSize] = field(
        default=None, metadata={"ac_type": [PhotoSize], "ac_name": "thumb"}
    )
    """*Optional*. Sticker set thumbnail in the .WEBP, .TGS, or .WEBM format
    """
