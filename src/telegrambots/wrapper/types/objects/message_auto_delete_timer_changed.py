from dataclasses import dataclass, field

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject


@dataclass(init=True, repr=True, slots=True)
class MessageAutoDeleteTimerChanged(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object represents a service message about a change in auto-delete timer settings.

    More info at: https://core.telegram.org/bots/api/#messageautodeletetimerchanged
    """

    # --- properties here ---
    message_auto_delete_time: int = field(
        metadata={"ac_type": [int], "ac_name": "message_auto_delete_time"}
    )
    """New auto-delete time for messages in the chat; in seconds
    """
