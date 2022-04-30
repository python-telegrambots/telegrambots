from dataclasses import dataclass, field

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject
from .menu_button import MenuButton


@dataclass(init=True, repr=True, slots=True)
class MenuButtonCommands(MenuButton):
    # --- description here ---
    """Represents a menu button, which opens the bot's list of commands.

    More info at: https://core.telegram.org/bots/api/#menubuttoncommands
    """

    # --- properties here ---
    type: str = field(metadata={"ac_type": [str], "ac_name": "type"})
    """Type of the button, must be *commands*
    """
