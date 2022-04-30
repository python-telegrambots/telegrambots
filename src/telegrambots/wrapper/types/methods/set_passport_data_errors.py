from dataclasses import dataclass, field
from typing import Any

from ..api_method import TelegramBotsMethod
from ..api_result import TelegramBotsApiResult
from ..objects.passport_element_error import PassportElementError


@dataclass(init=True, repr=True, slots=True)
class SetPassportDataErrors(TelegramBotsMethod[TelegramBotsApiResult[bool]]):
    # --- description here ---
    """Informs a user that some of the Telegram Passport elements they provided contains errors. The user will not be able to re-submit their Passport to you until the errors are fixed (the contents of the field for which you returned the error must change). Returns *True* on success.
    
    Use this if the data submitted by the user doesn't satisfy the standards your service requires for any reason. For example, if a birthday date seems invalid, a submitted document is blurry, a scan shows evidence of tampering, etc. Supply some details in the error message to make sure the user knows how to correct the issues.
    
    More info at: https://core.telegram.org/bots/api/#setpassportdataerrors
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMethod.__init__(  # type: ignore
            obj, "setPassportDataErrors", [bool])
        return obj


    # --- arguments here ---
    user_id: int = field(metadata={"ac_type": [int], "ac_name": "user_id"})
    """User identifier
    """

    errors: list[PassportElementError] = field(metadata={"ac_type": [PassportElementError], "ac_name": "errors"})
    """A JSON-serialized array describing the errors
    """

