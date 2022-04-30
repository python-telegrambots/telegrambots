from dataclasses import dataclass, field
from typing import Literal

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject
from .passport_element_error import PassportElementError


@dataclass(init=True, repr=True, slots=True)
class PassportElementErrorFiles(PassportElementError):
    # --- description here ---
    """Represents an issue with a list of scans. The error is considered resolved when the list of files containing the scans changes.

    More info at: https://core.telegram.org/bots/api/#passportelementerrorfiles
    """

    # --- properties here ---
    source: str = field(metadata={"ac_type": [str], "ac_name": "source"})
    """Error source, must be *files*
    """

    type: Literal[
        "utility_bill",
        "bank_statement",
        "rental_agreement",
        "passport_registration",
        "temporary_registration",
    ] = field(metadata={"ac_type": [str], "ac_name": "type"})
    """The section of the user's Telegram Passport which has the issue, one of “utility\\_bill”, “bank\\_statement”, “rental\\_agreement”, “passport\\_registration”, “temporary\\_registration”
    """

    file_hashes: list[str] = field(
        metadata={"ac_type": [str], "ac_name": "file_hashes"}
    )
    """List of base64-encoded file hashes
    """

    message: str = field(metadata={"ac_type": [str], "ac_name": "message"})
    """Error message
    """
