from dataclasses import dataclass, field

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject

from .user import User
from .shipping_address import ShippingAddress


@dataclass(init=True, repr=True, slots=True)
class ShippingQuery(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object contains information about an incoming shipping query.

    More info at: https://core.telegram.org/bots/api/#shippingquery
    """

    # --- properties here ---
    id: str = field(metadata={"ac_type": [str], "ac_name": "id"})
    """Unique query identifier
    """

    from_user: User = field(metadata={"ac_type": [User], "ac_name": "from"})
    """User who sent the query
    """

    invoice_payload: str = field(
        metadata={"ac_type": [str], "ac_name": "invoice_payload"}
    )
    """Bot specified invoice payload
    """

    shipping_address: ShippingAddress = field(
        metadata={"ac_type": [ShippingAddress], "ac_name": "shipping_address"}
    )
    """User specified shipping address
    """
