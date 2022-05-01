from dataclasses import dataclass, field
from typing import Literal

from .passport_element_error import PassportElementError


@dataclass(init=True, repr=True, slots=True)
class PassportElementErrorFile(PassportElementError):
    # --- description here ---
    """Represents an issue with a document scan. The error is considered resolved when the file with the document scan changes.

    More info at: https://core.telegram.org/bots/api/#passportelementerrorfile
    """

    # --- properties here ---
    @property
    def source(self) -> str:
        self._source = "file"
        return self._source

    type: Literal[
        "utility_bill",
        "bank_statement",
        "rental_agreement",
        "passport_registration",
        "temporary_registration",
    ] = field(metadata={"ac_type": [str], "ac_name": "type"})
    """The section of the user's Telegram Passport which has the issue, one of “utility\\_bill”, “bank\\_statement”, “rental\\_agreement”, “passport\\_registration”, “temporary\\_registration”
    """

    file_hash: str = field(metadata={"ac_type": [str], "ac_name": "file_hash"})
    """Base64-encoded file hash
    """

    message: str = field(metadata={"ac_type": [str], "ac_name": "message"})
    """Error message
    """
