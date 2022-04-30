import abc
import dataclasses

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject


@dataclasses.dataclass(init=True, repr=True, slots=True)
class MenuButton(abc.ABC, TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object describes the bot's menu button in a private chat. It should be one of

    * [MenuButtonCommands](https://core.telegram.org/bots/api/#menubuttoncommands)
    * [MenuButtonWebApp](https://core.telegram.org/bots/api/#menubuttonwebapp)
    * [MenuButtonDefault](https://core.telegram.org/bots/api/#menubuttondefault)

    More info at: https://core.telegram.org/bots/api/#menubutton
    """
