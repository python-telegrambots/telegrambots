from dataclasses import dataclass, field

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject

from .user import User


@dataclass(init=True, repr=True, slots=True)
class PollAnswer(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object represents an answer of a user in a non-anonymous poll.

    More info at: https://core.telegram.org/bots/api/#pollanswer
    """

    # --- properties here ---
    poll_id: str = field(metadata={"ac_type": [str], "ac_name": "poll_id"})
    """Unique poll identifier
    """

    user: User = field(metadata={"ac_type": [User], "ac_name": "user"})
    """The user, who changed the answer to the poll
    """

    option_ids: list[int] = field(metadata={"ac_type": [int], "ac_name": "option_ids"})
    """0-based identifiers of answer options, chosen by the user. May be empty if the user retracted their vote.
    """
