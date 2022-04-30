from dataclasses import dataclass, field
from typing import Optional

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject
from .input_message_content import InputMessageContent


@dataclass(init=True, repr=True, slots=True)
class InputLocationMessageContent(InputMessageContent):
    # --- description here ---
    """Represents the [content](https://core.telegram.org/bots/api/#inputmessagecontent) of a location message to be sent as the result of an inline query.

    More info at: https://core.telegram.org/bots/api/#inputlocationmessagecontent
    """

    # --- properties here ---
    latitude: float = field(metadata={"ac_type": [float], "ac_name": "latitude"})
    """Latitude of the location in degrees
    """

    longitude: float = field(metadata={"ac_type": [float], "ac_name": "longitude"})
    """Longitude of the location in degrees
    """

    horizontal_accuracy: Optional[float] = field(
        default=None, metadata={"ac_type": [float], "ac_name": "horizontal_accuracy"}
    )
    """*Optional*. The radius of uncertainty for the location, measured in meters; 0-1500
    """

    live_period: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "live_period"}
    )
    """*Optional*. Period in seconds for which the location can be updated, should be between 60 and 86400.
    """

    heading: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "heading"}
    )
    """*Optional*. For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.
    """

    proximity_alert_radius: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "proximity_alert_radius"}
    )
    """*Optional*. For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.
    """
