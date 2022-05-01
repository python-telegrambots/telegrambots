from dataclasses import dataclass, field
from typing import Literal

from .passport_element_error import PassportElementError


@dataclass(init=True, repr=True, slots=True)
class PassportElementErrorReverseSide(PassportElementError):
    # --- description here ---
    """Represents an issue with the reverse side of a document. The error is considered resolved when the file with reverse side of the document changes.

    More info at: https://core.telegram.org/bots/api/#passportelementerrorreverseside
    """

    # --- properties here ---
    @property
    def source(self) -> str:
        self._source = "reverse_side"
        return self._source

    type: Literal["driver_license", "identity_card"] = field(
        metadata={"ac_type": [str], "ac_name": "type"}
    )
    """The section of the user's Telegram Passport which has the issue, one of “driver\\_license”, “identity\\_card”
    """

    file_hash: str = field(metadata={"ac_type": [str], "ac_name": "file_hash"})
    """Base64-encoded hash of the file with the reverse side of the document
    """

    message: str = field(metadata={"ac_type": [str], "ac_name": "message"})
    """Error message
    """
