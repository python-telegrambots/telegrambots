from dataclasses import dataclass, field
from typing import Literal

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject
from .passport_element_error import PassportElementError


@dataclass(init=True, repr=True, slots=True)
class PassportElementErrorTranslationFiles(PassportElementError):
    # --- description here ---
    """Represents an issue with the translated version of a document. The error is considered resolved when a file with the document translation change.

    More info at: https://core.telegram.org/bots/api/#passportelementerrortranslationfiles
    """

    # --- properties here ---
    source: str = field(metadata={"ac_type": [str], "ac_name": "source"})
    """Error source, must be *translation\\_files*
    """

    type: Literal[
        "passport",
        "driver_license",
        "identity_card",
        "internal_passport",
        "utility_bill",
        "bank_statement",
        "rental_agreement",
        "passport_registration",
        "temporary_registration",
    ] = field(metadata={"ac_type": [str], "ac_name": "type"})
    """Type of element of the user's Telegram Passport which has the issue, one of “passport”, “driver\\_license”, “identity\\_card”, “internal\\_passport”, “utility\\_bill”, “bank\\_statement”, “rental\\_agreement”, “passport\\_registration”, “temporary\\_registration”
    """

    file_hashes: list[str] = field(
        metadata={"ac_type": [str], "ac_name": "file_hashes"}
    )
    """List of base64-encoded file hashes
    """

    message: str = field(metadata={"ac_type": [str], "ac_name": "message"})
    """Error message
    """
