from dataclasses import dataclass, field
from typing import Optional

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject

from .photo_size import PhotoSize
from .animation import Animation
from .message_entity import MessageEntity


@dataclass(init=True, repr=True, slots=True)
class Game(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object represents a game. Use BotFather to create and edit games, their short names will act as unique identifiers.

    More info at: https://core.telegram.org/bots/api/#game
    """

    # --- properties here ---
    title: str = field(metadata={"ac_type": [str], "ac_name": "title"})
    """Title of the game
    """

    description: str = field(metadata={"ac_type": [str], "ac_name": "description"})
    """Description of the game
    """

    photo: list[PhotoSize] = field(
        metadata={"ac_type": [PhotoSize], "ac_name": "photo"}
    )
    """Photo that will be displayed in the game message in chats.
    """

    text: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "text"}
    )
    """*Optional*. Brief description of the game or high scores included in the game message. Can be automatically edited to include current high scores for the game when the bot calls [setGameScore](https://core.telegram.org/bots/api/#setgamescore), or manually edited using [editMessageText](https://core.telegram.org/bots/api/#editmessagetext). 0-4096 characters.
    """

    text_entities: Optional[list[MessageEntity]] = field(
        default=None, metadata={"ac_type": [MessageEntity], "ac_name": "text_entities"}
    )
    """*Optional*. Special entities that appear in *text*, such as usernames, URLs, bot commands, etc.
    """

    animation: Optional[Animation] = field(
        default=None, metadata={"ac_type": [Animation], "ac_name": "animation"}
    )
    """*Optional*. Animation that will be displayed in the game message in chats. Upload via [BotFather](https://t.me/botfather)
    """
