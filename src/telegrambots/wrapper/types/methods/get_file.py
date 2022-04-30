from dataclasses import dataclass, field
from typing import Any

from ..api_method import TelegramBotsMethod
from ..api_result import TelegramBotsApiResult
from ..objects.file import File


@dataclass(init=True, repr=True, slots=True)
class GetFile(TelegramBotsMethod[TelegramBotsApiResult[File]]):
    # --- description here ---
    """Use this method to get basic info about a file and prepare it for downloading. For the moment, bots can download files of up to 20MB in size. On success, a [File](https://core.telegram.org/bots/api/#file) object is returned. The file can then be downloaded via the link `https://api.telegram.org/file/bot<token>/<file_path>`, where `<file_path>` is taken from the response. It is guaranteed that the link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling [getFile](https://core.telegram.org/bots/api/#getfile) again.
    
    More info at: https://core.telegram.org/bots/api/#getfile
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMethod.__init__(  # type: ignore
            obj, "getFile", [File])
        return obj


    # --- arguments here ---
    file_id: str = field(metadata={"ac_type": [str], "ac_name": "file_id"})
    """File identifier to get info about
    """

