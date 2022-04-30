from dataclasses import dataclass, field
from typing import Any, Optional

from ..api_multipart_method import TelegramBotsMultipartMethod
from ..api_result import TelegramBotsApiResult
from ..objects.input_file import InputFile


@dataclass(init=True, repr=True, slots=True)
class SetWebhook(TelegramBotsMultipartMethod[TelegramBotsApiResult[bool]]):
    # --- description here ---
    """Use this method to specify a url and receive incoming updates via an outgoing webhook. Whenever there is an update for the bot, we will send an HTTPS POST request to the specified url, containing a JSON-serialized [Update](https://core.telegram.org/bots/api/#update). In case of an unsuccessful request, we will give up after a reasonable amount of attempts. Returns *True* on success.
    
    If you'd like to make sure that the Webhook request comes from Telegram, we recommend using a secret path in the URL, e.g. `https://www.example.com/<token>`. Since nobody else knows your bot's token, you can be pretty sure it's us.
    
    More info at: https://core.telegram.org/bots/api/#setwebhook
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMultipartMethod.__init__(  # type: ignore
            obj, "setWebhook", [bool])
        return obj


    # --- arguments here ---
    url: str = field(metadata={"ac_type": [str], "ac_name": "url"})
    """HTTPS url to send updates to. Use an empty string to remove webhook integration
    """

    certificate: Optional[InputFile] = field(default=None, metadata={"ac_type": [InputFile], "ac_name": "certificate"})
    """Upload your public key certificate so that the root certificate in use can be checked. See our [self-signed guide](https://core.telegram.org/bots/self-signed) for details.
    """

    ip_address: Optional[str] = field(default=None, metadata={"ac_type": [str], "ac_name": "ip_address"})
    """The fixed IP address which will be used to send webhook requests instead of the IP address resolved through DNS
    """

    max_connections: int = field(default=40, metadata={"ac_type": [int], "ac_name": "max_connections"})
    """Maximum allowed number of simultaneous HTTPS connections to the webhook for update delivery, 1-100. Defaults to *40*. Use lower values to limit the load on your bot's server, and higher values to increase your bot's throughput.
    """

    allowed_updates: Optional[list[str]] = field(default=None, metadata={"ac_type": [str], "ac_name": "allowed_updates"})
    """A JSON-serialized list of the update types you want your bot to receive. For example, specify [“message”, “edited\\_channel\\_post”, “callback\\_query”] to only receive updates of these types. See [Update](https://core.telegram.org/bots/api/#update) for a complete list of available update types. Specify an empty list to receive all update types except *chat\\_member* (default). If not specified, the previous setting will be used.  
Please note that this parameter doesn't affect updates created before the call to the setWebhook, so unwanted updates may be received for a short period of time.
    """

    drop_pending_updates: Optional[bool] = field(default=None, metadata={"ac_type": [bool], "ac_name": "drop_pending_updates"})
    """Pass *True* to drop all pending updates
    """

