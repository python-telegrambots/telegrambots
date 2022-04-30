import dataclasses

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject


@dataclasses.dataclass(init=True, repr=True, slots=True)
class CallbackGame(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """A placeholder, currently holds no information. Use [BotFather](https://t.me/botfather) to set up your game.

    More info at: https://core.telegram.org/bots/api/#callbackgame
    """
