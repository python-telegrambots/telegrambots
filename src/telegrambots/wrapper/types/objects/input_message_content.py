import abc
import dataclasses

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject


@dataclasses.dataclass(init=True, repr=True, slots=True)
class InputMessageContent(abc.ABC, TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object represents the content of a message to be sent as a result of an inline query. Telegram clients currently support the following 5 types:

    * [InputTextMessageContent](https://core.telegram.org/bots/api/#inputtextmessagecontent)
    * [InputLocationMessageContent](https://core.telegram.org/bots/api/#inputlocationmessagecontent)
    * [InputVenueMessageContent](https://core.telegram.org/bots/api/#inputvenuemessagecontent)
    * [InputContactMessageContent](https://core.telegram.org/bots/api/#inputcontactmessagecontent)
    * [InputInvoiceMessageContent](https://core.telegram.org/bots/api/#inputinvoicemessagecontent)

    More info at: https://core.telegram.org/bots/api/#inputmessagecontent
    """
