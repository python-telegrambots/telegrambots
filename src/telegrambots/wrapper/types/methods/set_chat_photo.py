from dataclasses import dataclass, field
from typing import Any

from ..api_multipart_method import TelegramBotsMultipartMethod
from ..api_result import TelegramBotsApiResult
from ..objects.input_file import InputFile


@dataclass(init=True, repr=True, slots=True)
class SetChatPhoto(TelegramBotsMultipartMethod[TelegramBotsApiResult[bool]]):
    # --- description here ---
    """Use this method to set a new profile photo for the chat. Photos can't be changed for private chats. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns *True* on success.
    
    More info at: https://core.telegram.org/bots/api/#setchatphoto
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMultipartMethod.__init__(  # type: ignore
            obj, "setChatPhoto", [bool])
        return obj


    # --- arguments here ---
    chat_id: int | str = field(metadata={"ac_type": [int, str], "ac_name": "chat_id"})
    """Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
    """

    photo: InputFile = field(metadata={"ac_type": [InputFile], "ac_name": "photo"})
    """New chat photo, uploaded using multipart/form-data
    """

