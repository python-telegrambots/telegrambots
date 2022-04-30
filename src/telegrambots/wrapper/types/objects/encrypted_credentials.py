from dataclasses import dataclass, field

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject


@dataclass(init=True, repr=True, slots=True)
class EncryptedCredentials(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """Contains data required for decrypting and authenticating [EncryptedPassportElement](https://core.telegram.org/bots/api/#encryptedpassportelement). See the [Telegram Passport Documentation](https://core.telegram.org/passport#receiving-information) for a complete description of the data decryption and authentication processes.

    More info at: https://core.telegram.org/bots/api/#encryptedcredentials
    """

    # --- properties here ---
    data: str = field(metadata={"ac_type": [str], "ac_name": "data"})
    """Base64-encoded encrypted JSON-serialized data with unique user's payload, data hashes and secrets required for [EncryptedPassportElement](https://core.telegram.org/bots/api/#encryptedpassportelement) decryption and authentication
    """

    hash: str = field(metadata={"ac_type": [str], "ac_name": "hash"})
    """Base64-encoded data hash for data authentication
    """

    secret: str = field(metadata={"ac_type": [str], "ac_name": "secret"})
    """Base64-encoded secret, encrypted with the bot's public RSA key, required for data decryption
    """
