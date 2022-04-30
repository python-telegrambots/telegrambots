from dataclasses import dataclass, field

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject


@dataclass(init=True, repr=True, slots=True)
class ShippingAddress(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object represents a shipping address.

    More info at: https://core.telegram.org/bots/api/#shippingaddress
    """

    # --- properties here ---
    country_code: str = field(metadata={"ac_type": [str], "ac_name": "country_code"})
    """ISO 3166-1 alpha-2 country code
    """

    state: str = field(metadata={"ac_type": [str], "ac_name": "state"})
    """State, if applicable
    """

    city: str = field(metadata={"ac_type": [str], "ac_name": "city"})
    """City
    """

    street_line1: str = field(metadata={"ac_type": [str], "ac_name": "street_line1"})
    """First line for the address
    """

    street_line2: str = field(metadata={"ac_type": [str], "ac_name": "street_line2"})
    """Second line for the address
    """

    post_code: str = field(metadata={"ac_type": [str], "ac_name": "post_code"})
    """Address post code
    """
