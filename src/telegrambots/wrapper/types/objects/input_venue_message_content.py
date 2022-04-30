from dataclasses import dataclass, field
from typing import Optional

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject
from .input_message_content import InputMessageContent


@dataclass(init=True, repr=True, slots=True)
class InputVenueMessageContent(InputMessageContent):
    # --- description here ---
    """Represents the [content](https://core.telegram.org/bots/api/#inputmessagecontent) of a venue message to be sent as the result of an inline query.

    More info at: https://core.telegram.org/bots/api/#inputvenuemessagecontent
    """

    # --- properties here ---
    latitude: float = field(metadata={"ac_type": [float], "ac_name": "latitude"})
    """Latitude of the venue in degrees
    """

    longitude: float = field(metadata={"ac_type": [float], "ac_name": "longitude"})
    """Longitude of the venue in degrees
    """

    title: str = field(metadata={"ac_type": [str], "ac_name": "title"})
    """Name of the venue
    """

    address: str = field(metadata={"ac_type": [str], "ac_name": "address"})
    """Address of the venue
    """

    foursquare_id: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "foursquare_id"}
    )
    """*Optional*. Foursquare identifier of the venue, if known
    """

    foursquare_type: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "foursquare_type"}
    )
    """*Optional*. Foursquare type of the venue, if known. (For example, “arts\\_entertainment/default”, “arts\\_entertainment/aquarium” or “food/icecream”.)
    """

    google_place_id: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "google_place_id"}
    )
    """*Optional*. Google Places identifier of the venue
    """

    google_place_type: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "google_place_type"}
    )
    """*Optional*. Google Places type of the venue. (See [supported types](https://developers.google.com/places/web-service/supported_types).)
    """
