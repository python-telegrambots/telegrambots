from dataclasses import dataclass, field

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject


@dataclass(init=True, repr=True, slots=True)
class WebAppData(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """Contains data sent from a [Web App](https://core.telegram.org/bots/webapps) to the bot.

    More info at: https://core.telegram.org/bots/api/#webappdata
    """

    # --- properties here ---
    data: str = field(metadata={"ac_type": [str], "ac_name": "data"})
    """The data. Be aware that a bad client can send arbitrary data in this field.
    """

    button_text: str = field(metadata={"ac_type": [str], "ac_name": "button_text"})
    """Text of the *web\\_app* keyboard button, from which the Web App was opened. Be aware that a bad client can send arbitrary data in this field.
    """
