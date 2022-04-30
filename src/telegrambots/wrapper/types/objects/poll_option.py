from dataclasses import dataclass, field

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject


@dataclass(init=True, repr=True, slots=True)
class PollOption(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object contains information about one answer option in a poll.

    More info at: https://core.telegram.org/bots/api/#polloption
    """

    # --- properties here ---
    text: str = field(metadata={"ac_type": [str], "ac_name": "text"})
    """Option text, 1-100 characters
    """

    voter_count: int = field(metadata={"ac_type": [int], "ac_name": "voter_count"})
    """Number of users that voted for this option
    """
