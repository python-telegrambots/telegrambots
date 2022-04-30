from dataclasses import dataclass, field
from typing import Any, Optional

from ..api_method import TelegramBotsMethod
from ..api_result import TelegramBotsApiResult
from ..objects.message import Message


@dataclass(init=True, repr=True, slots=True)
class SetGameScore(TelegramBotsMethod[TelegramBotsApiResult[Message | bool]]):
    # --- description here ---
    """Use this method to set the score of the specified user in a game message. On success, if the message is not an inline message, the [Message](https://core.telegram.org/bots/api/#message) is returned, otherwise *True* is returned. Returns an error, if the new score is not greater than the user's current score in the chat and *force* is *False*.
    
    More info at: https://core.telegram.org/bots/api/#setgamescore
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMethod.__init__(  # type: ignore
            obj, "setGameScore", [Message,bool])
        return obj


    # --- arguments here ---
    user_id: int = field(metadata={"ac_type": [int], "ac_name": "user_id"})
    """User identifier
    """

    score: int = field(metadata={"ac_type": [int], "ac_name": "score"})
    """New score, must be non-negative
    """

    force: Optional[bool] = field(default=None, metadata={"ac_type": [bool], "ac_name": "force"})
    """Pass *True*, if the high score is allowed to decrease. This can be useful when fixing mistakes or banning cheaters
    """

    disable_edit_message: Optional[bool] = field(default=None, metadata={"ac_type": [bool], "ac_name": "disable_edit_message"})
    """Pass *True*, if the game message should not be automatically edited to include the current scoreboard
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

