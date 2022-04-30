from dataclasses import dataclass, field
from typing import Literal

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject
from .passport_element_error import PassportElementError


@dataclass(init=True, repr=True, slots=True)
class PassportElementErrorSelfie(PassportElementError):
    # --- description here ---
    """Represents an issue with the selfie with a document. The error is considered resolved when the file with the selfie changes.

    More info at: https://core.telegram.org/bots/api/#passportelementerrorselfie
    """

    # --- properties here ---
    source: str = field(metadata={"ac_type": [str], "ac_name": "source"})
    """Error source, must be *selfie*
    """

    type: Literal[
        "passport", "driver_license", "identity_card", "internal_passport"
    ] = field(metadata={"ac_type": [str], "ac_name": "type"})
    """The section of the user's Telegram Passport which has the issue, one of “passport”, “driver\\_license”, “identity\\_card”, “internal\\_passport”
    """

    file_hash: str = field(metadata={"ac_type": [str], "ac_name": "file_hash"})
    """Base64-encoded hash of the file with the selfie
    """

    message: str = field(metadata={"ac_type": [str], "ac_name": "message"})
    """Error message
    """
