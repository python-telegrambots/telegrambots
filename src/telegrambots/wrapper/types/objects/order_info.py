from dataclasses import dataclass, field
from typing import Optional

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject

from .shipping_address import ShippingAddress


@dataclass(init=True, repr=True, slots=True)
class OrderInfo(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object represents information about an order.

    More info at: https://core.telegram.org/bots/api/#orderinfo
    """

    # --- properties here ---
    name: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "name"}
    )
    """*Optional*. User name
    """

    phone_number: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "phone_number"}
    )
    """*Optional*. User's phone number
    """

    email: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "email"}
    )
    """*Optional*. User email
    """

    shipping_address: Optional[ShippingAddress] = field(
        default=None,
        metadata={"ac_type": [ShippingAddress], "ac_name": "shipping_address"},
    )
    """*Optional*. User shipping address
    """
