from dataclasses import dataclass, field
from typing import Literal, Optional

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject

from .passport_file import PassportFile


@dataclass(init=True, repr=True, slots=True)
class EncryptedPassportElement(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """Contains information about documents or other Telegram Passport elements shared with the bot by the user.

    More info at: https://core.telegram.org/bots/api/#encryptedpassportelement
    """

    # --- properties here ---
    type: Literal[
        "personal_details",
        "passport",
        "driver_license",
        "identity_card",
        "internal_passport",
        "address",
        "utility_bill",
        "bank_statement",
        "rental_agreement",
        "passport_registration",
        "temporary_registration",
        "phone_number",
        "email",
    ] = field(metadata={"ac_type": [str], "ac_name": "type"})
    """Element type. One of “personal\\_details”, “passport”, “driver\\_license”, “identity\\_card”, “internal\\_passport”, “address”, “utility\\_bill”, “bank\\_statement”, “rental\\_agreement”, “passport\\_registration”, “temporary\\_registration”, “phone\\_number”, “email”.
    """

    hash: str = field(metadata={"ac_type": [str], "ac_name": "hash"})
    """Base64-encoded element hash for using in [PassportElementErrorUnspecified](https://core.telegram.org/bots/api/#passportelementerrorunspecified)
    """

    data: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "data"}
    )
    """*Optional*. Base64-encoded encrypted Telegram Passport element data provided by the user, available for “personal\\_details”, “passport”, “driver\\_license”, “identity\\_card”, “internal\\_passport” and “address” types. Can be decrypted and verified using the accompanying [EncryptedCredentials](https://core.telegram.org/bots/api/#encryptedcredentials).
    """

    phone_number: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "phone_number"}
    )
    """*Optional*. User's verified phone number, available only for “phone\\_number” type
    """

    email: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "email"}
    )
    """*Optional*. User's verified email address, available only for “email” type
    """

    files: Optional[list[PassportFile]] = field(
        default=None, metadata={"ac_type": [PassportFile], "ac_name": "files"}
    )
    """*Optional*. Array of encrypted files with documents provided by the user, available for “utility\\_bill”, “bank\\_statement”, “rental\\_agreement”, “passport\\_registration” and “temporary\\_registration” types. Files can be decrypted and verified using the accompanying [EncryptedCredentials](https://core.telegram.org/bots/api/#encryptedcredentials).
    """

    front_side: Optional[PassportFile] = field(
        default=None, metadata={"ac_type": [PassportFile], "ac_name": "front_side"}
    )
    """*Optional*. Encrypted file with the front side of the document, provided by the user. Available for “passport”, “driver\\_license”, “identity\\_card” and “internal\\_passport”. The file can be decrypted and verified using the accompanying [EncryptedCredentials](https://core.telegram.org/bots/api/#encryptedcredentials).
    """

    reverse_side: Optional[PassportFile] = field(
        default=None, metadata={"ac_type": [PassportFile], "ac_name": "reverse_side"}
    )
    """*Optional*. Encrypted file with the reverse side of the document, provided by the user. Available for “driver\\_license” and “identity\\_card”. The file can be decrypted and verified using the accompanying [EncryptedCredentials](https://core.telegram.org/bots/api/#encryptedcredentials).
    """

    selfie: Optional[PassportFile] = field(
        default=None, metadata={"ac_type": [PassportFile], "ac_name": "selfie"}
    )
    """*Optional*. Encrypted file with the selfie of the user holding a document, provided by the user; available for “passport”, “driver\\_license”, “identity\\_card” and “internal\\_passport”. The file can be decrypted and verified using the accompanying [EncryptedCredentials](https://core.telegram.org/bots/api/#encryptedcredentials).
    """

    translation: Optional[list[PassportFile]] = field(
        default=None, metadata={"ac_type": [PassportFile], "ac_name": "translation"}
    )
    """*Optional*. Array of encrypted files with translated versions of documents provided by the user. Available if requested for “passport”, “driver\\_license”, “identity\\_card”, “internal\\_passport”, “utility\\_bill”, “bank\\_statement”, “rental\\_agreement”, “passport\\_registration” and “temporary\\_registration” types. Files can be decrypted and verified using the accompanying [EncryptedCredentials](https://core.telegram.org/bots/api/#encryptedcredentials).
    """
