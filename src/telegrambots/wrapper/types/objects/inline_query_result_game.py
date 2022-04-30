from dataclasses import dataclass, field
from typing import Optional

from .inline_query_result import InlineQueryResult
from .inline_keyboard_markup import InlineKeyboardMarkup


@dataclass(init=True, repr=True, slots=True)
class InlineQueryResultGame(InlineQueryResult):
    # --- description here ---
    """Represents a [Game](https://core.telegram.org/bots/api/#games).

    More info at: https://core.telegram.org/bots/api/#inlinequeryresultgame
    """

    # --- properties here ---
    @property
    def type(self) -> str:
        self._type = 'game'
        return self._type

    id: str = field(metadata={"ac_type": [str], "ac_name": "id"})
    """Unique identifier for this result, 1-64 bytes
    """

    game_short_name: str = field(
        metadata={"ac_type": [str], "ac_name": "game_short_name"})
    """Short name of the game
    """

    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None, metadata={
                                                         "ac_type": [InlineKeyboardMarkup], "ac_name": "reply_markup"})
    """*Optional*. [Inline keyboard](https://core.telegram.org/bots#inline-keyboards-and-on-the-fly-updating) attached to the message
    """
