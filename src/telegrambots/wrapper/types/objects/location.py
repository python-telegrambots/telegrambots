from dataclasses import dataclass, field
from typing import Optional

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject


@dataclass(init=True, repr=True, slots=True)
class Location(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object represents a point on the map.

    More info at: https://core.telegram.org/bots/api/#location
    """

    # --- properties here ---
    longitude: float = field(metadata={"ac_type": [float], "ac_name": "longitude"})
    """Longitude as defined by sender
    """

    latitude: float = field(metadata={"ac_type": [float], "ac_name": "latitude"})
    """Latitude as defined by sender
    """

    horizontal_accuracy: Optional[float] = field(
        default=None, metadata={"ac_type": [float], "ac_name": "horizontal_accuracy"}
    )
    """*Optional*. The radius of uncertainty for the location, measured in meters; 0-1500
    """

    live_period: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "live_period"}
    )
    """*Optional*. Time relative to the message sending date, during which the location can be updated; in seconds. For active live locations only.
    """

    heading: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "heading"}
    )
    """*Optional*. The direction in which user is moving, in degrees; 1-360. For active live locations only.
    """

    proximity_alert_radius: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "proximity_alert_radius"}
    )
    """*Optional*. Maximum distance for proximity alerts about approaching another chat member, in meters. For sent live locations only.
    """
