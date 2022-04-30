import abc
import dataclasses

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject


@dataclasses.dataclass(init=True, repr=True, slots=True)
class InputMedia(abc.ABC, TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object represents the content of a media message to be sent. It should be one of

    * [InputMediaAnimation](https://core.telegram.org/bots/api/#inputmediaanimation)
    * [InputMediaDocument](https://core.telegram.org/bots/api/#inputmediadocument)
    * [InputMediaAudio](https://core.telegram.org/bots/api/#inputmediaaudio)
    * [InputMediaPhoto](https://core.telegram.org/bots/api/#inputmediaphoto)
    * [InputMediaVideo](https://core.telegram.org/bots/api/#inputmediavideo)

    More info at: https://core.telegram.org/bots/api/#inputmedia
    """

    _type: str = dataclasses.field(
        init=False, repr=True, metadata={"ac_type": [str], "ac_name": "type"}
    )

    @property
    def type(self) -> str:
        ...
