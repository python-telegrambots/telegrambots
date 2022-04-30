from dataclasses import dataclass, field

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject

from .user import User


@dataclass(init=True, repr=True, slots=True)
class VideoChatParticipantsInvited(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object represents a service message about new members invited to a video chat.

    More info at: https://core.telegram.org/bots/api/#videochatparticipantsinvited
    """

    # --- properties here ---
    users: list[User] = field(metadata={"ac_type": [User], "ac_name": "users"})
    """New members that were invited to the video chat
    """
