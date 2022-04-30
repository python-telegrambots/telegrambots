from dataclasses import dataclass, field
from typing import Optional

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject


@dataclass(init=True, repr=True, slots=True)
class ChatPermissions(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """Describes actions that a non-administrator user is allowed to take in a chat.

    More info at: https://core.telegram.org/bots/api/#chatpermissions
    """

    # --- properties here ---
    can_send_messages: Optional[bool] = field(
        default=None, metadata={"ac_type": [bool], "ac_name": "can_send_messages"}
    )
    """*Optional*. *True*, if the user is allowed to send text messages, contacts, locations and venues
    """

    can_send_media_messages: Optional[bool] = field(
        default=None, metadata={"ac_type": [bool], "ac_name": "can_send_media_messages"}
    )
    """*Optional*. *True*, if the user is allowed to send audios, documents, photos, videos, video notes and voice notes, implies can\\_send\\_messages
    """

    can_send_polls: Optional[bool] = field(
        default=None, metadata={"ac_type": [bool], "ac_name": "can_send_polls"}
    )
    """*Optional*. *True*, if the user is allowed to send polls, implies can\\_send\\_messages
    """

    can_send_other_messages: Optional[bool] = field(
        default=None, metadata={"ac_type": [bool], "ac_name": "can_send_other_messages"}
    )
    """*Optional*. *True*, if the user is allowed to send animations, games, stickers and use inline bots, implies can\\_send\\_media\\_messages
    """

    can_add_web_page_previews: Optional[bool] = field(
        default=None,
        metadata={"ac_type": [bool], "ac_name": "can_add_web_page_previews"},
    )
    """*Optional*. *True*, if the user is allowed to add web page previews to their messages, implies can\\_send\\_media\\_messages
    """

    can_change_info: Optional[bool] = field(
        default=None, metadata={"ac_type": [bool], "ac_name": "can_change_info"}
    )
    """*Optional*. *True*, if the user is allowed to change the chat title, photo and other settings. Ignored in public supergroups
    """

    can_invite_users: Optional[bool] = field(
        default=None, metadata={"ac_type": [bool], "ac_name": "can_invite_users"}
    )
    """*Optional*. *True*, if the user is allowed to invite new users to the chat
    """

    can_pin_messages: Optional[bool] = field(
        default=None, metadata={"ac_type": [bool], "ac_name": "can_pin_messages"}
    )
    """*Optional*. *True*, if the user is allowed to pin messages. Ignored in public supergroups
    """
