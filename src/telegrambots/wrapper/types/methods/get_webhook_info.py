from dataclasses import dataclass
from typing import Any

from ..api_method import TelegramBotsMethod
from ..api_result import TelegramBotsApiResult
from ..objects.webhook_info import WebhookInfo


@dataclass(init=True, repr=True, slots=True)
class GetWebhookInfo(TelegramBotsMethod[TelegramBotsApiResult[WebhookInfo]]):
    # --- description here ---
    """Use this method to get current webhook status. Requires no parameters. On success, returns a [WebhookInfo](https://core.telegram.org/bots/api/#webhookinfo) object. If the bot is using [getUpdates](https://core.telegram.org/bots/api/#getupdates), will return an object with the *url* field empty.
    
    More info at: https://core.telegram.org/bots/api/#getwebhookinfo
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMethod.__init__(  # type: ignore
            obj, "getWebhookInfo", [WebhookInfo])
        return obj


    # --- arguments here ---

