from dataclasses import dataclass, field
from typing import Optional

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject

from .photo_size import PhotoSize


@dataclass(init=True, repr=True, slots=True)
class VideoNote(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object represents a [video message](https://telegram.org/blog/video-messages-and-telescope) (available in Telegram apps as of [v.4.0](https://telegram.org/blog/video-messages-and-telescope)).

    More info at: https://core.telegram.org/bots/api/#videonote
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

    length: int = field(metadata={"ac_type": [int], "ac_name": "length"})
    """Video width and height (diameter of the video message) as defined by sender
    """

    duration: int = field(metadata={"ac_type": [int], "ac_name": "duration"})
    """Duration of the video in seconds as defined by sender
    """

    thumb: Optional[PhotoSize] = field(
        default=None, metadata={"ac_type": [PhotoSize], "ac_name": "thumb"}
    )
    """*Optional*. Video thumbnail
    """

    file_size: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "file_size"}
    )
    """*Optional*. File size in bytes
    """
