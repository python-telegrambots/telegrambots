from dataclasses import dataclass, field

from .chat_member import ChatMember
from .user import User


@dataclass(init=True, repr=True, slots=True)
class ChatMemberRestricted(ChatMember):
    # --- description here ---
    """Represents a [chat member](https://core.telegram.org/bots/api/#chatmember) that is under certain restrictions in the chat. Supergroups only.

    More info at: https://core.telegram.org/bots/api/#chatmemberrestricted
    """

    # --- properties here ---
    status: str = field(metadata={"ac_type": [str], "ac_name": "status"})
    """The member's status in the chat, always “restricted”
    """

    user: User = field(metadata={"ac_type": [User], "ac_name": "user"})
    """Information about the user
    """

    is_member: bool = field(
        metadata={"ac_type": [bool], "ac_name": "is_member"})
    """*True*, if the user is a member of the chat at the moment of the request
    """

    can_change_info: bool = field(
        metadata={"ac_type": [bool], "ac_name": "can_change_info"})
    """*True*, if the user is allowed to change the chat title, photo and other settings
    """

    can_invite_users: bool = field(
        metadata={"ac_type": [bool], "ac_name": "can_invite_users"})
    """*True*, if the user is allowed to invite new users to the chat
    """

    can_pin_messages: bool = field(
        metadata={"ac_type": [bool], "ac_name": "can_pin_messages"})
    """*True*, if the user is allowed to pin messages
    """

    can_send_messages: bool = field(
        metadata={"ac_type": [bool], "ac_name": "can_send_messages"})
    """*True*, if the user is allowed to send text messages, contacts, locations and venues
    """

    can_send_media_messages: bool = field(
        metadata={"ac_type": [bool], "ac_name": "can_send_media_messages"})
    """*True*, if the user is allowed to send audios, documents, photos, videos, video notes and voice notes
    """

    can_send_polls: bool = field(
        metadata={"ac_type": [bool], "ac_name": "can_send_polls"})
    """*True*, if the user is allowed to send polls
    """

    can_send_other_messages: bool = field(
        metadata={"ac_type": [bool], "ac_name": "can_send_other_messages"})
    """*True*, if the user is allowed to send animations, games, stickers and use inline bots
    """

    can_add_web_page_previews: bool = field(
        metadata={"ac_type": [bool], "ac_name": "can_add_web_page_previews"})
    """*True*, if the user is allowed to add web page previews to their messages
    """

    until_date: int = field(
        metadata={"ac_type": [int], "ac_name": "until_date"})
    """Date when restrictions will be lifted for this user; unix time. If 0, then the user is restricted forever
    """
