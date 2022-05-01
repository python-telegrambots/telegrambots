from dataclasses import dataclass
from typing import Any

from ..api_method import TelegramBotsMethodNoOutput


@dataclass(init=True, repr=True, slots=True)
class LogOut(TelegramBotsMethodNoOutput):
    # --- description here ---
    """Use this method to log out from the cloud Bot API server before launching the bot locally. You **must** log out the bot before running it locally, otherwise there is no guarantee that the bot will receive updates. After a successful call, you can immediately log in on a local server, but will not be able to log in back to the cloud Bot API server for 10 minutes. Returns *True* on success. Requires no parameters.

    More info at: https://core.telegram.org/bots/api/#logout
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMethod.__init__(obj, "logOut", [bool])  # type: ignore
        return obj

    # --- arguments here ---
