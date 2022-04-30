from dataclasses import dataclass, field
from typing import Any, Optional

from ..api_method import TelegramBotsMethod
from ..api_result import TelegramBotsApiResult
from ..objects.update import Update


@dataclass(init=True, repr=True, slots=True)
class GetUpdates(TelegramBotsMethod[TelegramBotsApiResult[list[Update]]]):
    # --- description here ---
    """Use this method to receive incoming updates using long polling ([wiki](https://en.wikipedia.org/wiki/Push_technology#Long_polling)). An Array of [Update](https://core.telegram.org/bots/api/#update) objects is returned.
    
    More info at: https://core.telegram.org/bots/api/#getupdates
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMethod.__init__(  # type: ignore
            obj, "getUpdates", [Update])
        return obj


    # --- arguments here ---
    offset: Optional[int] = field(default=None, metadata={"ac_type": [int], "ac_name": "offset"})
    """Identifier of the first update to be returned. Must be greater by one than the highest among the identifiers of previously received updates. By default, updates starting with the earliest unconfirmed update are returned. An update is considered confirmed as soon as [getUpdates](https://core.telegram.org/bots/api/#getupdates) is called with an *offset* higher than its *update\\_id*. The negative offset can be specified to retrieve updates starting from *-offset* update from the end of the updates queue. All previous updates will forgotten.
    """

    limit: int = field(default=100, metadata={"ac_type": [int], "ac_name": "limit"})
    """Limits the number of updates to be retrieved. Values between 1-100 are accepted. Defaults to 100.
    """

    timeout: int = field(default=0, metadata={"ac_type": [int], "ac_name": "timeout"})
    """Timeout in seconds for long polling. Defaults to 0, i.e. usual short polling. Should be positive, short polling should be used for testing purposes only.
    """

    allowed_updates: Optional[list[str]] = field(default=None, metadata={"ac_type": [str], "ac_name": "allowed_updates"})
    """A JSON-serialized list of the update types you want your bot to receive. For example, specify [“message”, “edited\\_channel\\_post”, “callback\\_query”] to only receive updates of these types. See [Update](https://core.telegram.org/bots/api/#update) for a complete list of available update types. Specify an empty list to receive all update types except *chat\\_member* (default). If not specified, the previous setting will be used.  

Please note that this parameter doesn't affect updates created before the call to the getUpdates, so unwanted updates may be received for a short period of time.
    """

