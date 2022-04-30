import abc
import dataclasses
from typing import Any

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject


@dataclasses.dataclass(init=True, repr=True, slots=True)
class ChatMember(abc.ABC, TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object contains information about one member of a chat. Currently, the following 6 types of chat members are supported:

    * [ChatMemberOwner](https://core.telegram.org/bots/api/#chatmemberowner)
    * [ChatMemberAdministrator](https://core.telegram.org/bots/api/#chatmemberadministrator)
    * [ChatMemberMember](https://core.telegram.org/bots/api/#chatmembermember)
    * [ChatMemberRestricted](https://core.telegram.org/bots/api/#chatmemberrestricted)
    * [ChatMemberLeft](https://core.telegram.org/bots/api/#chatmemberleft)
    * [ChatMemberBanned](https://core.telegram.org/bots/api/#chatmemberbanned)

    More info at: https://core.telegram.org/bots/api/#chatmember
    """

    @classmethod
    def deserialize(
        cls,
        data: dict[str, Any] | list[Any],
        custom_types: dict[str, list[type[Any]]] | None = None,
        client: Any = None,
    ) -> "ChatMember":

        from .chat_member_administrator import ChatMemberAdministrator
        from .chat_member_banned import ChatMemberBanned
        from .chat_member_left import ChatMemberLeft
        from .chat_member_member import ChatMemberMember
        from .chat_member_owner import ChatMemberOwner
        from .chat_member_restricted import ChatMemberRestricted

        if not isinstance(data, dict):
            raise ValueError(f"Expected dict, got {type(data)}")

        if "status" not in data:
            raise ValueError('Expected "status" in data')

        def deserialize_to(status: str) -> type[ChatMember]:
            match (status):
                case "administrator":
                    return ChatMemberAdministrator
                case "kicked":
                    return ChatMemberBanned
                case "left":
                    return ChatMemberLeft
                case "member":
                    return ChatMemberMember
                case "creator":
                    return ChatMemberOwner
                case "restricted":
                    return ChatMemberRestricted
                case _:
                    raise ValueError(f"Unknown chat member status: {status}")

        return TelegramBotsObject.deserialize_to(
            deserialize_to(data["status"]), data, custom_types, client
        )
