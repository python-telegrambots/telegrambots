from dataclasses import dataclass, field

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject


@dataclass(init=True, repr=True, slots=True)
class MessageId(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object represents a unique message identifier.

    More info at: https://core.telegram.org/bots/api/#messageid
    """

    # --- properties here ---
    message_id: int = field(metadata={"ac_type": [int], "ac_name": "message_id"})
    """Unique message identifier
    """
