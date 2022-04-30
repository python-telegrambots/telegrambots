from dataclasses import dataclass, field

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject

from .photo_size import PhotoSize


@dataclass(init=True, repr=True, slots=True)
class UserProfilePhotos(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object represent a user's profile pictures.

    More info at: https://core.telegram.org/bots/api/#userprofilephotos
    """

    # --- properties here ---
    total_count: int = field(metadata={"ac_type": [int], "ac_name": "total_count"})
    """Total number of profile pictures the target user has
    """

    photos: list[list[PhotoSize]] = field(
        metadata={"ac_type": [PhotoSize], "ac_name": "photos"}
    )
    """Requested profile pictures (in up to 4 sizes each)
    """
