from typing import Any
from .types.api_object import TelegramBotsObject, T
from .types.objects import Message


__custom_types = {
    "pinned_message": [Message],  # in Chat object
    "reply_to_message": [Message],
}


def serialize(
    obj: TelegramBotsObject | list[TelegramBotsObject] | list[list[TelegramBotsObject]],
) -> dict[str, Any] | list[Any]:
    """serialize a `TelegramBotsObject` to a dict or list of dicts (`json-like`).

    Args:
        obj (`TelegramBotsObject | list[TelegramBotsObject] | list[list[TelegramBotsObject]]`):
            the object to serialize.

    Returns:
        `dict[str, Any] | list[Any]`: the serialized object.
    """
    return TelegramBotsObject.serialize_dataclass(obj, obj)


def deserialize(
    object_type: type[T],
    data: dict[str, Any] | list[Any],
    client: Any = None,
) -> T:
    """deserialize a `TelegramBotsObject` from a dict or list of dicts (`json-like`).

    Args:
        object_type (`type[T]`): Object to deserialize (`data`) to.
        data (`dict[str, Any] | list[Any]`): The data to deserialize.
        client (`Any`, optional): `TelegramBotsClient` instance. Defaults to None.

    Returns:
        T: The deserialized object.
    """
    return TelegramBotsObject.deserialize_to(object_type, data, __custom_types, client)
