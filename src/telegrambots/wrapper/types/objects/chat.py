from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Literal, Optional

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject

from .chat_permissions import ChatPermissions
from .chat_location import ChatLocation
from .chat_photo import ChatPhoto

if TYPE_CHECKING:
    from .message import Message


@dataclass(init=True, repr=True, slots=True)
class Chat(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object represents a chat.

    More info at: https://core.telegram.org/bots/api/#chat
    """

    # --- properties here ---
    id: int = field(metadata={"ac_type": [int], "ac_name": "id"})
    """Unique identifier for this chat. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
    """

    type: Literal["private", "group", "supergroup", "channel"] = field(
        metadata={"ac_type": [str], "ac_name": "type"}
    )
    """Type of chat, can be either “private”, “group”, “supergroup” or “channel”
    """

    title: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "title"}
    )
    """*Optional*. Title, for supergroups, channels and group chats
    """

    username: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "username"}
    )
    """*Optional*. Username, for private chats, supergroups and channels if available
    """

    first_name: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "first_name"}
    )
    """*Optional*. First name of the other party in a private chat
    """

    last_name: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "last_name"}
    )
    """*Optional*. Last name of the other party in a private chat
    """

    photo: Optional[ChatPhoto] = field(
        default=None, metadata={"ac_type": [ChatPhoto], "ac_name": "photo"}
    )
    """*Optional*. Chat photo. Returned only in [getChat](https://core.telegram.org/bots/api/#getchat).
    """

    bio: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "bio"}
    )
    """*Optional*. Bio of the other party in a private chat. Returned only in [getChat](https://core.telegram.org/bots/api/#getchat).
    """

    has_private_forwards: Optional[bool] = field(
        default=None, metadata={"ac_type": [bool], "ac_name": "has_private_forwards"}
    )
    """*Optional*. True, if privacy settings of the other party in the private chat allows to use `tg://user?id=<user_id>` links only in chats with the user. Returned only in [getChat](https://core.telegram.org/bots/api/#getchat).
    """

    description: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "description"}
    )
    """*Optional*. Description, for groups, supergroups and channel chats. Returned only in [getChat](https://core.telegram.org/bots/api/#getchat).
    """

    invite_link: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "invite_link"}
    )
    """*Optional*. Primary invite link, for groups, supergroups and channel chats. Returned only in [getChat](https://core.telegram.org/bots/api/#getchat).
    """

    pinned_message: Optional["Message"] = field(
        default=None, metadata={"ac_type": ["Message"], "ac_name": "pinned_message"}
    )
    """*Optional*. The most recent pinned message (by sending date). Returned only in [getChat](https://core.telegram.org/bots/api/#getchat).
    """

    permissions: Optional[ChatPermissions] = field(
        default=None, metadata={"ac_type": [ChatPermissions], "ac_name": "permissions"}
    )
    """*Optional*. Default chat member permissions, for groups and supergroups. Returned only in [getChat](https://core.telegram.org/bots/api/#getchat).
    """

    slow_mode_delay: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "slow_mode_delay"}
    )
    """*Optional*. For supergroups, the minimum allowed delay between consecutive messages sent by each unpriviledged user; in seconds. Returned only in [getChat](https://core.telegram.org/bots/api/#getchat).
    """

    message_auto_delete_time: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "message_auto_delete_time"}
    )
    """*Optional*. The time after which all messages sent to the chat will be automatically deleted; in seconds. Returned only in [getChat](https://core.telegram.org/bots/api/#getchat).
    """

    has_protected_content: Optional[bool] = field(
        default=None, metadata={"ac_type": [bool], "ac_name": "has_protected_content"}
    )
    """*Optional*. True, if messages from the chat can't be forwarded to other chats. Returned only in [getChat](https://core.telegram.org/bots/api/#getchat).
    """

    sticker_set_name: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "sticker_set_name"}
    )
    """*Optional*. For supergroups, name of group sticker set. Returned only in [getChat](https://core.telegram.org/bots/api/#getchat).
    """

    can_set_sticker_set: Optional[bool] = field(
        default=None, metadata={"ac_type": [bool], "ac_name": "can_set_sticker_set"}
    )
    """*Optional*. *True*, if the bot can change the group sticker set. Returned only in [getChat](https://core.telegram.org/bots/api/#getchat).
    """

    linked_chat_id: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "linked_chat_id"}
    )
    """*Optional*. Unique identifier for the linked chat, i.e. the discussion group identifier for a channel and vice versa; for supergroups and channel chats. This identifier may be greater than 32 bits and some programming languages may have difficulty/silent defects in interpreting it. But it is smaller than 52 bits, so a signed 64 bit integer or double-precision float type are safe for storing this identifier. Returned only in [getChat](https://core.telegram.org/bots/api/#getchat).
    """

    location: Optional[ChatLocation] = field(
        default=None, metadata={"ac_type": [ChatLocation], "ac_name": "location"}
    )
    """*Optional*. For supergroups, the location to which the supergroup is connected. Returned only in [getChat](https://core.telegram.org/bots/api/#getchat).
    """
