from dataclasses import dataclass, field
from typing import Any, Optional

from ..api_method import TelegramBotsMethod
from ..api_result import TelegramBotsApiResult
from ..objects.menu_button import MenuButton


@dataclass(init=True, repr=True, slots=True)
class SetChatMenuButton(TelegramBotsMethod[TelegramBotsApiResult[bool]]):
    # --- description here ---
    """Use this method to change the bot's menu button in a private chat, or the default menu button. Returns *True* on success.
    
    More info at: https://core.telegram.org/bots/api/#setchatmenubutton
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMethod.__init__(  # type: ignore
            obj, "setChatMenuButton", [bool])
        return obj


    # --- arguments here ---
    chat_id: Optional[int] = field(default=None, metadata={"ac_type": [int], "ac_name": "chat_id"})
    """Unique identifier for the target private chat. If not specified, default bot's menu button will be changed
    """

    menu_button: Optional[MenuButton] = field(default=None, metadata={"ac_type": [MenuButton], "ac_name": "menu_button"})
    """A JSON-serialized object for the new bot's menu button. Defaults to [MenuButtonDefault](https://core.telegram.org/bots/api/#menubuttondefault)
    """

