from dataclasses import dataclass, field

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject


@dataclass(init=True, repr=True, slots=True)
class PassportFile(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object represents a file uploaded to Telegram Passport. Currently all Telegram Passport files are in JPEG format when decrypted and don't exceed 10MB.

    More info at: https://core.telegram.org/bots/api/#passportfile
    """

    # --- properties here ---
    file_id: str = field(metadata={"ac_type": [str], "ac_name": "file_id"})
    """Identifier for this file, which can be used to download or reuse the file
    """

    file_unique_id: str = field(
        metadata={"ac_type": [str], "ac_name": "file_unique_id"}
    )
    """Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.
    """

    file_size: int = field(metadata={"ac_type": [int], "ac_name": "file_size"})
    """File size in bytes
    """

    file_date: int = field(metadata={"ac_type": [int], "ac_name": "file_date"})
    """Unix time when the file was uploaded
    """
