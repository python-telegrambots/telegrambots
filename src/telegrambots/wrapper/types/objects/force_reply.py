from dataclasses import dataclass, field
from typing import Optional

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject


@dataclass(init=True, repr=True, slots=True)
class ForceReply(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """Upon receiving a message with this object, Telegram clients will display a reply interface to the user (act as if the user has selected the bot's message and tapped 'Reply'). This can be extremely useful if you want to create user-friendly step-by-step interfaces without having to sacrifice [privacy mode](https://core.telegram.org/bots#privacy-mode).

    More info at: https://core.telegram.org/bots/api/#forcereply
    """

    # --- properties here ---
    force_reply: bool = field(
        default=True, init=False, metadata={"ac_type": [bool], "ac_name": "force_reply"}
    )
    """Shows reply interface to the user, as if they manually selected the bot's message and tapped 'Reply'
    """

    input_field_placeholder: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "input_field_placeholder"}
    )
    """*Optional*. The placeholder to be shown in the input field when the reply is active; 1-64 characters
    """

    selective: Optional[bool] = field(
        default=None, metadata={"ac_type": [bool], "ac_name": "selective"}
    )
    """*Optional*. Use this parameter if you want to force reply from specific users only. Targets: 1) users that are @mentioned in the *text* of the [Message](https://core.telegram.org/bots/api/#message) object; 2) if the bot's message is a reply (has *reply\\_to\\_message\\_id*), sender of the original message.
    """
