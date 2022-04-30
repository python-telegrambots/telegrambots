from dataclasses import dataclass, field
from typing import Optional

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject


@dataclass(init=True, repr=True, slots=True)
class PhotoSize(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object represents one size of a photo or a [file](https://core.telegram.org/bots/api/#document) / [sticker](https://core.telegram.org/bots/api/#sticker) thumbnail.

    More info at: https://core.telegram.org/bots/api/#photosize
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

    width: int = field(metadata={"ac_type": [int], "ac_name": "width"})
    """Photo width
    """

    height: int = field(metadata={"ac_type": [int], "ac_name": "height"})
    """Photo height
    """

    file_size: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "file_size"}
    )
    """*Optional*. File size in bytes
    """
