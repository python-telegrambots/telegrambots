from dataclasses import dataclass, field

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject
from .passport_element_error import PassportElementError


@dataclass(init=True, repr=True, slots=True)
class PassportElementErrorUnspecified(PassportElementError):
    # --- description here ---
    """Represents an issue in an unspecified place. The error is considered resolved when new data is added.

    More info at: https://core.telegram.org/bots/api/#passportelementerrorunspecified
    """

    # --- properties here ---
    source: str = field(metadata={"ac_type": [str], "ac_name": "source"})
    """Error source, must be *unspecified*
    """

    type: str = field(metadata={"ac_type": [str], "ac_name": "type"})
    """Type of element of the user's Telegram Passport which has the issue
    """

    element_hash: str = field(metadata={"ac_type": [str], "ac_name": "element_hash"})
    """Base64-encoded element hash
    """

    message: str = field(metadata={"ac_type": [str], "ac_name": "message"})
    """Error message
    """
