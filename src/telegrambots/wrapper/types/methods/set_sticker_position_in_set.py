from dataclasses import dataclass, field
from typing import Any

from ..api_method import TelegramBotsMethod
from ..api_result import TelegramBotsApiResult



@dataclass(init=True, repr=True, slots=True)
class SetStickerPositionInSet(TelegramBotsMethod[TelegramBotsApiResult[bool]]):
    # --- description here ---
    """Use this method to move a sticker in a set created by the bot to a specific position. Returns *True* on success.
    
    More info at: https://core.telegram.org/bots/api/#setstickerpositioninset
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMethod.__init__(  # type: ignore
            obj, "setStickerPositionInSet", [bool])
        return obj


    # --- arguments here ---
    sticker: str = field(metadata={"ac_type": [str], "ac_name": "sticker"})
    """File identifier of the sticker
    """

    position: int = field(metadata={"ac_type": [int], "ac_name": "position"})
    """New sticker position in the set, zero-based
    """

