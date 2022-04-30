from dataclasses import dataclass, field
from typing import Optional

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject


@dataclass(init=True, repr=True, slots=True)
class Contact(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object represents a phone contact.

    More info at: https://core.telegram.org/bots/api/#contact
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

    user_id: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "user_id"}
    )
    """*Optional*. Contact's user identifier in Telegram. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier.
    """

    vcard: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "vcard"}
    )
    """*Optional*. Additional data about the contact in the form of a [vCard](https://en.wikipedia.org/wiki/VCard)
    """
