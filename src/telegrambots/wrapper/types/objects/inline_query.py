from dataclasses import dataclass, field
from typing import Literal, Optional

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject

from .user import User
from .location import Location


@dataclass(init=True, repr=True, slots=True)
class InlineQuery(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object represents an incoming inline query. When the user sends an empty query, your bot could return some default or trending results.

    More info at: https://core.telegram.org/bots/api/#inlinequery
    """

    # --- properties here ---
    id: str = field(metadata={"ac_type": [str], "ac_name": "id"})
    """Unique identifier for this query
    """

    from_user: User = field(metadata={"ac_type": [User], "ac_name": "from"})
    """Sender
    """

    query: str = field(metadata={"ac_type": [str], "ac_name": "query"})
    """Text of the query (up to 256 characters)
    """

    offset: str = field(metadata={"ac_type": [str], "ac_name": "offset"})
    """Offset of the results to be returned, can be controlled by the bot
    """

    chat_type: Optional[
        Literal["sender", "private", "group", "supergroup", "channel"]
    ] = field(default=None, metadata={"ac_type": [str], "ac_name": "chat_type"})
    """*Optional*. Type of the chat, from which the inline query was sent. Can be either “sender” for a private chat with the inline query sender, “private”, “group”, “supergroup”, or “channel”. The chat type should be always known for requests sent from official clients and most third-party clients, unless the request was sent from a secret chat
    """

    location: Optional[Location] = field(
        default=None, metadata={"ac_type": [Location], "ac_name": "location"}
    )
    """*Optional*. Sender location, only for bots that request user location
    """
