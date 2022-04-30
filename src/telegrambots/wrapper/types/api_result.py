import dataclasses

from .api_object import TelegramBotsObject, TResult
from .objects.response_parameters import ResponseParameters
from typing import Any, Generic, Optional


@dataclasses.dataclass(init=True, repr=True, frozen=True, slots=True, kw_only=True)
class TelegramBotsApiResult(Generic[TResult], TelegramBotsObject):
    """
    This class is used to represent the result of an API call.
    """

    ok: bool = dataclasses.field(
        metadata={"ac_type": [bool], "ac_name": "ok"})
    """
    :obj:`bool`: True if the request was successful.
    """

    result: Optional[TResult] = dataclasses.field(default=None,
                                                  metadata={"ac_type": [Any], "ac_name": "result"})
    """
    :typevar:`T`: The result of the request.
    """

    description: Optional[str] = dataclasses.field(
        default=None, metadata={"ac_type": [str], "ac_name": "description"})
    """
    :obj:`str`: A human-readable description of the result.
    """

    error_code: Optional[int] = dataclasses.field(
        default=None, metadata={"ac_type": [int], "ac_name": "error_code"})
    """
    :obj:`int`: Error code.
    """

    parameters: Optional[ResponseParameters] = dataclasses.field(
        default=None, metadata={"ac_type": [ResponseParameters], "ac_name": "parameters"})
    """Some errors may also have an optional field 'parameters' of the
    type ResponseParameters, which can help to automatically
    handle the error."""
