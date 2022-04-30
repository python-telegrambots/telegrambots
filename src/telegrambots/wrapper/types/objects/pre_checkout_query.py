from dataclasses import dataclass, field
from typing import Optional

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject

from .user import User
from .order_info import OrderInfo


@dataclass(init=True, repr=True, slots=True)
class PreCheckoutQuery(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object contains information about an incoming pre-checkout query.

    More info at: https://core.telegram.org/bots/api/#precheckoutquery
    """

    # --- properties here ---
    id: str = field(metadata={"ac_type": [str], "ac_name": "id"})
    """Unique query identifier
    """

    from_user: User = field(metadata={"ac_type": [User], "ac_name": "from"})
    """User who sent the query
    """

    currency: str = field(metadata={"ac_type": [str], "ac_name": "currency"})
    """Three-letter ISO 4217 [currency](https://core.telegram.org/bots/payments#supported-currencies) code
    """

    total_amount: int = field(metadata={"ac_type": [int], "ac_name": "total_amount"})
    """Total price in the *smallest units* of the currency (integer, **not** float/double). For example, for a price of `US$ 1.45` pass `amount = 145`. See the *exp* parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
    """

    invoice_payload: str = field(
        metadata={"ac_type": [str], "ac_name": "invoice_payload"}
    )
    """Bot specified invoice payload
    """

    shipping_option_id: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "shipping_option_id"}
    )
    """*Optional*. Identifier of the shipping option chosen by the user
    """

    order_info: Optional[OrderInfo] = field(
        default=None, metadata={"ac_type": [OrderInfo], "ac_name": "order_info"}
    )
    """*Optional*. Order info provided by the user
    """
