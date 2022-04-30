from dataclasses import dataclass, field
from typing import Optional

from .input_media import InputMedia
from .message_entity import MessageEntity
from .input_file import InputFile


@dataclass(init=True, repr=True, slots=True)
class InputMediaAudio(InputMedia):
    # --- description here ---
    """Represents an audio file to be treated as music to be sent.

    More info at: https://core.telegram.org/bots/api/#inputmediaaudio
    """

    # --- properties here ---
    @property
    def type(self) -> str:
        self._type = 'audio'
        return self._type

    media: str = field(metadata={"ac_type": [str], "ac_name": "media"})
    """File to send. Pass a file\\_id to send a file that exists on the Telegram servers (recommended), pass an HTTP URL for Telegram to get a file from the Internet, or pass “attach://<file\\_attach\\_name>” to upload a new one using multipart/form-data under <file\\_attach\\_name> name. [More info on Sending Files »](https://core.telegram.org/bots/api/#sending-files)
    """

    thumb: Optional[InputFile | str] = field(
        default=None, metadata={"ac_type": [InputFile, str], "ac_name": "thumb"})
    """*Optional*. Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320. Ignored if the file is not uploaded using multipart/form-data. Thumbnails can't be reused and can be only uploaded as a new file, so you can pass “attach://<file\\_attach\\_name>” if the thumbnail was uploaded using multipart/form-data under <file\\_attach\\_name>. [More info on Sending Files »](https://core.telegram.org/bots/api/#sending-files)
    """

    caption: Optional[str] = field(default=None, metadata={
                                   "ac_type": [str], "ac_name": "caption"})
    """*Optional*. Caption of the audio to be sent, 0-1024 characters after entities parsing
    """

    parse_mode: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "parse_mode"})
    """*Optional*. Mode for parsing entities in the audio caption. See [formatting options](https://core.telegram.org/bots/api/#formatting-options) for more details.
    """

    caption_entities: Optional[list[MessageEntity]] = field(
        default=None, metadata={"ac_type": [MessageEntity], "ac_name": "caption_entities"})
    """*Optional*. List of special entities that appear in the caption, which can be specified instead of *parse\\_mode*
    """

    duration: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "duration"})
    """*Optional*. Duration of the audio in seconds
    """

    performer: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "performer"})
    """*Optional*. Performer of the audio
    """

    title: Optional[str] = field(default=None, metadata={
                                 "ac_type": [str], "ac_name": "title"})
    """*Optional*. Title of the audio
    """
