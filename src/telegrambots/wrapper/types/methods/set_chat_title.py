from dataclasses import dataclass, field
from typing import Any

from ..api_method import TelegramBotsMethodNoOutput


@dataclass(init=True, repr=True, slots=True)
class SetChatTitle(TelegramBotsMethodNoOutput):
    # --- description here ---
    """Use this method to change the title of a chat. Titles can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns *True* on success.

    More info at: https://core.telegram.org/bots/api/#setchattitle
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMethod.__init__(obj, "setChatTitle", [bool])  # type: ignore
        return obj

    # --- arguments here ---
    chat_id: int | str = field(metadata={"ac_type": [int, str], "ac_name": "chat_id"})
    """Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
    """

    title: str = field(metadata={"ac_type": [str], "ac_name": "title"})
    """New chat title, 1-255 characters
    """
