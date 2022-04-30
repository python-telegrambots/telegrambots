from dataclasses import dataclass, field
from typing import Literal, Optional

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject

from .message_entity import MessageEntity
from .poll_option import PollOption


@dataclass(init=True, repr=True, slots=True)
class Poll(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object contains information about a poll.

    More info at: https://core.telegram.org/bots/api/#poll
    """

    # --- properties here ---
    id: str = field(metadata={"ac_type": [str], "ac_name": "id"})
    """Unique poll identifier
    """

    question: str = field(metadata={"ac_type": [str], "ac_name": "question"})
    """Poll question, 1-300 characters
    """

    options: list[PollOption] = field(
        metadata={"ac_type": [PollOption], "ac_name": "options"}
    )
    """List of poll options
    """

    total_voter_count: int = field(
        metadata={"ac_type": [int], "ac_name": "total_voter_count"}
    )
    """Total number of users that voted in the poll
    """

    is_closed: bool = field(metadata={"ac_type": [bool], "ac_name": "is_closed"})
    """*True*, if the poll is closed
    """

    is_anonymous: bool = field(metadata={"ac_type": [bool], "ac_name": "is_anonymous"})
    """*True*, if the poll is anonymous
    """

    type: Literal["regular", "quiz"] = field(
        metadata={"ac_type": [str], "ac_name": "type"}
    )
    """Poll type, currently can be “regular” or “quiz”
    """

    allows_multiple_answers: bool = field(
        metadata={"ac_type": [bool], "ac_name": "allows_multiple_answers"}
    )
    """*True*, if the poll allows multiple answers
    """

    correct_option_id: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "correct_option_id"}
    )
    """*Optional*. 0-based identifier of the correct answer option. Available only for polls in the quiz mode, which are closed, or was sent (not forwarded) by the bot or to the private chat with the bot.
    """

    explanation: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "explanation"}
    )
    """*Optional*. Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll, 0-200 characters
    """

    explanation_entities: Optional[list[MessageEntity]] = field(
        default=None,
        metadata={"ac_type": [MessageEntity], "ac_name": "explanation_entities"},
    )
    """*Optional*. Special entities like usernames, URLs, bot commands, etc. that appear in the *explanation*
    """

    open_period: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "open_period"}
    )
    """*Optional*. Amount of time in seconds the poll will be active after creation
    """

    close_date: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "close_date"}
    )
    """*Optional*. Point in time (Unix timestamp) when the poll will be automatically closed
    """
