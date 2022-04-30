from dataclasses import dataclass, field

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject


@dataclass(init=True, repr=True, slots=True)
class Dice(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object represents an animated emoji that displays a random value.

    More info at: https://core.telegram.org/bots/api/#dice
    """

    # --- properties here ---
    emoji: str = field(metadata={"ac_type": [str], "ac_name": "emoji"})
    """Emoji on which the dice throw animation is based
    """

    value: int = field(metadata={"ac_type": [int], "ac_name": "value"})
    """Value of the dice, 1-6 for “🎲”, “🎯” and “🎳” base emoji, 1-5 for “🏀” and “⚽” base emoji, 1-64 for “🎰” base emoji
    """
