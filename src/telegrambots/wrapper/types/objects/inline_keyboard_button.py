from dataclasses import dataclass, field
from typing import Optional

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject

from .web_app_info import WebAppInfo
from .callback_game import CallbackGame
from .login_url import LoginUrl


@dataclass(init=True, repr=True, slots=True)
class InlineKeyboardButton(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object represents one button of an inline keyboard. You **must** use exactly one of the optional fields.

    More info at: https://core.telegram.org/bots/api/#inlinekeyboardbutton
    """

    # --- properties here ---
    text: str = field(metadata={"ac_type": [str], "ac_name": "text"})
    """Label text on the button
    """

    url: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "url"}
    )
    """*Optional*. HTTP or tg:// url to be opened when the button is pressed. Links `tg://user?id=<user_id>` can be used to mention a user by their ID without using a username, if this is allowed by their privacy settings.
    """

    callback_data: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "callback_data"}
    )
    """*Optional*. Data to be sent in a [callback query](https://core.telegram.org/bots/api/#callbackquery) to the bot when button is pressed, 1-64 bytes
    """

    web_app: Optional[WebAppInfo] = field(
        default=None, metadata={"ac_type": [WebAppInfo], "ac_name": "web_app"}
    )
    """*Optional*. Description of the [Web App](https://core.telegram.org/bots/webapps) that will be launched when the user presses the button. The Web App will be able to send an arbitrary message on behalf of the user using the method [answerWebAppQuery](https://core.telegram.org/bots/api/#answerwebappquery). Available only in private chats between a user and the bot.
    """

    login_url: Optional[LoginUrl] = field(
        default=None, metadata={"ac_type": [LoginUrl], "ac_name": "login_url"}
    )
    """*Optional*. An HTTP URL used to automatically authorize the user. Can be used as a replacement for the [Telegram Login Widget](https://core.telegram.org/widgets/login).
    """

    switch_inline_query: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "switch_inline_query"}
    )
    """*Optional*. If set, pressing the button will prompt the user to select one of their chats, open that chat and insert the bot's username and the specified inline query in the input field. Can be empty, in which case just the bot's username will be inserted.  

**Note:** This offers an easy way for users to start using your bot in [inline mode](https://core.telegram.org/bots/inline) when they are currently in a private chat with it. Especially useful when combined with [*switch\\_pm…*](https://core.telegram.org/bots/api/#answerinlinequery) actions – in this case the user will be automatically returned to the chat they switched from, skipping the chat selection screen.
    """

    switch_inline_query_current_chat: Optional[str] = field(
        default=None,
        metadata={"ac_type": [str], "ac_name": "switch_inline_query_current_chat"},
    )
    """*Optional*. If set, pressing the button will insert the bot's username and the specified inline query in the current chat's input field. Can be empty, in which case only the bot's username will be inserted.  

This offers a quick way for the user to open your bot in inline mode in the same chat – good for selecting something from multiple options.
    """

    callback_game: Optional[CallbackGame] = field(
        default=None, metadata={"ac_type": [CallbackGame], "ac_name": "callback_game"}
    )
    """*Optional*. Description of the game that will be launched when the user presses the button.  

**NOTE:** This type of button **must** always be the first button in the first row.
    """

    pay: Optional[bool] = field(
        default=None, metadata={"ac_type": [bool], "ac_name": "pay"}
    )
    """*Optional*. Specify *True*, to send a [Pay button](https://core.telegram.org/bots/api/#payments).  

**NOTE:** This type of button **must** always be the first button in the first row and can only be used in invoice messages.
    """

    # --- static methods ----

    @staticmethod
    def with_url(text: str, url: str) -> "InlineKeyboardButton":
        """Creates a new InlineKeyboardButton object with url property set.

        Args:
            text (`str`): Label text on the button

            url (`str`): HTTP or tg:// url to be opened when the button
            is pressed. Links `tg://user?id=<user_id>` can be used to mention
            a user by their ID without using a username, if this is allowed by
            their privacy settings.

        Returns:
            `InlineKeyboardButton`: InlineKeyboardButton object.
        """
        return InlineKeyboardButton(text=text, url=url)

    @staticmethod
    def with_callback_data(text: str, callback_data: str) -> "InlineKeyboardButton":
        """Creates a new InlineKeyboardButton object with the specified text and callback_data.

        Args:
            text (`str`): Label text on the button

            callback_data (`str`): Data to be sent in a
            [callback query](https://core.telegram.org/bots/api/#callbackquery)
            to the bot when button is pressed, 1-64 bytes

        Returns:
            `InlineKeyboardButton`: InlineKeyboardButton object.
        """
        return InlineKeyboardButton(text=text, callback_data=callback_data)

    @staticmethod
    def with_switch_inline_query(
        text: str, switch_inline_query: str
    ) -> "InlineKeyboardButton":
        """Creates a new InlineKeyboardButton object with the specified text and switch_inline_query.

        Args:
            text (`str`): Label text on the button

            switch_inline_query (`str`): Query to be sent to the bot via
            [inline mode](https://core.telegram.org/bots/inline)
            when the button is pressed. 1-64 characters

        Returns:
            `InlineKeyboardButton`: InlineKeyboardButton object.
        """
        return InlineKeyboardButton(text=text, switch_inline_query=switch_inline_query)

    @staticmethod
    def with_switch_inline_query_current_chat(
        text: str, switch_inline_query_current_chat: str
    ) -> "InlineKeyboardButton":
        """Creates a new InlineKeyboardButton object with the specified text and switch_inline_query_current_chat.

        Args:
            text (`str`): Label text on the button

            switch_inline_query_current_chat (`str`): Query to be sent to the bot via
            [inline mode](https://core.telegram.org/bots/inline)
            when the button is pressed. 1-64 characters

        Returns:
            `InlineKeyboardButton`: InlineKeyboardButton object.
        """
        return InlineKeyboardButton(
            text=text, switch_inline_query_current_chat=switch_inline_query_current_chat
        )

    @staticmethod
    def with_login_url(text: str, login_url: LoginUrl) -> "InlineKeyboardButton":
        """Creates a new InlineKeyboardButton object with the specified text and login_url.

        Args:
            text (`str`): Label text on the button

            login_url (`LoginUrl`): An HTTP URL used to automatically authorize the user. Can be used as a replacement for the [Telegram Login Widget](https://core.telegram.org/widgets/login).

        Returns:
            `InlineKeyboardButton`: InlineKeyboardButton object.
        """
        return InlineKeyboardButton(text=text, login_url=login_url)

    @staticmethod
    def with_callback_game(
        text: str, callback_game: CallbackGame
    ) -> "InlineKeyboardButton":
        """Creates a new InlineKeyboardButton object with the specified text and callback_game.

        Args:
            text (`str`): Label text on the button

            callback_game (`CallbackGame`): Description of the game that will be launched when the user presses the button.

        Returns:
            `InlineKeyboardButton`: InlineKeyboardButton object.
        """
        return InlineKeyboardButton(text=text, callback_game=callback_game)

    @staticmethod
    def with_pay(text: str, pay: bool) -> "InlineKeyboardButton":
        """Creates a new InlineKeyboardButton object with the specified text and pay.

        Args:
            text (`str`): Label text on the button

            pay (`bool`): Specify *True*, to send a [Pay button](https://core.telegram.org/bots/api/#payments).

        Returns:
            `InlineKeyboardButton`: InlineKeyboardButton object.
        """
        return InlineKeyboardButton(text=text, pay=pay)
