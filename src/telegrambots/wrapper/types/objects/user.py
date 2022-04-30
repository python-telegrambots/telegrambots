from dataclasses import dataclass, field
from typing import Optional

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject


@dataclass(init=True, repr=True, slots=True)
class User(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object represents a Telegram user or bot.

    More info at: https://core.telegram.org/bots/api/#user
    """

    # --- properties here ---
    id: int = field(metadata={"ac_type": [int], "ac_name": "id"})
    """Unique identifier for this user or bot. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a 64-bit integer or double-precision float type are safe for storing this identifier.
    """

    is_bot: bool = field(metadata={"ac_type": [bool], "ac_name": "is_bot"})
    """*True*, if this user is a bot
    """

    first_name: str = field(metadata={"ac_type": [str], "ac_name": "first_name"})
    """User's or bot's first name
    """

    last_name: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "last_name"}
    )
    """*Optional*. User's or bot's last name
    """

    username: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "username"}
    )
    """*Optional*. User's or bot's username
    """

    language_code: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "language_code"}
    )
    """*Optional*. [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag) of the user's language
    """

    can_join_groups: Optional[bool] = field(
        default=None, metadata={"ac_type": [bool], "ac_name": "can_join_groups"}
    )
    """*Optional*. *True*, if the bot can be invited to groups. Returned only in [getMe](https://core.telegram.org/bots/api/#getme).
    """

    can_read_all_group_messages: Optional[bool] = field(
        default=None,
        metadata={"ac_type": [bool], "ac_name": "can_read_all_group_messages"},
    )
    """*Optional*. *True*, if [privacy mode](https://core.telegram.org/bots#privacy-mode) is disabled for the bot. Returned only in [getMe](https://core.telegram.org/bots/api/#getme).
    """

    supports_inline_queries: Optional[bool] = field(
        default=None, metadata={"ac_type": [bool], "ac_name": "supports_inline_queries"}
    )
    """*Optional*. *True*, if the bot supports inline queries. Returned only in [getMe](https://core.telegram.org/bots/api/#getme).
    """
