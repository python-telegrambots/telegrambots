from dataclasses import dataclass, field
from typing import Any, Optional

from ..api_method import TelegramBotsMethod
from ..api_result import TelegramBotsApiResult
from ..objects.user_profile_photos import UserProfilePhotos


@dataclass(init=True, repr=True, slots=True)
class GetUserProfilePhotos(TelegramBotsMethod[TelegramBotsApiResult[UserProfilePhotos]]):
    # --- description here ---
    """Use this method to get a list of profile pictures for a user. Returns a [UserProfilePhotos](https://core.telegram.org/bots/api/#userprofilephotos) object.
    
    More info at: https://core.telegram.org/bots/api/#getuserprofilephotos
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMethod.__init__(  # type: ignore
            obj, "getUserProfilePhotos", [UserProfilePhotos])
        return obj


    # --- arguments here ---
    user_id: int = field(metadata={"ac_type": [int], "ac_name": "user_id"})
    """Unique identifier of the target user
    """

    offset: Optional[int] = field(default=None, metadata={"ac_type": [int], "ac_name": "offset"})
    """Sequential number of the first photo to be returned. By default, all photos are returned.
    """

    limit: int = field(default=100, metadata={"ac_type": [int], "ac_name": "limit"})
    """Limits the number of photos to be retrieved. Values between 1-100 are accepted. Defaults to 100.
    """

