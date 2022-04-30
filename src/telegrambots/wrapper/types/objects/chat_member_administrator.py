from dataclasses import dataclass, field
from typing import Optional

from .chat_member import ChatMember
from .user import User


@dataclass(init=True, repr=True, slots=True)
class ChatMemberAdministrator(ChatMember):
    # --- description here ---
    """Represents a [chat member](https://core.telegram.org/bots/api/#chatmember) that has some additional privileges.

    More info at: https://core.telegram.org/bots/api/#chatmemberadministrator
    """

    # --- properties here ---
    status: str = field(metadata={"ac_type": [str], "ac_name": "status"})
    """The member's status in the chat, always “administrator”
    """

    user: User = field(metadata={"ac_type": [User], "ac_name": "user"})
    """Information about the user
    """

    can_be_edited: bool = field(
        metadata={"ac_type": [bool], "ac_name": "can_be_edited"})
    """*True*, if the bot is allowed to edit administrator privileges of that user
    """

    is_anonymous: bool = field(
        metadata={"ac_type": [bool], "ac_name": "is_anonymous"})
    """*True*, if the user's presence in the chat is hidden
    """

    can_manage_chat: bool = field(
        metadata={"ac_type": [bool], "ac_name": "can_manage_chat"})
    """*True*, if the administrator can access the chat event log, chat statistics, message statistics in channels, see channel members, see anonymous administrators in supergroups and ignore slow mode. Implied by any other administrator privilege
    """

    can_delete_messages: bool = field(
        metadata={"ac_type": [bool], "ac_name": "can_delete_messages"})
    """*True*, if the administrator can delete messages of other users
    """

    can_manage_video_chats: bool = field(
        metadata={"ac_type": [bool], "ac_name": "can_manage_video_chats"})
    """*True*, if the administrator can manage video chats
    """

    can_restrict_members: bool = field(
        metadata={"ac_type": [bool], "ac_name": "can_restrict_members"})
    """*True*, if the administrator can restrict, ban or unban chat members
    """

    can_promote_members: bool = field(
        metadata={"ac_type": [bool], "ac_name": "can_promote_members"})
    """*True*, if the administrator can add new administrators with a subset of their own privileges or demote administrators that he has promoted, directly or indirectly (promoted by administrators that were appointed by the user)
    """

    can_change_info: bool = field(
        metadata={"ac_type": [bool], "ac_name": "can_change_info"})
    """*True*, if the user is allowed to change the chat title, photo and other settings
    """

    can_invite_users: bool = field(
        metadata={"ac_type": [bool], "ac_name": "can_invite_users"})
    """*True*, if the user is allowed to invite new users to the chat
    """

    can_post_messages: Optional[bool] = field(
        default=None, metadata={"ac_type": [bool], "ac_name": "can_post_messages"})
    """*Optional*. *True*, if the administrator can post in the channel; channels only
    """

    can_edit_messages: Optional[bool] = field(
        default=None, metadata={"ac_type": [bool], "ac_name": "can_edit_messages"})
    """*Optional*. *True*, if the administrator can edit messages of other users and can pin messages; channels only
    """

    can_pin_messages: Optional[bool] = field(
        default=None, metadata={"ac_type": [bool], "ac_name": "can_pin_messages"})
    """*Optional*. *True*, if the user is allowed to pin messages; groups and supergroups only
    """

    custom_title: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "custom_title"})
    """*Optional*. Custom title for this user
    """
