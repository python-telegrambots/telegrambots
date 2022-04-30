from dataclasses import dataclass, field
from typing import Literal

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject


@dataclass(init=True, repr=True, slots=True)
class MaskPosition(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object describes the position on faces where a mask should be placed by default.

    More info at: https://core.telegram.org/bots/api/#maskposition
    """

    # --- properties here ---
    point: Literal["forehead", "eyes", "mouth", "chin"] = field(
        metadata={"ac_type": [str], "ac_name": "point"}
    )
    """The part of the face relative to which the mask should be placed. One of “forehead”, “eyes”, “mouth”, or “chin”.
    """

    x_shift: float = field(metadata={"ac_type": [float], "ac_name": "x_shift"})
    """Shift by X-axis measured in widths of the mask scaled to the face size, from left to right. For example, choosing -1.0 will place mask just to the left of the default mask position.
    """

    y_shift: float = field(metadata={"ac_type": [float], "ac_name": "y_shift"})
    """Shift by Y-axis measured in heights of the mask scaled to the face size, from top to bottom. For example, 1.0 will place the mask just below the default mask position.
    """

    scale: float = field(metadata={"ac_type": [float], "ac_name": "scale"})
    """Mask scaling coefficient. For example, 2.0 means double size.
    """
