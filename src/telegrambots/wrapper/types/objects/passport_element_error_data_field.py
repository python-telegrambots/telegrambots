from dataclasses import dataclass, field
from typing import Literal

from .passport_element_error import PassportElementError


@dataclass(init=True, repr=True, slots=True)
class PassportElementErrorDataField(PassportElementError):
    # --- description here ---
    """Represents an issue in one of the data fields that was provided by the user. The error is considered resolved when the field's value changes.

    More info at: https://core.telegram.org/bots/api/#passportelementerrordatafield
    """

    # --- properties here ---
    @property
    def source(self) -> str:
        self._source = "data"
        return self._source

    type: Literal[
        "personal_details",
        "passport",
        "driver_license",
        "identity_card",
        "internal_passport",
        "address",
    ] = field(metadata={"ac_type": [str], "ac_name": "type"})
    """The section of the user's Telegram Passport which has the error, one of “personal\\_details”, “passport”, “driver\\_license”, “identity\\_card”, “internal\\_passport”, “address”
    """

    field_name: str = field(metadata={"ac_type": [str], "ac_name": "field_name"})
    """Name of the data field which has the error
    """

    data_hash: str = field(metadata={"ac_type": [str], "ac_name": "data_hash"})
    """Base64-encoded data hash
    """

    message: str = field(metadata={"ac_type": [str], "ac_name": "message"})
    """Error message
    """
