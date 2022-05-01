from dataclasses import dataclass, field
from typing import Any, Optional

from ..api_method import TelegramBotsMethodNoOutput


@dataclass(init=True, repr=True, slots=True)
class SetChatDescription(TelegramBotsMethodNoOutput):
    # --- description here ---
    """Use this method to change the description of a group, a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns *True* on success.

    More info at: https://core.telegram.org/bots/api/#setchatdescription
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMethodNoOutput.__init__(obj, "setChatDescription")  # type: ignore
        return obj

    # --- arguments here ---
    chat_id: int | str = field(metadata={"ac_type": [int, str], "ac_name": "chat_id"})
    """Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
    """

    description: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "description"}
    )
    """New chat description, 0-255 characters
    """
