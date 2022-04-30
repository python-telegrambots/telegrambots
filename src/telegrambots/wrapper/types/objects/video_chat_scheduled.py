from dataclasses import dataclass, field

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject


@dataclass(init=True, repr=True, slots=True)
class VideoChatScheduled(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object represents a service message about a video chat scheduled in the chat.

    More info at: https://core.telegram.org/bots/api/#videochatscheduled
    """

    # --- properties here ---
    start_date: int = field(metadata={"ac_type": [int], "ac_name": "start_date"})
    """Point in time (Unix timestamp) when the video chat is supposed to be started by a chat administrator
    """
