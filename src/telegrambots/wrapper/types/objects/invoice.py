from dataclasses import dataclass, field

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject


@dataclass(init=True, repr=True, slots=True)
class Invoice(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object contains basic information about an invoice.

    More info at: https://core.telegram.org/bots/api/#invoice
    """

    # --- properties here ---
    title: str = field(metadata={"ac_type": [str], "ac_name": "title"})
    """Product name
    """

    description: str = field(metadata={"ac_type": [str], "ac_name": "description"})
    """Product description
    """

    start_parameter: str = field(
        metadata={"ac_type": [str], "ac_name": "start_parameter"}
    )
    """Unique bot deep-linking parameter that can be used to generate this invoice
    """

    currency: str = field(metadata={"ac_type": [str], "ac_name": "currency"})
    """Three-letter ISO 4217 [currency](https://core.telegram.org/bots/payments#supported-currencies) code
    """

    total_amount: int = field(metadata={"ac_type": [int], "ac_name": "total_amount"})
    """Total price in the *smallest units* of the currency (integer, **not** float/double). For example, for a price of `US$ 1.45` pass `amount = 145`. See the *exp* parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
    """
