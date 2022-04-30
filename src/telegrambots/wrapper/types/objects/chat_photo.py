from dataclasses import dataclass, field

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject


@dataclass(init=True, repr=True, slots=True)
class ChatPhoto(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object represents a chat photo.

    More info at: https://core.telegram.org/bots/api/#chatphoto
    """

    # --- properties here ---
    small_file_id: str = field(metadata={"ac_type": [str], "ac_name": "small_file_id"})
    """File identifier of small (160x160) chat photo. This file\\_id can be used only for photo download and only for as long as the photo is not changed.
    """

    small_file_unique_id: str = field(
        metadata={"ac_type": [str], "ac_name": "small_file_unique_id"}
    )
    """Unique file identifier of small (160x160) chat photo, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    """

    big_file_id: str = field(metadata={"ac_type": [str], "ac_name": "big_file_id"})
    """File identifier of big (640x640) chat photo. This file\\_id can be used only for photo download and only for as long as the photo is not changed.
    """

    big_file_unique_id: str = field(
        metadata={"ac_type": [str], "ac_name": "big_file_unique_id"}
    )
    """Unique file identifier of big (640x640) chat photo, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    """
