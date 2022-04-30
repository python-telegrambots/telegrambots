from dataclasses import dataclass, field
from typing import Any, Optional

from ..api_method import TelegramBotsMethod
from ..api_result import TelegramBotsApiResult



@dataclass(init=True, repr=True, slots=True)
class PromoteChatMember(TelegramBotsMethod[TelegramBotsApiResult[bool]]):
    # --- description here ---
    """Use this method to promote or demote a user in a supergroup or a channel. The bot must be an administrator in the chat for this to work and must have the appropriate administrator rights. Pass *False* for all boolean parameters to demote a user. Returns *True* on success.
    
    More info at: https://core.telegram.org/bots/api/#promotechatmember
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMethod.__init__(  # type: ignore
            obj, "promoteChatMember", [bool])
        return obj


    # --- arguments here ---
    chat_id: int | str = field(metadata={"ac_type": [int, str], "ac_name": "chat_id"})
    """Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
    """

    user_id: int = field(metadata={"ac_type": [int], "ac_name": "user_id"})
    """Unique identifier of the target user
    """

    is_anonymous: Optional[bool] = field(default=None, metadata={"ac_type": [bool], "ac_name": "is_anonymous"})
    """Pass *True*, if the administrator's presence in the chat is hidden
    """

    can_manage_chat: Optional[bool] = field(default=None, metadata={"ac_type": [bool], "ac_name": "can_manage_chat"})
    """Pass *True*, if the administrator can access the chat event log, chat statistics, message statistics in channels, see channel members, see anonymous administrators in supergroups and ignore slow mode. Implied by any other administrator privilege
    """

    can_post_messages: Optional[bool] = field(default=None, metadata={"ac_type": [bool], "ac_name": "can_post_messages"})
    """Pass *True*, if the administrator can create channel posts, channels only
    """

    can_edit_messages: Optional[bool] = field(default=None, metadata={"ac_type": [bool], "ac_name": "can_edit_messages"})
    """Pass *True*, if the administrator can edit messages of other users and can pin messages, channels only
    """

    can_delete_messages: Optional[bool] = field(default=None, metadata={"ac_type": [bool], "ac_name": "can_delete_messages"})
    """Pass *True*, if the administrator can delete messages of other users
    """

    can_manage_video_chats: Optional[bool] = field(default=None, metadata={"ac_type": [bool], "ac_name": "can_manage_video_chats"})
    """Pass *True*, if the administrator can manage video chats
    """

    can_restrict_members: Optional[bool] = field(default=None, metadata={"ac_type": [bool], "ac_name": "can_restrict_members"})
    """Pass *True*, if the administrator can restrict, ban or unban chat members
    """

    can_promote_members: Optional[bool] = field(default=None, metadata={"ac_type": [bool], "ac_name": "can_promote_members"})
    """Pass *True*, if the administrator can add new administrators with a subset of their own privileges or demote administrators that he has promoted, directly or indirectly (promoted by administrators that were appointed by him)
    """

    can_change_info: Optional[bool] = field(default=None, metadata={"ac_type": [bool], "ac_name": "can_change_info"})
    """Pass *True*, if the administrator can change chat title, photo and other settings
    """

    can_invite_users: Optional[bool] = field(default=None, metadata={"ac_type": [bool], "ac_name": "can_invite_users"})
    """Pass *True*, if the administrator can invite new users to the chat
    """

    can_pin_messages: Optional[bool] = field(default=None, metadata={"ac_type": [bool], "ac_name": "can_pin_messages"})
    """Pass *True*, if the administrator can pin messages, supergroups only
    """

