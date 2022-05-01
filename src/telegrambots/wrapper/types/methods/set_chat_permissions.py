from dataclasses import dataclass, field
from typing import Any

from ..api_method import TelegramBotsMethodNoOutput
from ..objects.chat_permissions import ChatPermissions


@dataclass(init=True, repr=True, slots=True)
class SetChatPermissions(TelegramBotsMethodNoOutput):
    # --- description here ---
    """Use this method to set default chat permissions for all members. The bot must be an administrator in the group or a supergroup for this to work and must have the *can\\_restrict\\_members* administrator rights. Returns *True* on success.

    More info at: https://core.telegram.org/bots/api/#setchatpermissions
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMethod.__init__(obj, "setChatPermissions", [bool])  # type: ignore
        return obj

    # --- arguments here ---
    chat_id: int | str = field(metadata={"ac_type": [int, str], "ac_name": "chat_id"})
    """Unique identifier for the target chat or username of the target supergroup (in the format `@supergroupusername`)
    """

    permissions: ChatPermissions = field(
        metadata={"ac_type": [ChatPermissions], "ac_name": "permissions"}
    )
    """A JSON-serialized object for new default chat permissions
    """
