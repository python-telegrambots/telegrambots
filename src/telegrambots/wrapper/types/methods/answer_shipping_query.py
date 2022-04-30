from dataclasses import dataclass, field
from typing import Any, Optional

from ..api_method import TelegramBotsMethod
from ..api_result import TelegramBotsApiResult
from ..objects.shipping_option import ShippingOption


@dataclass(init=True, repr=True, slots=True)
class AnswerShippingQuery(TelegramBotsMethod[TelegramBotsApiResult[bool]]):
    # --- description here ---
    """If you sent an invoice requesting a shipping address and the parameter *is\\_flexible* was specified, the Bot API will send an [Update](https://core.telegram.org/bots/api/#update) with a *shipping\\_query* field to the bot. Use this method to reply to shipping queries. On success, *True* is returned.
    
    More info at: https://core.telegram.org/bots/api/#answershippingquery
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMethod.__init__(  # type: ignore
            obj, "answerShippingQuery", [bool])
        return obj


    # --- arguments here ---
    shipping_query_id: str = field(metadata={"ac_type": [str], "ac_name": "shipping_query_id"})
    """Unique identifier for the query to be answered
    """

    ok: bool = field(metadata={"ac_type": [bool], "ac_name": "ok"})
    """Specify *True* if delivery to the specified address is possible and False if there are any problems (for example, if delivery to the specified address is not possible)
    """

    shipping_options: Optional[list[ShippingOption]] = field(default=None, metadata={"ac_type": [ShippingOption], "ac_name": "shipping_options"})
    """Required if *ok* is *True*. A JSON-serialized array of available shipping options.
    """

    error_message: Optional[str] = field(default=None, metadata={"ac_type": [str], "ac_name": "error_message"})
    """Required if *ok* is False. Error message in human readable form that explains why it is impossible to complete the order (e.g. "Sorry, delivery to your desired address is unavailable'). Telegram will display this message to the user.
    """

