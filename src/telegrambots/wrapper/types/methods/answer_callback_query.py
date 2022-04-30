from dataclasses import dataclass, field
from typing import Any, Optional

from ..api_method import TelegramBotsMethod
from ..api_result import TelegramBotsApiResult



@dataclass(init=True, repr=True, slots=True)
class AnswerCallbackQuery(TelegramBotsMethod[TelegramBotsApiResult[bool]]):
    # --- description here ---
    """Use this method to send answers to callback queries sent from [inline keyboards](https://core.telegram.org/bots#inline-keyboards-and-on-the-fly-updating). The answer will be displayed to the user as a notification at the top of the chat screen or as an alert. On success, *True* is returned.
    
    Alternatively, the user can be redirected to the specified Game URL. For this option to work, you must first create a game for your bot via [@Botfather](https://t.me/botfather) and accept the terms. Otherwise, you may use links like `t.me/your_bot?start=XXXX` that open your bot with a parameter.
    
    More info at: https://core.telegram.org/bots/api/#answercallbackquery
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMethod.__init__(  # type: ignore
            obj, "answerCallbackQuery", [bool])
        return obj


    # --- arguments here ---
    callback_query_id: str = field(metadata={"ac_type": [str], "ac_name": "callback_query_id"})
    """Unique identifier for the query to be answered
    """

    text: Optional[str] = field(default=None, metadata={"ac_type": [str], "ac_name": "text"})
    """Text of the notification. If not specified, nothing will be shown to the user, 0-200 characters
    """

    show_alert: bool = field(default=False, metadata={"ac_type": [bool], "ac_name": "show_alert"})
    """If *True*, an alert will be shown by the client instead of a notification at the top of the chat screen. Defaults to *false*.
    """

    url: Optional[str] = field(default=None, metadata={"ac_type": [str], "ac_name": "url"})
    """URL that will be opened by the user's client. If you have created a [Game](https://core.telegram.org/bots/api/#game) and accepted the conditions via [@Botfather](https://t.me/botfather), specify the URL that opens your game — note that this will only work if the query comes from a [*callback\\_game*](https://core.telegram.org/bots/api/#inlinekeyboardbutton) button.  

Otherwise, you may use links like `t.me/your_bot?start=XXXX` that open your bot with a parameter.
    """

    cache_time: int = field(default=0, metadata={"ac_type": [int], "ac_name": "cache_time"})
    """The maximum amount of time in seconds that the result of the callback query may be cached client-side. Telegram apps will support caching starting in version 3.14. Defaults to 0.
    """

