from dataclasses import dataclass, field
from typing import Optional

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject


@dataclass(init=True, repr=True, slots=True)
class Voice(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object represents a voice note.

    More info at: https://core.telegram.org/bots/api/#voice
    """

    # --- properties here ---
    file_id: str = field(metadata={"ac_type": [str], "ac_name": "file_id"})
    """Identifier for this file, which can be used to download or reuse the file
    """

    file_unique_id: str = field(
        metadata={"ac_type": [str], "ac_name": "file_unique_id"}
    )
    """Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    """

    duration: int = field(metadata={"ac_type": [int], "ac_name": "duration"})
    """Duration of the audio in seconds as defined by sender
    """

    mime_type: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "mime_type"}
    )
    """*Optional*. MIME type of the file as defined by sender
    """

    file_size: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "file_size"}
    )
    """*Optional*. File size in bytes
    """
