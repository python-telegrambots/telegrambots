from dataclasses import dataclass, field

from .chat_member import ChatMember
from .user import User


@dataclass(init=True, repr=True, slots=True)
class ChatMemberMember(ChatMember):
    # --- description here ---
    """Represents a [chat member](https://core.telegram.org/bots/api/#chatmember) that has no additional privileges or restrictions.

    More info at: https://core.telegram.org/bots/api/#chatmembermember
    """

    # --- properties here ---
    status: str = field(metadata={"ac_type": [str], "ac_name": "status"})
    """The member's status in the chat, always “member”
    """

    user: User = field(metadata={"ac_type": [User], "ac_name": "user"})
    """Information about the user
    """
