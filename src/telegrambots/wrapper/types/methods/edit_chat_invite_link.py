from dataclasses import dataclass, field
from typing import Any, Optional

from ..api_method import TelegramBotsMethod
from ..api_result import TelegramBotsApiResult
from ..objects.chat_invite_link import ChatInviteLink


@dataclass(init=True, repr=True, slots=True)
class EditChatInviteLink(TelegramBotsMethod[TelegramBotsApiResult[ChatInviteLink]]):
    # --- description here ---
    """Use this method to edit a non-primary invite link created by the bot. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Returns the edited invite link as a [ChatInviteLink](https://core.telegram.org/bots/api/#chatinvitelink) object.
    
    More info at: https://core.telegram.org/bots/api/#editchatinvitelink
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMethod.__init__(  # type: ignore
            obj, "editChatInviteLink", [ChatInviteLink])
        return obj


    # --- arguments here ---
    chat_id: int | str = field(metadata={"ac_type": [int, str], "ac_name": "chat_id"})
    """Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
    """

    invite_link: str = field(metadata={"ac_type": [str], "ac_name": "invite_link"})
    """The invite link to edit
    """

    name: Optional[str] = field(default=None, metadata={"ac_type": [str], "ac_name": "name"})
    """Invite link name; 0-32 characters
    """

    expire_date: Optional[int] = field(default=None, metadata={"ac_type": [int], "ac_name": "expire_date"})
    """Point in time (Unix timestamp) when the link will expire
    """

    member_limit: Optional[int] = field(default=None, metadata={"ac_type": [int], "ac_name": "member_limit"})
    """Maximum number of users that can be members of the chat simultaneously after joining the chat via this invite link; 1-99999
    """

    creates_join_request: Optional[bool] = field(default=None, metadata={"ac_type": [bool], "ac_name": "creates_join_request"})
    """*True*, if users joining the chat via the link need to be approved by chat administrators. If *True*, *member\\_limit* can't be specified
    """

