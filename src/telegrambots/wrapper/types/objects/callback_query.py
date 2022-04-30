from dataclasses import dataclass, field
from typing import Optional

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject

from .user import User
from .message import Message


@dataclass(init=True, repr=True, slots=True)
class CallbackQuery(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object represents an incoming callback query from a callback button in an [inline keyboard](https://core.telegram.org/bots#inline-keyboards-and-on-the-fly-updating). If the button that originated the query was attached to a message sent by the bot, the field *message* will be present. If the button was attached to a message sent via the bot (in [inline mode](https://core.telegram.org/bots/api/#inline-mode)), the field *inline\\_message\\_id* will be present. Exactly one of the fields *data* or *game\\_short\\_name* will be present.

    More info at: https://core.telegram.org/bots/api/#callbackquery
    """

    # --- properties here ---
    id: str = field(metadata={"ac_type": [str], "ac_name": "id"})
    """Unique identifier for this query
    """

    from_user: User = field(metadata={"ac_type": [User], "ac_name": "from"})
    """Sender
    """

    chat_instance: str = field(metadata={"ac_type": [str], "ac_name": "chat_instance"})
    """Global identifier, uniquely corresponding to the chat to which the message with the callback button was sent. Useful for high scores in [games](https://core.telegram.org/bots/api/#games).
    """

    message: Optional[Message] = field(
        default=None, metadata={"ac_type": [Message], "ac_name": "message"}
    )
    """*Optional*. Message with the callback button that originated the query. Note that message content and message date will not be available if the message is too old
    """

    inline_message_id: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "inline_message_id"}
    )
    """*Optional*. Identifier of the message sent via the bot in inline mode, that originated the query.
    """

    data: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "data"}
    )
    """*Optional*. Data associated with the callback button. Be aware that a bad client can send arbitrary data in this field.
    """

    game_short_name: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "game_short_name"}
    )
    """*Optional*. Short name of a [Game](https://core.telegram.org/bots/api/#games) to be returned, serves as the unique identifier for the game
    """
