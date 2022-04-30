from dataclasses import dataclass, field
from typing import Any, overload

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject

from .inline_keyboard_button import InlineKeyboardButton


@dataclass(init=True, repr=True, slots=True)
class InlineKeyboardMarkup(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object represents an [inline keyboard](https://core.telegram.org/bots#inline-keyboards-and-on-the-fly-updating) that appears right next to the message it belongs to.

    More info at: https://core.telegram.org/bots/api/#inlinekeyboardmarkup
    """

    # --- properties here ---
    inline_keyboard: list[list[InlineKeyboardButton]] = field(
        metadata={"ac_type": [InlineKeyboardButton], "ac_name": "inline_keyboard"}
    )
    """Array of button rows, each represented by an Array of [InlineKeyboardButton](https://core.telegram.org/bots/api/#inlinekeyboardbutton) objects
    """

    @overload
    def __init__(self, inline_keyboard: list[list[InlineKeyboardButton]]) -> None:
        """Creates a new InlineKeyboardMarkup object with a list of rows.

        Args:
            inline_keyboard (`list[list[InlineKeyboardButton]]`):
            Array of button rows, each represented by an Array of objects
        """
        ...

    @overload
    def __init__(self, inline_keyboard: list[InlineKeyboardButton]) -> None:
        """Creates a new single row InlineKeyboardMarkup object with a list of buttons.

        Args:
            inline_keyboard (`list[InlineKeyboardButton]`):
            Array of buttons in a row
        """
        ...

    @overload
    def __init__(self, inline_keyboard: InlineKeyboardButton) -> None:
        """Creates a new single button InlineKeyboardMarkup object.

        Args:
            inline_keyboard (`InlineKeyboardButton`): Button to be added
        """
        ...

    def __init__(self, inline_keyboard: Any) -> None:
        if isinstance(inline_keyboard, list):
            if isinstance(inline_keyboard[0], list):
                self.inline_keyboard = inline_keyboard
            else:
                self.inline_keyboard = [inline_keyboard]
        elif isinstance(inline_keyboard, InlineKeyboardButton):
            self.inline_keyboard = [[inline_keyboard]]
        else:
            raise ValueError(
                f"InlineKeyboardMarkup.__init__: inline_keyboard must be a"
                "list of InlineKeyboardButton or list of lists of"
                "InlineKeyboardButton. Got {type(inline_keyboard)} instead."
            )
