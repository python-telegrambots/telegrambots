from dataclasses import dataclass, field
from typing import Any, Optional

from ..api_method import TelegramBotsMethod
from ..api_result import TelegramBotsApiResult
from ..objects.chat_administrator_rights import ChatAdministratorRights


@dataclass(init=True, repr=True, slots=True)
class GetMyDefaultAdministratorRights(TelegramBotsMethod[TelegramBotsApiResult[ChatAdministratorRights]]):
    # --- description here ---
    """Use this method to get the current default administrator rights of the bot. Returns [ChatAdministratorRights](https://core.telegram.org/bots/api/#chatadministratorrights) on success.
    
    More info at: https://core.telegram.org/bots/api/#getmydefaultadministratorrights
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMethod.__init__(  # type: ignore
            obj, "getMyDefaultAdministratorRights", [ChatAdministratorRights])
        return obj


    # --- arguments here ---
    for_channels: Optional[bool] = field(default=None, metadata={"ac_type": [bool], "ac_name": "for_channels"})
    """Pass *True* to get default administrator rights of the bot in channels. Otherwise, default administrator rights of the bot for groups and supergroups will be returned.
    """

