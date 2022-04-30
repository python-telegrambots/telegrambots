from dataclasses import dataclass, field

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject


@dataclass(init=True, repr=True, slots=True)
class WebAppInfo(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """Contains information about a [Web App](https://core.telegram.org/bots/webapps).

    More info at: https://core.telegram.org/bots/api/#webappinfo
    """

    # --- properties here ---
    url: str = field(metadata={"ac_type": [str], "ac_name": "url"})
    """An HTTPS URL of a Web App to be opened with additional data as specified in [Initializing Web Apps](https://core.telegram.org/bots/webapps#initializing-web-apps)
    """
