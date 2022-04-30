from dataclasses import dataclass, field
from typing import Optional

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject

from .user import User


@dataclass(init=True, repr=True, slots=True)
class ChatInviteLink(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """Represents an invite link for a chat.

    More info at: https://core.telegram.org/bots/api/#chatinvitelink
    """

    # --- properties here ---
    invite_link: str = field(metadata={"ac_type": [str], "ac_name": "invite_link"})
    """The invite link. If the link was created by another chat administrator, then the second part of the link will be replaced with “…”.
    """

    creator: User = field(metadata={"ac_type": [User], "ac_name": "creator"})
    """Creator of the link
    """

    creates_join_request: bool = field(
        metadata={"ac_type": [bool], "ac_name": "creates_join_request"}
    )
    """*True*, if users joining the chat via the link need to be approved by chat administrators
    """

    is_primary: bool = field(metadata={"ac_type": [bool], "ac_name": "is_primary"})
    """*True*, if the link is primary
    """

    is_revoked: bool = field(metadata={"ac_type": [bool], "ac_name": "is_revoked"})
    """*True*, if the link is revoked
    """

    name: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "name"}
    )
    """*Optional*. Invite link name
    """

    expire_date: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "expire_date"}
    )
    """*Optional*. Point in time (Unix timestamp) when the link will expire or has been expired
    """

    member_limit: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "member_limit"}
    )
    """*Optional*. Maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1-99999
    """

    pending_join_request_count: Optional[int] = field(
        default=None,
        metadata={"ac_type": [int], "ac_name": "pending_join_request_count"},
    )
    """*Optional*. Number of pending join requests created using this link
    """
