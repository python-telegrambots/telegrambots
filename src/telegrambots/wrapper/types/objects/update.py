from dataclasses import dataclass, field, fields
from typing import Any, Optional

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject

from .inline_query import InlineQuery
from .callback_query import CallbackQuery
from .shipping_query import ShippingQuery
from .pre_checkout_query import PreCheckoutQuery
from .poll import Poll
from .chat_join_request import ChatJoinRequest
from .message import Message
from .chat_member_updated import ChatMemberUpdated
from .chosen_inline_result import ChosenInlineResult
from .poll_answer import PollAnswer


@dataclass(init=True, repr=True, slots=True)
class Update(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This [object](https://core.telegram.org/bots/api/#available-types) represents an incoming update.
    At most **one** of the optional parameters can be present in any given update.

    More info at: https://core.telegram.org/bots/api/#update
    """

    # --- properties here ---
    _update_type: Optional[type[Any]] = field(
        default=None, init=False, metadata={"ac_type": [type], "ac_name": "update_type"}
    )

    update_id: int = field(metadata={"ac_type": [int], "ac_name": "update_id"})
    """The update's unique identifier. Update identifiers start from a certain positive number and increase sequentially. This ID becomes especially handy if you're using [Webhooks](https://core.telegram.org/bots/api/#setwebhook), since it allows you to ignore repeated updates or to restore the correct update sequence, should they get out of order. If there are no new updates for at least a week, then identifier of the next update will be chosen randomly instead of sequentially.
    """

    message: Optional[Message] = field(
        default=None, metadata={"ac_type": [Message], "ac_name": "message"}
    )
    """*Optional*. New incoming message of any kind — text, photo, sticker, etc.
    """

    edited_message: Optional[Message] = field(
        default=None, metadata={"ac_type": [Message], "ac_name": "edited_message"}
    )
    """*Optional*. New version of a message that is known to the bot and was edited
    """

    channel_post: Optional[Message] = field(
        default=None, metadata={"ac_type": [Message], "ac_name": "channel_post"}
    )
    """*Optional*. New incoming channel post of any kind — text, photo, sticker, etc.
    """

    edited_channel_post: Optional[Message] = field(
        default=None, metadata={"ac_type": [Message], "ac_name": "edited_channel_post"}
    )
    """*Optional*. New version of a channel post that is known to the bot and was edited
    """

    inline_query: Optional[InlineQuery] = field(
        default=None, metadata={"ac_type": [InlineQuery], "ac_name": "inline_query"}
    )
    """*Optional*. New incoming [inline](https://core.telegram.org/bots/api/#inline-mode) query
    """

    chosen_inline_result: Optional[ChosenInlineResult] = field(
        default=None,
        metadata={"ac_type": [ChosenInlineResult], "ac_name": "chosen_inline_result"},
    )
    """*Optional*. The result of an [inline](https://core.telegram.org/bots/api/#inline-mode) query that was chosen by a user and sent to their chat partner. Please see our documentation on the [feedback collecting](https://core.telegram.org/bots/inline#collecting-feedback) for details on how to enable these updates for your bot.
    """

    callback_query: Optional[CallbackQuery] = field(
        default=None, metadata={"ac_type": [CallbackQuery], "ac_name": "callback_query"}
    )
    """*Optional*. New incoming callback query
    """

    shipping_query: Optional[ShippingQuery] = field(
        default=None, metadata={"ac_type": [ShippingQuery], "ac_name": "shipping_query"}
    )
    """*Optional*. New incoming shipping query. Only for invoices with flexible price
    """

    pre_checkout_query: Optional[PreCheckoutQuery] = field(
        default=None,
        metadata={"ac_type": [PreCheckoutQuery], "ac_name": "pre_checkout_query"},
    )
    """*Optional*. New incoming pre-checkout query. Contains full information about checkout
    """

    poll: Optional[Poll] = field(
        default=None, metadata={"ac_type": [Poll], "ac_name": "poll"}
    )
    """*Optional*. New poll state. Bots receive only updates about stopped polls and polls, which are sent by the bot
    """

    poll_answer: Optional[PollAnswer] = field(
        default=None, metadata={"ac_type": [PollAnswer], "ac_name": "poll_answer"}
    )
    """*Optional*. A user changed their answer in a non-anonymous poll. Bots receive new votes only in polls that were sent by the bot itself.
    """

    my_chat_member: Optional[ChatMemberUpdated] = field(
        default=None,
        metadata={"ac_type": [ChatMemberUpdated], "ac_name": "my_chat_member"},
    )
    """*Optional*. The bot's chat member status was updated in a chat. For private chats, this update is received only when the bot is blocked or unblocked by the user.
    """

    chat_member: Optional[ChatMemberUpdated] = field(
        default=None,
        metadata={"ac_type": [ChatMemberUpdated], "ac_name": "chat_member"},
    )
    """*Optional*. A chat member's status was updated in a chat. The bot must be an administrator in the chat and must explicitly specify “chat\\_member” in the list of *allowed\\_updates* to receive these updates.
    """

    chat_join_request: Optional[ChatJoinRequest] = field(
        default=None,
        metadata={"ac_type": [ChatJoinRequest], "ac_name": "chat_join_request"},
    )
    """*Optional*. A request to join the chat has been sent. The bot must have the *can\\_invite\\_users* administrator right in the chat to receive these updates.
    """

    @property
    def update_type(self):
        """The type of the update."""
        if self._update_type is not None:
            return self._update_type
        self._update_type = self._resolve_update_type()
        return self._update_type

    def _resolve_update_type(self):
        fs = fields(self)
        for field in fs:
            if field.name == "update_id":
                continue

            field_value = getattr(self, field.name)
            if field_value is not None:
                return field.metadata["ac_type"][0]
        return None
