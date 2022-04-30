from dataclasses import dataclass, field

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject

from .encrypted_credentials import EncryptedCredentials
from .encrypted_passport_element import EncryptedPassportElement


@dataclass(init=True, repr=True, slots=True)
class PassportData(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """Contains information about Telegram Passport data shared with the bot by the user.

    More info at: https://core.telegram.org/bots/api/#passportdata
    """

    # --- properties here ---
    data: list[EncryptedPassportElement] = field(
        metadata={"ac_type": [EncryptedPassportElement], "ac_name": "data"}
    )
    """Array with information about documents and other Telegram Passport elements that was shared with the bot
    """

    credentials: EncryptedCredentials = field(
        metadata={"ac_type": [EncryptedCredentials], "ac_name": "credentials"}
    )
    """Encrypted credentials required to decrypt the data
    """
