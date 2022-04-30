from dataclasses import dataclass, field
from typing import Any, Optional

from ..api_method import TelegramBotsMethod
from ..api_result import TelegramBotsApiResult
from ..objects.chat_administrator_rights import ChatAdministratorRights


@dataclass(init=True, repr=True, slots=True)
class SetMyDefaultAdministratorRights(TelegramBotsMethod[TelegramBotsApiResult[bool]]):
    # --- description here ---
    """Use this method to change the default administrator rights requested by the bot when it's added as an administrator to groups or channels. These rights will be suggested to users, but they are are free to modify the list before adding the bot. Returns *True* on success.
    
    More info at: https://core.telegram.org/bots/api/#setmydefaultadministratorrights
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMethod.__init__(  # type: ignore
            obj, "setMyDefaultAdministratorRights", [bool])
        return obj


    # --- arguments here ---
    rights: Optional[ChatAdministratorRights] = field(default=None, metadata={"ac_type": [ChatAdministratorRights], "ac_name": "rights"})
    """A JSON-serialized object describing new default administrator rights. If not specified, the default administrator rights will be cleared.
    """

    for_channels: Optional[bool] = field(default=None, metadata={"ac_type": [bool], "ac_name": "for_channels"})
    """Pass *True* to change the default administrator rights of the bot in channels. Otherwise, the default administrator rights of the bot for groups and supergroups will be changed.
    """

