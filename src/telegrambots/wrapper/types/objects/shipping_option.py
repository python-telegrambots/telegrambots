from dataclasses import dataclass, field

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject

from .labeled_price import LabeledPrice


@dataclass(init=True, repr=True, slots=True)
class ShippingOption(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object represents one shipping option.

    More info at: https://core.telegram.org/bots/api/#shippingoption
    """

    # --- properties here ---
    id: str = field(metadata={"ac_type": [str], "ac_name": "id"})
    """Shipping option identifier
    """

    title: str = field(metadata={"ac_type": [str], "ac_name": "title"})
    """Option title
    """

    prices: list[LabeledPrice] = field(
        metadata={"ac_type": [LabeledPrice], "ac_name": "prices"}
    )
    """List of price portions
    """
