from dataclasses import dataclass, field

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject

from .location import Location


@dataclass(init=True, repr=True, slots=True)
class ChatLocation(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """Represents a location to which a chat is connected.

    More info at: https://core.telegram.org/bots/api/#chatlocation
    """

    # --- properties here ---
    location: Location = field(metadata={"ac_type": [Location], "ac_name": "location"})
    """The location to which the supergroup is connected. Can't be a live location.
    """

    address: str = field(metadata={"ac_type": [str], "ac_name": "address"})
    """Location address; 1-64 characters, as defined by the chat owner
    """
