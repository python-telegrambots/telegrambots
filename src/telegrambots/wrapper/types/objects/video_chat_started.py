import dataclasses

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject


@dataclasses.dataclass(init=True, repr=True, slots=True)
class VideoChatStarted(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object represents a service message about a video chat started in the chat. Currently holds no information.

    More info at: https://core.telegram.org/bots/api/#videochatstarted
    """
