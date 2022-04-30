from dataclasses import dataclass, field
from typing import Optional

from .chat_member import ChatMember
from .user import User


@dataclass(init=True, repr=True, slots=True)
class ChatMemberOwner(ChatMember):
    # --- description here ---
    """Represents a [chat member](https://core.telegram.org/bots/api/#chatmember) that owns the chat and has all administrator privileges.

    More info at: https://core.telegram.org/bots/api/#chatmemberowner
    """

    # --- properties here ---
    status: str = field(metadata={"ac_type": [str], "ac_name": "status"})
    """The member's status in the chat, always “creator”
    """

    user: User = field(metadata={"ac_type": [User], "ac_name": "user"})
    """Information about the user
    """

    is_anonymous: bool = field(
        metadata={"ac_type": [bool], "ac_name": "is_anonymous"})
    """*True*, if the user's presence in the chat is hidden
    """

    custom_title: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "custom_title"})
    """*Optional*. Custom title for this user
    """
