from dataclasses import dataclass, field

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject

from .user import User


@dataclass(init=True, repr=True, slots=True)
class ProximityAlertTriggered(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object represents the content of a service message, sent whenever a user in the chat triggers a proximity alert set by another user.

    More info at: https://core.telegram.org/bots/api/#proximityalerttriggered
    """

    # --- properties here ---
    traveler: User = field(metadata={"ac_type": [User], "ac_name": "traveler"})
    """User that triggered the alert
    """

    watcher: User = field(metadata={"ac_type": [User], "ac_name": "watcher"})
    """User that set the alert
    """

    distance: int = field(metadata={"ac_type": [int], "ac_name": "distance"})
    """The distance between the users
    """
