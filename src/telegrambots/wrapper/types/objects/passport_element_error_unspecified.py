from dataclasses import dataclass, field

from .passport_element_error import PassportElementError


@dataclass(init=True, repr=True, slots=True)
class PassportElementErrorUnspecified(PassportElementError):
    # --- description here ---
    """Represents an issue in an unspecified place. The error is considered resolved when new data is added.

    More info at: https://core.telegram.org/bots/api/#passportelementerrorunspecified
    """

    # --- properties here ---
    @property
    def source(self) -> str:
        self._source = "unspecified"
        return self._source

    type: str = field(metadata={"ac_type": [str], "ac_name": "type"})
    """Type of element of the user's Telegram Passport which has the issue
    """

    element_hash: str = field(metadata={"ac_type": [str], "ac_name": "element_hash"})
    """Base64-encoded element hash
    """

    message: str = field(metadata={"ac_type": [str], "ac_name": "message"})
    """Error message
    """
