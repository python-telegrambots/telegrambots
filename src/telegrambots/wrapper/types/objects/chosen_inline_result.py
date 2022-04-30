from dataclasses import dataclass, field
from typing import Optional

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject

from .user import User
from .location import Location


@dataclass(init=True, repr=True, slots=True)
class ChosenInlineResult(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """Represents a [result](https://core.telegram.org/bots/api/#inlinequeryresult) of an inline query that was chosen by the user and sent to their chat partner.

    More info at: https://core.telegram.org/bots/api/#choseninlineresult
    """

    # --- properties here ---
    result_id: str = field(metadata={"ac_type": [str], "ac_name": "result_id"})
    """The unique identifier for the result that was chosen
    """

    from_user: User = field(metadata={"ac_type": [User], "ac_name": "from"})
    """The user that chose the result
    """

    query: str = field(metadata={"ac_type": [str], "ac_name": "query"})
    """The query that was used to obtain the result
    """

    location: Optional[Location] = field(
        default=None, metadata={"ac_type": [Location], "ac_name": "location"}
    )
    """*Optional*. Sender location, only for bots that require user location
    """

    inline_message_id: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "inline_message_id"}
    )
    """*Optional*. Identifier of the sent inline message. Available only if there is an [inline keyboard](https://core.telegram.org/bots/api/#inlinekeyboardmarkup) attached to the message. Will be also received in [callback queries](https://core.telegram.org/bots/api/#callbackquery) and can be used to [edit](https://core.telegram.org/bots/api/#updating-messages) the message.
    """
