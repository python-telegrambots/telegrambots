from dataclasses import dataclass, field
from typing import Any

from ..api_method import TelegramBotsMethod
from ..api_result import TelegramBotsApiResult
from ..objects.sticker_set import StickerSet


@dataclass(init=True, repr=True, slots=True)
class GetStickerSet(TelegramBotsMethod[TelegramBotsApiResult[StickerSet]]):
    # --- description here ---
    """Use this method to get a sticker set. On success, a [StickerSet](https://core.telegram.org/bots/api/#stickerset) object is returned.
    
    More info at: https://core.telegram.org/bots/api/#getstickerset
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMethod.__init__(  # type: ignore
            obj, "getStickerSet", [StickerSet])
        return obj


    # --- arguments here ---
    name: str = field(metadata={"ac_type": [str], "ac_name": "name"})
    """Name of the sticker set
    """

