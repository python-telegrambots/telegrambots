import abc
import dataclasses

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject


@dataclasses.dataclass(init=True, repr=True, slots=True)
class BotCommandScope(abc.ABC, TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object represents the scope to which bot commands are applied. Currently, the following 7 scopes are supported:

    * [BotCommandScopeDefault](https://core.telegram.org/bots/api/#botcommandscopedefault)
    * [BotCommandScopeAllPrivateChats](https://core.telegram.org/bots/api/#botcommandscopeallprivatechats)
    * [BotCommandScopeAllGroupChats](https://core.telegram.org/bots/api/#botcommandscopeallgroupchats)
    * [BotCommandScopeAllChatAdministrators](https://core.telegram.org/bots/api/#botcommandscopeallchatadministrators)
    * [BotCommandScopeChat](https://core.telegram.org/bots/api/#botcommandscopechat)
    * [BotCommandScopeChatAdministrators](https://core.telegram.org/bots/api/#botcommandscopechatadministrators)
    * [BotCommandScopeChatMember](https://core.telegram.org/bots/api/#botcommandscopechatmember)

    More info at: https://core.telegram.org/bots/api/#botcommandscope
    """

    _type: str = dataclasses.field(
        init=False,
        repr=True,
        default="default",
        metadata={"ac_type": [str], "ac_name": "type"},
    )

    @property
    def type(self) -> str:
        raise NotImplementedError()
