from dataclasses import dataclass, field
from typing import Any, Optional

from ..api_method import TelegramBotsMethod
from ..api_result import TelegramBotsApiResult
from ..objects.inline_query_result import InlineQueryResult


@dataclass(init=True, repr=True, slots=True)
class AnswerInlineQuery(TelegramBotsMethod[TelegramBotsApiResult[bool]]):
    # --- description here ---
    """Use this method to send answers to an inline query. On success, *True* is returned.  
    No more than **50** results per query are allowed.
    
    More info at: https://core.telegram.org/bots/api/#answerinlinequery
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMethod.__init__(  # type: ignore
            obj, "answerInlineQuery", [bool])
        return obj


    # --- arguments here ---
    inline_query_id: str = field(metadata={"ac_type": [str], "ac_name": "inline_query_id"})
    """Unique identifier for the answered query
    """

    results: list[InlineQueryResult] = field(metadata={"ac_type": [InlineQueryResult], "ac_name": "results"})
    """A JSON-serialized array of results for the inline query
    """

    cache_time: int = field(default=300, metadata={"ac_type": [int], "ac_name": "cache_time"})
    """The maximum amount of time in seconds that the result of the inline query may be cached on the server. Defaults to 300.
    """

    is_personal: Optional[bool] = field(default=None, metadata={"ac_type": [bool], "ac_name": "is_personal"})
    """Pass *True*, if results may be cached on the server side only for the user that sent the query. By default, results may be returned to any user who sends the same query
    """

    next_offset: Optional[str] = field(default=None, metadata={"ac_type": [str], "ac_name": "next_offset"})
    """Pass the offset that a client should send in the next query with the same text to receive more results. Pass an empty string if there are no more results or if you don't support pagination. Offset length can't exceed 64 bytes.
    """

    switch_pm_text: Optional[str] = field(default=None, metadata={"ac_type": [str], "ac_name": "switch_pm_text"})
    """If passed, clients will display a button with specified text that switches the user to a private chat with the bot and sends the bot a start message with the parameter *switch\\_pm\\_parameter*
    """

    switch_pm_parameter: Optional[str] = field(default=None, metadata={"ac_type": [str], "ac_name": "switch_pm_parameter"})
    """[Deep-linking](https://core.telegram.org/bots#deep-linking) parameter for the /start message sent to the bot when user presses the switch button. 1-64 characters, only `A-Z`, `a-z`, `0-9`, `_` and `-` are allowed.  

*Example:* An inline bot that sends YouTube videos can ask the user to connect the bot to their YouTube account to adapt search results accordingly. To do this, it displays a 'Connect your YouTube account' button above the results, or even before showing any. The user presses the button, switches to a private chat with the bot and, in doing so, passes a start parameter that instructs the bot to return an OAuth link. Once done, the bot can offer a [*switch\\_inline*](https://core.telegram.org/bots/api/#inlinekeyboardmarkup) button so that the user can easily return to the chat where they wanted to use the bot's inline capabilities.
    """

