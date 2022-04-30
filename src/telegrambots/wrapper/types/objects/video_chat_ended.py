from dataclasses import dataclass, field

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject


@dataclass(init=True, repr=True, slots=True)
class VideoChatEnded(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object represents a service message about a video chat ended in the chat.

    More info at: https://core.telegram.org/bots/api/#videochatended
    """

    # --- properties here ---
    duration: int = field(metadata={"ac_type": [int], "ac_name": "duration"})
    """Video chat duration in seconds
    """
