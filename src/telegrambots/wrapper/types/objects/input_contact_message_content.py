from dataclasses import dataclass, field
from typing import Optional

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject
from .input_message_content import InputMessageContent


@dataclass(init=True, repr=True, slots=True)
class InputContactMessageContent(InputMessageContent):
    # --- description here ---
    """Represents the [content](https://core.telegram.org/bots/api/#inputmessagecontent) of a contact message to be sent as the result of an inline query.

    More info at: https://core.telegram.org/bots/api/#inputcontactmessagecontent
    """

    # --- properties here ---
    phone_number: str = field(metadata={"ac_type": [str], "ac_name": "phone_number"})
    """Contact's phone number
    """

    first_name: str = field(metadata={"ac_type": [str], "ac_name": "first_name"})
    """Contact's first name
    """

    last_name: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "last_name"}
    )
    """*Optional*. Contact's last name
    """

    vcard: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "vcard"}
    )
    """*Optional*. Additional data about the contact in the form of a [vCard](https://en.wikipedia.org/wiki/VCard), 0-2048 bytes
    """
