from dataclasses import dataclass, field
from typing import Optional

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject


@dataclass(init=True, repr=True, slots=True)
class ResponseParameters(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """Contains information about why a request was unsuccessful.

    More info at: https://core.telegram.org/bots/api/#responseparameters
    """

    # --- properties here ---
    migrate_to_chat_id: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "migrate_to_chat_id"}
    )
    """*Optional*. The group has been migrated to a supergroup with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
    """

    retry_after: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "retry_after"}
    )
    """*Optional*. In case of exceeding flood control, the number of seconds left to wait before the request can be repeated
    """
