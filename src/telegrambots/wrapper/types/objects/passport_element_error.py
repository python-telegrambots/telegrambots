import abc
import dataclasses

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject


@dataclasses.dataclass(init=True, repr=True, slots=True)
class PassportElementError(abc.ABC, TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object represents an error in the Telegram Passport element which was submitted that should be resolved by the user. It should be one of:

    * [PassportElementErrorDataField](https://core.telegram.org/bots/api/#passportelementerrordatafield)
    * [PassportElementErrorFrontSide](https://core.telegram.org/bots/api/#passportelementerrorfrontside)
    * [PassportElementErrorReverseSide](https://core.telegram.org/bots/api/#passportelementerrorreverseside)
    * [PassportElementErrorSelfie](https://core.telegram.org/bots/api/#passportelementerrorselfie)
    * [PassportElementErrorFile](https://core.telegram.org/bots/api/#passportelementerrorfile)
    * [PassportElementErrorFiles](https://core.telegram.org/bots/api/#passportelementerrorfiles)
    * [PassportElementErrorTranslationFile](https://core.telegram.org/bots/api/#passportelementerrortranslationfile)
    * [PassportElementErrorTranslationFiles](https://core.telegram.org/bots/api/#passportelementerrortranslationfiles)
    * [PassportElementErrorUnspecified](https://core.telegram.org/bots/api/#passportelementerrorunspecified)

    More info at: https://core.telegram.org/bots/api/#passportelementerror
    """

    _source: str = dataclasses.field(
        init=False,
        repr=True,
        default="unspecified",
        metadata={"ac_type": [str], "ac_name": "source"},
    )

    @property
    def source(self) -> str:
        raise NotImplementedError()
