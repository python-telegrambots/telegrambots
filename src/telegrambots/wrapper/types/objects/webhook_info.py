from dataclasses import dataclass, field
from typing import Optional

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject


@dataclass(init=True, repr=True, slots=True)
class WebhookInfo(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """Contains information about the current status of a webhook.

    More info at: https://core.telegram.org/bots/api/#webhookinfo
    """

    # --- properties here ---
    url: str = field(metadata={"ac_type": [str], "ac_name": "url"})
    """Webhook URL, may be empty if webhook is not set up
    """

    has_custom_certificate: bool = field(
        metadata={"ac_type": [bool], "ac_name": "has_custom_certificate"}
    )
    """*True*, if a custom certificate was provided for webhook certificate checks
    """

    pending_update_count: int = field(
        metadata={"ac_type": [int], "ac_name": "pending_update_count"}
    )
    """Number of updates awaiting delivery
    """

    ip_address: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "ip_address"}
    )
    """*Optional*. Currently used webhook IP address
    """

    last_error_date: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "last_error_date"}
    )
    """*Optional*. Unix time for the most recent error that happened when trying to deliver an update via webhook
    """

    last_error_message: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "last_error_message"}
    )
    """*Optional*. Error message in human-readable format for the most recent error that happened when trying to deliver an update via webhook
    """

    last_synchronization_error_date: Optional[int] = field(
        default=None,
        metadata={"ac_type": [int], "ac_name": "last_synchronization_error_date"},
    )
    """*Optional*. Unix time of the most recent error that happened when trying to synchronize available updates with Telegram datacenters
    """

    max_connections: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "max_connections"}
    )
    """*Optional*. Maximum allowed number of simultaneous HTTPS connections to the webhook for update delivery
    """

    allowed_updates: Optional[list[str]] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "allowed_updates"}
    )
    """*Optional*. A list of update types the bot is subscribed to. Defaults to all update types except *chat\\_member*
    """
