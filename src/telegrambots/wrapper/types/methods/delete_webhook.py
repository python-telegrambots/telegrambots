from dataclasses import dataclass, field
from typing import Any, Optional

from ..api_method import TelegramBotsMethod
from ..api_result import TelegramBotsApiResult



@dataclass(init=True, repr=True, slots=True)
class DeleteWebhook(TelegramBotsMethod[TelegramBotsApiResult[bool]]):
    # --- description here ---
    """Use this method to remove webhook integration if you decide to switch back to [getUpdates](https://core.telegram.org/bots/api/#getupdates). Returns *True* on success.
    
    More info at: https://core.telegram.org/bots/api/#deletewebhook
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMethod.__init__(  # type: ignore
            obj, "deleteWebhook", [bool])
        return obj


    # --- arguments here ---
    drop_pending_updates: Optional[bool] = field(default=None, metadata={"ac_type": [bool], "ac_name": "drop_pending_updates"})
    """Pass *True* to drop all pending updates
    """

