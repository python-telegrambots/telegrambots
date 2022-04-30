from dataclasses import dataclass, field
from typing import Any, Optional

from ..api_method import TelegramBotsMethod
from ..api_result import TelegramBotsApiResult
from ..objects.game_high_score import GameHighScore


@dataclass(init=True, repr=True, slots=True)
class GetGameHighScores(TelegramBotsMethod[TelegramBotsApiResult[list[GameHighScore]]]):
    # --- description here ---
    """Use this method to get data for high score tables. Will return the score of the specified user and several of their neighbors in a game. On success, returns an *Array* of [GameHighScore](https://core.telegram.org/bots/api/#gamehighscore) objects.
    
    This method will currently return scores for the target user, plus two of their closest neighbors on each side. Will also return the top three users if the user and his neighbors are not among them. Please note that this behavior is subject to change.
    
    More info at: https://core.telegram.org/bots/api/#getgamehighscores
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMethod.__init__(  # type: ignore
            obj, "getGameHighScores", [GameHighScore])
        return obj


    # --- arguments here ---
    user_id: int = field(metadata={"ac_type": [int], "ac_name": "user_id"})
    """Target user id
    """

    chat_id: Optional[int] = field(default=None, metadata={"ac_type": [int], "ac_name": "chat_id"})
    """Required if *inline\\_message\\_id* is not specified. Unique identifier for the target chat
    """

    message_id: Optional[int] = field(default=None, metadata={"ac_type": [int], "ac_name": "message_id"})
    """Required if *inline\\_message\\_id* is not specified. Identifier of the sent message
    """

    inline_message_id: Optional[str] = field(default=None, metadata={"ac_type": [str], "ac_name": "inline_message_id"})
    """Required if *chat\\_id* and *message\\_id* are not specified. Identifier of the inline message
    """

