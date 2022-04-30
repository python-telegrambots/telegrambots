from dataclasses import dataclass, field

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject


@dataclass(init=True, repr=True, slots=True)
class BotCommand(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object represents a bot command.

    More info at: https://core.telegram.org/bots/api/#botcommand
    """

    # --- properties here ---
    command: str = field(metadata={"ac_type": [str], "ac_name": "command"})
    """Text of the command; 1-32 characters. Can contain only lowercase English letters, digits and underscores.
    """

    description: str = field(metadata={"ac_type": [str], "ac_name": "description"})
    """Description of the command; 1-256 characters.
    """
