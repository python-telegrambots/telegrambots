from dataclasses import dataclass, field
from typing import Any, Optional

from ..api_method import TelegramBotsMethod
from ..api_result import TelegramBotsApiResult
from ..objects.chat_permissions import ChatPermissions


@dataclass(init=True, repr=True, slots=True)
class RestrictChatMember(TelegramBotsMethod[TelegramBotsApiResult[bool]]):
    # --- description here ---
    """Use this method to restrict a user in a supergroup. The bot must be an administrator in the supergroup for this to work and must have the appropriate administrator rights. Pass *True* for all permissions to lift restrictions from a user. Returns *True* on success.
    
    More info at: https://core.telegram.org/bots/api/#restrictchatmember
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMethod.__init__(  # type: ignore
            obj, "restrictChatMember", [bool])
        return obj


    # --- arguments here ---
    chat_id: int | str = field(metadata={"ac_type": [int, str], "ac_name": "chat_id"})
    """Unique identifier for the target chat or username of the target supergroup (in the format `@supergroupusername`)
    """

    user_id: int = field(metadata={"ac_type": [int], "ac_name": "user_id"})
    """Unique identifier of the target user
    """

    permissions: ChatPermissions = field(metadata={"ac_type": [ChatPermissions], "ac_name": "permissions"})
    """A JSON-serialized object for new user permissions
    """

    until_date: Optional[int] = field(default=None, metadata={"ac_type": [int], "ac_name": "until_date"})
    """Date when restrictions will be lifted for the user, unix time. If user is restricted for more than 366 days or less than 30 seconds from the current time, they are considered to be restricted forever
    """

