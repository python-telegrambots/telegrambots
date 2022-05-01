from dataclasses import dataclass, field
from typing import Any

from ..api_method import TelegramBotsMethodNoOutput


@dataclass(init=True, repr=True, slots=True)
class DeleteStickerFromSet(TelegramBotsMethodNoOutput):
    # --- description here ---
    """Use this method to delete a sticker from a set created by the bot. Returns *True* on success.

    More info at: https://core.telegram.org/bots/api/#deletestickerfromset
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMethodNoOutput.__init__(obj, "deleteStickerFromSet")  # type: ignore
        return obj

    # --- arguments here ---
    sticker: str = field(metadata={"ac_type": [str], "ac_name": "sticker"})
    """File identifier of the sticker
    """
