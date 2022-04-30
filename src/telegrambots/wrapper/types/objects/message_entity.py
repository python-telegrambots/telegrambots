from dataclasses import dataclass, field
from typing import Literal, Optional

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject

from .user import User


@dataclass(init=True, repr=True, slots=True)
class MessageEntity(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object represents one special entity in a text message. For example, hashtags, usernames, URLs, etc.

    More info at: https://core.telegram.org/bots/api/#messageentity
    """

    # --- properties here ---
    type: Literal[
        "mention",
        "hashtag",
        "cashtag",
        "bot_command",
        "url",
        "email",
        "phone_number",
        "bold",
        "italic",
        "underline",
        "strikethrough",
        "spoiler",
        "code",
        "pre",
        "text_link",
        "text_mention",
    ] = field(metadata={"ac_type": [str], "ac_name": "type"})
    """Type of the entity. Currently, can be “mention” (`@username`), “hashtag” (`#hashtag`), “cashtag” (`$USD`), “bot\\_command” (`/start@jobs_bot`), “url” (`https://telegram.org`), “email” (`do-not-reply@telegram.org`), “phone\\_number” (`+1-212-555-0123`), “bold” (**bold text**), “italic” (*italic text*), “underline” (underlined text), “strikethrough” (strikethrough text), “spoiler” (spoiler message), “code” (monowidth string), “pre” (monowidth block), “text\\_link” (for clickable text URLs), “text\\_mention” (for users [without usernames](https://telegram.org/blog/edit#new-mentions))
    """

    offset: int = field(metadata={"ac_type": [int], "ac_name": "offset"})
    """Offset in UTF-16 code units to the start of the entity
    """

    length: int = field(metadata={"ac_type": [int], "ac_name": "length"})
    """Length of the entity in UTF-16 code units
    """

    url: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "url"}
    )
    """*Optional*. For “text\\_link” only, url that will be opened after user taps on the text
    """

    user: Optional[User] = field(
        default=None, metadata={"ac_type": [User], "ac_name": "user"}
    )
    """*Optional*. For “text\\_mention” only, the mentioned user
    """

    language: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "language"}
    )
    """*Optional*. For “pre” only, the programming language of the entity text
    """
