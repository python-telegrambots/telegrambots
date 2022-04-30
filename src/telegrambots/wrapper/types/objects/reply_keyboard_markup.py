from dataclasses import dataclass, field
from typing import Optional

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject

from .keyboard_button import KeyboardButton


@dataclass(init=True, repr=True, slots=True)
class ReplyKeyboardMarkup(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object represents a [custom keyboard](https://core.telegram.org/bots#keyboards) with reply options (see [Introduction to bots](https://core.telegram.org/bots#keyboards) for details and examples).

    More info at: https://core.telegram.org/bots/api/#replykeyboardmarkup
    """

    # --- properties here ---
    keyboard: list[list[KeyboardButton]] = field(
        metadata={"ac_type": [KeyboardButton], "ac_name": "keyboard"}
    )
    """Array of button rows, each represented by an Array of [KeyboardButton](https://core.telegram.org/bots/api/#keyboardbutton) objects
    """

    resize_keyboard: bool = field(
        default=False, metadata={"ac_type": [bool], "ac_name": "resize_keyboard"}
    )
    """*Optional*. Requests clients to resize the keyboard vertically for optimal fit (e.g., make the keyboard smaller if there are just two rows of buttons). Defaults to *false*, in which case the custom keyboard is always of the same height as the app's standard keyboard.
    """

    one_time_keyboard: bool = field(
        default=False, metadata={"ac_type": [bool], "ac_name": "one_time_keyboard"}
    )
    """*Optional*. Requests clients to hide the keyboard as soon as it's been used. The keyboard will still be available, but clients will automatically display the usual letter-keyboard in the chat – the user can press a special button in the input field to see the custom keyboard again. Defaults to *false*.
    """

    input_field_placeholder: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "input_field_placeholder"}
    )
    """*Optional*. The placeholder to be shown in the input field when the keyboard is active; 1-64 characters
    """

    selective: Optional[bool] = field(
        default=None, metadata={"ac_type": [bool], "ac_name": "selective"}
    )
    """*Optional*. Use this parameter if you want to show the keyboard to specific users only. Targets: 1) users that are @mentioned in the *text* of the [Message](https://core.telegram.org/bots/api/#message) object; 2) if the bot's message is a reply (has *reply\\_to\\_message\\_id*), sender of the original message.  

*Example:* A user requests to change the bot's language, bot replies to the request with a keyboard to select the new language. Other users in the group don't see the keyboard.
    """
