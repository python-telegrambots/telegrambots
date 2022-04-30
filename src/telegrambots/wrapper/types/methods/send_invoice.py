from dataclasses import dataclass, field
from typing import Any, Optional

from ..api_method import TelegramBotsMethod
from ..api_result import TelegramBotsApiResult
from ..objects.labeled_price import LabeledPrice
from ..objects.message import Message
from ..objects.inline_keyboard_markup import InlineKeyboardMarkup


@dataclass(init=True, repr=True, slots=True)
class SendInvoice(TelegramBotsMethod[TelegramBotsApiResult[Message]]):
    # --- description here ---
    """Use this method to send invoices. On success, the sent [Message](https://core.telegram.org/bots/api/#message) is returned.
    
    More info at: https://core.telegram.org/bots/api/#sendinvoice
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMethod.__init__(  # type: ignore
            obj, "sendInvoice", [Message])
        return obj


    # --- arguments here ---
    chat_id: int | str = field(metadata={"ac_type": [int, str], "ac_name": "chat_id"})
    """Unique identifier for the target chat or username of the target channel (in the format `@channelusername`)
    """

    title: str = field(metadata={"ac_type": [str], "ac_name": "title"})
    """Product name, 1-32 characters
    """

    description: str = field(metadata={"ac_type": [str], "ac_name": "description"})
    """Product description, 1-255 characters
    """

    payload: str = field(metadata={"ac_type": [str], "ac_name": "payload"})
    """Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use for your internal processes.
    """

    provider_token: str = field(metadata={"ac_type": [str], "ac_name": "provider_token"})
    """Payments provider token, obtained via [Botfather](https://t.me/botfather)
    """

    currency: str = field(metadata={"ac_type": [str], "ac_name": "currency"})
    """Three-letter ISO 4217 currency code, see [more on currencies](https://core.telegram.org/bots/payments#supported-currencies)
    """

    prices: list[LabeledPrice] = field(metadata={"ac_type": [LabeledPrice], "ac_name": "prices"})
    """Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.)
    """

    max_tip_amount: int = field(default=0, metadata={"ac_type": [int], "ac_name": "max_tip_amount"})
    """The maximum accepted amount for tips in the *smallest units* of the currency (integer, **not** float/double). For example, for a maximum tip of `US$ 1.45` pass `max_tip_amount = 145`. See the *exp* parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). Defaults to 0
    """

    suggested_tip_amounts: Optional[list[int]] = field(default=None, metadata={"ac_type": [int], "ac_name": "suggested_tip_amounts"})
    """A JSON-serialized array of suggested amounts of tips in the *smallest units* of the currency (integer, **not** float/double). At most 4 suggested tip amounts can be specified. The suggested tip amounts must be positive, passed in a strictly increased order and must not exceed *max\\_tip\\_amount*.
    """

    start_parameter: Optional[str] = field(default=None, metadata={"ac_type": [str], "ac_name": "start_parameter"})
    """Unique deep-linking parameter. If left empty, **forwarded copies** of the sent message will have a *Pay* button, allowing multiple users to pay directly from the forwarded message, using the same invoice. If non-empty, forwarded copies of the sent message will have a *URL* button with a deep link to the bot (instead of a *Pay* button), with the value used as the start parameter
    """

    provider_data: Optional[str] = field(default=None, metadata={"ac_type": [str], "ac_name": "provider_data"})
    """A JSON-serialized data about the invoice, which will be shared with the payment provider. A detailed description of required fields should be provided by the payment provider.
    """

    photo_url: Optional[str] = field(default=None, metadata={"ac_type": [str], "ac_name": "photo_url"})
    """URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service. People like it better when they see what they are paying for.
    """

    photo_size: Optional[int] = field(default=None, metadata={"ac_type": [int], "ac_name": "photo_size"})
    """Photo size
    """

    photo_width: Optional[int] = field(default=None, metadata={"ac_type": [int], "ac_name": "photo_width"})
    """Photo width
    """

    photo_height: Optional[int] = field(default=None, metadata={"ac_type": [int], "ac_name": "photo_height"})
    """Photo height
    """

    need_name: Optional[bool] = field(default=None, metadata={"ac_type": [bool], "ac_name": "need_name"})
    """Pass *True*, if you require the user's full name to complete the order
    """

    need_phone_number: Optional[bool] = field(default=None, metadata={"ac_type": [bool], "ac_name": "need_phone_number"})
    """Pass *True*, if you require the user's phone number to complete the order
    """

    need_email: Optional[bool] = field(default=None, metadata={"ac_type": [bool], "ac_name": "need_email"})
    """Pass *True*, if you require the user's email address to complete the order
    """

    need_shipping_address: Optional[bool] = field(default=None, metadata={"ac_type": [bool], "ac_name": "need_shipping_address"})
    """Pass *True*, if you require the user's shipping address to complete the order
    """

    send_phone_number_to_provider: Optional[bool] = field(default=None, metadata={"ac_type": [bool], "ac_name": "send_phone_number_to_provider"})
    """Pass *True*, if user's phone number should be sent to provider
    """

    send_email_to_provider: Optional[bool] = field(default=None, metadata={"ac_type": [bool], "ac_name": "send_email_to_provider"})
    """Pass *True*, if user's email address should be sent to provider
    """

    is_flexible: Optional[bool] = field(default=None, metadata={"ac_type": [bool], "ac_name": "is_flexible"})
    """Pass *True*, if the final price depends on the shipping method
    """

    disable_notification: Optional[bool] = field(default=None, metadata={"ac_type": [bool], "ac_name": "disable_notification"})
    """Sends the message [silently](https://telegram.org/blog/channels-2-0#silent-messages). Users will receive a notification with no sound.
    """

    protect_content: Optional[bool] = field(default=None, metadata={"ac_type": [bool], "ac_name": "protect_content"})
    """Protects the contents of the sent message from forwarding and saving
    """

    reply_to_message_id: Optional[int] = field(default=None, metadata={"ac_type": [int], "ac_name": "reply_to_message_id"})
    """If the message is a reply, ID of the original message
    """

    allow_sending_without_reply: Optional[bool] = field(default=None, metadata={"ac_type": [bool], "ac_name": "allow_sending_without_reply"})
    """Pass *True*, if the message should be sent even if the specified replied-to message is not found
    """

    reply_markup: Optional[InlineKeyboardMarkup] = field(default=None, metadata={"ac_type": [InlineKeyboardMarkup], "ac_name": "reply_markup"})
    """A JSON-serialized object for an [inline keyboard](https://core.telegram.org/bots#inline-keyboards-and-on-the-fly-updating). If empty, one 'Pay `total price`' button will be shown. If not empty, the first button must be a Pay button.
    """

