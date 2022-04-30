from dataclasses import dataclass, field
from typing import Optional

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject


@dataclass(init=True, repr=True, slots=True)
class KeyboardButtonPollType(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object represents type of a poll, which is allowed to be created and sent when the corresponding button is pressed.

    More info at: https://core.telegram.org/bots/api/#keyboardbuttonpolltype
    """

    # --- properties here ---
    type: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "type"}
    )
    """*Optional*. If *quiz* is passed, the user will be allowed to create only polls in the quiz mode. If *regular* is passed, only regular polls will be allowed. Otherwise, the user will be allowed to create a poll of any type.
    """
