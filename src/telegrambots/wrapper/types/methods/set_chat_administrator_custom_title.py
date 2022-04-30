from dataclasses import dataclass, field
from typing import Any

from ..api_method import TelegramBotsMethod
from ..api_result import TelegramBotsApiResult



@dataclass(init=True, repr=True, slots=True)
class SetChatAdministratorCustomTitle(TelegramBotsMethod[TelegramBotsApiResult[bool]]):
    # --- description here ---
    """Use this method to set a custom title for an administrator in a supergroup promoted by the bot. Returns *True* on success.
    
    More info at: https://core.telegram.org/bots/api/#setchatadministratorcustomtitle
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMethod.__init__(  # type: ignore
            obj, "setChatAdministratorCustomTitle", [bool])
        return obj


    # --- arguments here ---
    chat_id: int | str = field(metadata={"ac_type": [int, str], "ac_name": "chat_id"})
    """Unique identifier for the target chat or username of the target supergroup (in the format `@supergroupusername`)
    """

    user_id: int = field(metadata={"ac_type": [int], "ac_name": "user_id"})
    """Unique identifier of the target user
    """

    custom_title: str = field(metadata={"ac_type": [str], "ac_name": "custom_title"})
    """New custom title for the administrator; 0-16 characters, emoji are not allowed
    """

