from dataclasses import dataclass, field

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject

from .user import User


@dataclass(init=True, repr=True, slots=True)
class GameHighScore(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object represents one row of the high scores table for a game.

    More info at: https://core.telegram.org/bots/api/#gamehighscore
    """

    # --- properties here ---
    position: int = field(metadata={"ac_type": [int], "ac_name": "position"})
    """Position in high score table for the game
    """

    user: User = field(metadata={"ac_type": [User], "ac_name": "user"})
    """User
    """

    score: int = field(metadata={"ac_type": [int], "ac_name": "score"})
    """Score
    """
