from dataclasses import dataclass, field
from typing import Any

from ..api_method import TelegramBotsMethod
from ..api_result import TelegramBotsApiResult
from ..objects.sent_web_app_message import SentWebAppMessage
from ..objects.inline_query_result import InlineQueryResult


@dataclass(init=True, repr=True, slots=True)
class AnswerWebAppQuery(TelegramBotsMethod[TelegramBotsApiResult[SentWebAppMessage]]):
    # --- description here ---
    """Use this method to set the result of an interaction with a [Web App](https://core.telegram.org/bots/webapps) and send a corresponding message on behalf of the user to the chat from which the query originated. On success, a [SentWebAppMessage](https://core.telegram.org/bots/api/#sentwebappmessage) object is returned.
    
    More info at: https://core.telegram.org/bots/api/#answerwebappquery
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        TelegramBotsMethod.__init__(  # type: ignore
            obj, "answerWebAppQuery", [SentWebAppMessage])
        return obj


    # --- arguments here ---
    web_app_query_id: str = field(metadata={"ac_type": [str], "ac_name": "web_app_query_id"})
    """Unique identifier for the query to be answered
    """

    result: InlineQueryResult = field(metadata={"ac_type": [InlineQueryResult], "ac_name": "result"})
    """A JSON-serialized object describing the message to be sent
    """

