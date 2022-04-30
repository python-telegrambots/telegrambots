from dataclasses import dataclass, field
from typing import Any, Optional

from ..api_method import TelegramBotsMethod
from ..api_result import TelegramBotsApiResult



@dataclass(init=True, repr=True, slots=True)
class AnswerPreCheckoutQuery(TelegramBotsMethod[TelegramBotsApiResult[bool]]):
    # --- description here ---
    """Once the user has confirmed their payment and shipping details, the Bot API sends the final confirmation in the form of an [Update](https://core.telegram.org/bots/api/#update) with the field *pre\\_checkout\\_query*. Use this method to respond to such pre-checkout queries. On success, *True* is returned. **Note:** The Bot API must receive an answer within 10 seconds after the pre-checkout query was sent.
    
    More info at: https://core.telegram.org/bots/api/#answerprecheckoutquery
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMethod.__init__(  # type: ignore
            obj, "answerPreCheckoutQuery", [bool])
        return obj


    # --- arguments here ---
    pre_checkout_query_id: str = field(metadata={"ac_type": [str], "ac_name": "pre_checkout_query_id"})
    """Unique identifier for the query to be answered
    """

    ok: bool = field(metadata={"ac_type": [bool], "ac_name": "ok"})
    """Specify *True* if everything is alright (goods are available, etc.) and the bot is ready to proceed with the order. Use *False* if there are any problems.
    """

    error_message: Optional[str] = field(default=None, metadata={"ac_type": [str], "ac_name": "error_message"})
    """Required if *ok* is *False*. Error message in human readable form that explains the reason for failure to proceed with the checkout (e.g. "Sorry, somebody just bought the last of our amazing black T-shirts while you were busy filling out your payment details. Please choose a different color or garment!"). Telegram will display this message to the user.
    """

