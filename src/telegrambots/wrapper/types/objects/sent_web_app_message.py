from dataclasses import dataclass, field
from typing import Optional

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject


@dataclass(init=True, repr=True, slots=True)
class SentWebAppMessage(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """Contains information about an inline message sent by a [Web App](https://core.telegram.org/bots/webapps) on behalf of a user.

    More info at: https://core.telegram.org/bots/api/#sentwebappmessage
    """

    # --- properties here ---
    inline_message_id: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "inline_message_id"}
    )
    """*Optional*. Identifier of the sent inline message. Available only if there is an [inline keyboard](https://core.telegram.org/bots/api/#inlinekeyboardmarkup) attached to the message.
    """
