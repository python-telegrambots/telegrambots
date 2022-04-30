from dataclasses import dataclass, field

from .chat_member import ChatMember
from .user import User


@dataclass(init=True, repr=True, slots=True)
class ChatMemberBanned(ChatMember):
    # --- description here ---
    """Represents a [chat member](https://core.telegram.org/bots/api/#chatmember) that was banned in the chat and can't return to the chat or view chat messages.

    More info at: https://core.telegram.org/bots/api/#chatmemberbanned
    """

    # --- properties here ---
    status: str = field(metadata={"ac_type": [str], "ac_name": "status"})
    """The member's status in the chat, always “kicked”
    """

    user: User = field(metadata={"ac_type": [User], "ac_name": "user"})
    """Information about the user
    """

    until_date: int = field(
        metadata={"ac_type": [int], "ac_name": "until_date"})
    """Date when restrictions will be lifted for this user; unix time. If 0, then the user is banned forever
    """
