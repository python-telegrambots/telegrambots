from dataclasses import dataclass, field
from typing import Optional

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject

from .web_app_info import WebAppInfo
from .keyboard_button_poll_type import KeyboardButtonPollType


@dataclass(init=True, repr=True, slots=True)
class KeyboardButton(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object represents one button of the reply keyboard. For simple text buttons *String* can be used instead of this object to specify text of the button. Optional fields *web\\_app*, *request\\_contact*, *request\\_location*, and *request\\_poll* are mutually exclusive.

    More info at: https://core.telegram.org/bots/api/#keyboardbutton
    """

    # --- properties here ---
    text: str = field(metadata={"ac_type": [str], "ac_name": "text"})
    """Text of the button. If none of the optional fields are used, it will be sent as a message when the button is pressed
    """

    request_contact: Optional[bool] = field(
        default=None, metadata={"ac_type": [bool], "ac_name": "request_contact"}
    )
    """*Optional*. If *True*, the user's phone number will be sent as a contact when the button is pressed. Available in private chats only.
    """

    request_location: Optional[bool] = field(
        default=None, metadata={"ac_type": [bool], "ac_name": "request_location"}
    )
    """*Optional*. If *True*, the user's current location will be sent when the button is pressed. Available in private chats only.
    """

    request_poll: Optional[KeyboardButtonPollType] = field(
        default=None,
        metadata={"ac_type": [KeyboardButtonPollType], "ac_name": "request_poll"},
    )
    """*Optional*. If specified, the user will be asked to create a poll and send it to the bot when the button is pressed. Available in private chats only.
    """

    web_app: Optional[WebAppInfo] = field(
        default=None, metadata={"ac_type": [WebAppInfo], "ac_name": "web_app"}
    )
    """*Optional*. If specified, the described [Web App](https://core.telegram.org/bots/webapps) will be launched when the button is pressed. The Web App will be able to send a “web\\_app\\_data” service message. Available in private chats only.
    """
