from dataclasses import dataclass, field

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject


@dataclass(init=True, repr=True, slots=True)
class LabeledPrice(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object represents a portion of the price for goods or services.

    More info at: https://core.telegram.org/bots/api/#labeledprice
    """

    # --- properties here ---
    label: str = field(metadata={"ac_type": [str], "ac_name": "label"})
    """Portion label
    """

    amount: int = field(metadata={"ac_type": [int], "ac_name": "amount"})
    """Price of the product in the *smallest units* of the [currency](https://core.telegram.org/bots/payments#supported-currencies) (integer, **not** float/double). For example, for a price of `US$ 1.45` pass `amount = 145`. See the *exp* parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).
    """
