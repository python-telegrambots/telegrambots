from dataclasses import dataclass, field
from typing import Any

from ..api_method import TelegramBotsMethod
from ..api_result import TelegramBotsApiResult
from ..objects.chat_invite_link import ChatInviteLink


@dataclass(init=True, repr=True, slots=True)
class RevokeChatInviteLink(TelegramBotsMethod[TelegramBotsApiResult[ChatInviteLink]]):
    # --- description here ---
    """Use this method to revoke an invite link created by the bot. If the primary link is revoked, a new link is automatically generated. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the revoked invite link as [ChatInviteLink](https://core.telegram.org/bots/api/#chatinvitelink) object.
    
    More info at: https://core.telegram.org/bots/api/#revokechatinvitelink
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMethod.__init__(  # type: ignore
            obj, "revokeChatInviteLink", [ChatInviteLink])
        return obj


    # --- arguments here ---
    chat_id: int | str = field(metadata={"ac_type": [int, str], "ac_name": "chat_id"})
    """Unique identifier of the target chat or username of the target channel (in the format `@channelusername`)
    """

    invite_link: str = field(metadata={"ac_type": [str], "ac_name": "invite_link"})
    """The invite link to revoke
    """

