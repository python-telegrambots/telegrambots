from dataclasses import dataclass, field
from typing import Optional

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject

from .photo_size import PhotoSize


@dataclass(init=True, repr=True, slots=True)
class Document(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object represents a general file (as opposed to [photos](https://core.telegram.org/bots/api/#photosize), [voice messages](https://core.telegram.org/bots/api/#voice) and [audio files](https://core.telegram.org/bots/api/#audio)).

    More info at: https://core.telegram.org/bots/api/#document
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

    thumb: Optional[PhotoSize] = field(
        default=None, metadata={"ac_type": [PhotoSize], "ac_name": "thumb"}
    )
    """*Optional*. Document thumbnail as defined by sender
    """

    file_name: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "file_name"}
    )
    """*Optional*. Original filename as defined by sender
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
