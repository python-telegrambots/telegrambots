from dataclasses import dataclass, field

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject
from .menu_button import MenuButton
from .web_app_info import WebAppInfo


@dataclass(init=True, repr=True, slots=True)
class MenuButtonWebApp(MenuButton):
    # --- description here ---
    """Represents a menu button, which launches a [Web App](https://core.telegram.org/bots/webapps).

    More info at: https://core.telegram.org/bots/api/#menubuttonwebapp
    """

    # --- properties here ---
    type: str = field(metadata={"ac_type": [str], "ac_name": "type"})
    """Type of the button, must be *web\\_app*
    """

    text: str = field(metadata={"ac_type": [str], "ac_name": "text"})
    """Text on the button
    """

    web_app: WebAppInfo = field(
        metadata={"ac_type": [WebAppInfo], "ac_name": "web_app"}
    )
    """Description of the Web App that will be launched when the user presses the button. The Web App will be able to send an arbitrary message on behalf of the user using the method [answerWebAppQuery](https://core.telegram.org/bots/api/#answerwebappquery).
    """
