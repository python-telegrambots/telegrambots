from dataclasses import dataclass, field
from typing import Optional

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject

from .chat_invite_link import ChatInviteLink
from .user import User
from .chat import Chat


@dataclass(init=True, repr=True, slots=True)
class ChatJoinRequest(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """Represents a join request sent to a chat.

    More info at: https://core.telegram.org/bots/api/#chatjoinrequest
    """

    # --- properties here ---
    chat: Chat = field(metadata={"ac_type": [Chat], "ac_name": "chat"})
    """Chat to which the request was sent
    """

    from_user: User = field(metadata={"ac_type": [User], "ac_name": "from"})
    """User that sent the join request
    """

    date: int = field(metadata={"ac_type": [int], "ac_name": "date"})
    """Date the request was sent in Unix time
    """

    bio: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "bio"}
    )
    """*Optional*. Bio of the user.
    """

    invite_link: Optional[ChatInviteLink] = field(
        default=None, metadata={"ac_type": [ChatInviteLink], "ac_name": "invite_link"}
    )
    """*Optional*. Chat invite link that was used by the user to send the join request
    """
