from dataclasses import dataclass, field
from typing import Optional

from .input_file import InputFile

from .input_media import InputMedia
from .message_entity import MessageEntity


@dataclass(init=True, repr=True, slots=True)
class InputMediaPhoto(InputMedia):
    # --- description here ---
    """Represents a photo to be sent.

    More info at: https://core.telegram.org/bots/api/#inputmediaphoto
    """

    # --- properties here ---
    @property
    def type(self) -> str:
        self._type = 'photo'
        return self._type

    media: str | InputFile = field(
        metadata={"ac_type": [str], "ac_name": "media"})
    """File to send. Pass a file\\_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file\\_attach\\_name>” to upload a new one using multipart/form-data under <file\\_attach\\_name> name. [More info on Sending Files »](https://core.telegram.org/bots/api/#sending-files)
    """

    caption: Optional[str] = field(default=None, metadata={
                                   "ac_type": [str], "ac_name": "caption"})
    """*Optional*. Caption of the photo to be sent, 0-1024 characters after entities parsing
    """

    parse_mode: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "parse_mode"})
    """*Optional*. Mode for parsing entities in the photo caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details.
    """

    caption_entities: Optional[list[MessageEntity]] = field(
        default=None, metadata={"ac_type": [MessageEntity], "ac_name": "caption_entities"})
    """*Optional*. List of special entities that appear in the caption, which can be specified instead of *parse\\_mode*
    """
