from dataclasses import dataclass, field

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject
from .menu_button import MenuButton


@dataclass(init=True, repr=True, slots=True)
class MenuButtonDefault(MenuButton):
    # --- description here ---
    """Describes that no specific value for the menu button was set.

    More info at: https://core.telegram.org/bots/api/#menubuttondefault
    """

    # --- properties here ---
    type: str = field(metadata={"ac_type": [str], "ac_name": "type"})
    """Type of the button, must be *default*
    """
