from dataclasses import dataclass, field
from typing import Literal

from .passport_element_error import PassportElementError


@dataclass(init=True, repr=True, slots=True)
class PassportElementErrorTranslationFile(PassportElementError):
    # --- description here ---
    """Represents an issue with one of the files that constitute the translation of a document. The error is considered resolved when the file changes.

    More info at: https://core.telegram.org/bots/api/#passportelementerrortranslationfile
    """

    # --- properties here ---
    @property
    def source(self) -> str:
        self._source = "translation_file"
        return self._source

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

    file_hash: str = field(metadata={"ac_type": [str], "ac_name": "file_hash"})
    """Base64-encoded file hash
    """

    message: str = field(metadata={"ac_type": [str], "ac_name": "message"})
    """Error message
    """
