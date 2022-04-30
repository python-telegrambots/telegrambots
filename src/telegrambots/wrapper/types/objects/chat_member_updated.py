from dataclasses import dataclass, field
from typing import Optional

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject

from .chat_invite_link import ChatInviteLink
from .user import User
from .chat_member import ChatMember
from .chat import Chat


@dataclass(init=True, repr=True, slots=True)
class ChatMemberUpdated(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object represents changes in the status of a chat member.

    More info at: https://core.telegram.org/bots/api/#chatmemberupdated
    """

    # --- properties here ---
    chat: Chat = field(metadata={"ac_type": [Chat], "ac_name": "chat"})
    """Chat the user belongs to
    """

    from_user: User = field(metadata={"ac_type": [User], "ac_name": "from"})
    """Performer of the action, which resulted in the change
    """

    date: int = field(metadata={"ac_type": [int], "ac_name": "date"})
    """Date the change was done in Unix time
    """

    old_chat_member: ChatMember = field(
        metadata={"ac_type": [ChatMember], "ac_name": "old_chat_member"}
    )
    """Previous information about the chat member
    """

    new_chat_member: ChatMember = field(
        metadata={"ac_type": [ChatMember], "ac_name": "new_chat_member"}
    )
    """New information about the chat member
    """

    invite_link: Optional[ChatInviteLink] = field(
        default=None, metadata={"ac_type": [ChatInviteLink], "ac_name": "invite_link"}
    )
    """*Optional*. Chat invite link, which was used by the user to join the chat; for joining by invite link events only.
    """
