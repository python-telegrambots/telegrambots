from dataclasses import dataclass, field
from typing import Optional

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject

from .location import Location


@dataclass(init=True, repr=True, slots=True)
class Venue(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object represents a venue.

    More info at: https://core.telegram.org/bots/api/#venue
    """

    # --- properties here ---
    location: Location = field(metadata={"ac_type": [Location], "ac_name": "location"})
    """Venue location. Can't be a live location
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
    """*Optional*. Foursquare identifier of the venue
    """

    foursquare_type: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "foursquare_type"}
    )
    """*Optional*. Foursquare type of the venue. (For example, “arts\\_entertainment/default”, “arts\\_entertainment/aquarium” or “food/icecream”.)
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
