from abc import ABCMeta
import dataclasses
from typing import Any, Optional, TypeVar, cast

from .._client_utilities._client_setter import ClientSetter


T = TypeVar("T", bound="TelegramBotsObject")
TValue = TypeVar("TValue")
TResult = TypeVar("TResult")


class TelegramBotsObject(metaclass=ABCMeta):
    def __init__(self, **kwargs: dict[str, Any]) -> None:
        self._metadata: dict[str, Any] = {}

    def set_metadata(self, key: str, value: TValue) -> TValue:
        try:
            self._metadata[key] = value
        except AttributeError:
            self._metadata = {key: value}
        return value

    def get_metadata(self, key: str, default_value: TValue) -> TValue:
        try:
            if key in self._metadata:
                return cast(TValue, self._metadata[key])
            else:
                self._metadata[key] = default_value
        except AttributeError:
            self._metadata = {key: default_value}
        return default_value

    def append_list_metadata(self, key: str, value: TValue) -> TValue:
        try:
            self._metadata[key].append(value)
        except AttributeError:
            self._metadata = {key: [value]}
        except KeyError:
            self._metadata[key] = [value]
        return value

    def get_list_metadata(self, key: str) -> list[Any]:
        try:
            return self._metadata[key]
        except (AttributeError, KeyError):
            return []

    def serialize(
        self,
        is_multipart_obj: bool = False,
        master_obj: Any = None,
        parent_key: Optional[str] = None,
    ) -> dict[str, Any] | Any:
        return self.serialize_dataclass(self, is_multipart_obj, master_obj, parent_key)

    @classmethod
    def deserialize(
        cls,
        data: dict[str, Any] | list[Any],
        custom_types: dict[str, list[type[Any]]] | None = None,
        client: Any = None,
    ):
        return TelegramBotsObject._deserialize(cls, data, custom_types, client)

    @staticmethod
    def deserialize_to(
        object_type: type[T],
        data: dict[str, Any] | list[Any],
        custom_types: dict[str, list[type[Any]]] | None = None,
        client: Any = None,
    ) -> T:
        return TelegramBotsObject._deserialize(object_type, data, custom_types, client)

    @staticmethod
    def serialize_dataclass(
        obj: "TelegramBotsObject",
        is_multipart_obj: bool = False,
        master_obj: Any = None,
        parent_key: Optional[str] = None,
    ) -> dict[str, Any]:

        if isinstance(obj, (list, tuple)):
            return [
                TelegramBotsObject.serialize_dataclass(
                    item, is_multipart_obj, master_obj, parent_key  # type: ignore
                )
                for item in obj  # type: ignore
            ]  # type: ignore

        fields = dataclasses.fields(obj)
        fields_values = (
            (x.metadata["ac_name"], getattr(obj, x.metadata["ac_name"])) for x in fields
        )

        non_none_fields_values = {x[0]: x[1] for x in fields_values if x[1] is not None}

        for x in non_none_fields_values:
            value = non_none_fields_values[x]
            if isinstance(value, TelegramBotsObject):
                non_none_fields_values[x] = value.serialize(
                    is_multipart_obj, master_obj, x
                )
            elif isinstance(value, (list, tuple)):
                results = [
                    TelegramBotsObject.serialize_dataclass(
                        x, is_multipart_obj, master_obj, x  # type: ignore
                    )
                    for x in value  # type: ignore
                ]
                non_none_fields_values[x] = [x for x in results if x is not None]
        # Remove None from dict
        return {x: y for x, y in non_none_fields_values.items() if y is not None}

    @staticmethod
    def _deserialize(
        object_type: type[T],
        data: dict[str, Any] | list[Any],
        custom_types: dict[str, list[type[Any]]] | None = None,
        client: Any = None,
    ) -> T:

        fields = dataclasses.fields(object_type)
        info = {x.metadata["ac_name"]: x.metadata["ac_type"] for x in fields}

        if custom_types is not None:
            for x in custom_types:
                if x in info:
                    info[x] = custom_types[x]

        name_replacements: dict[str, str] = {
            x.metadata["ac_name"]: x.name
            for x in fields
            if x.name != x.metadata["ac_name"]
        }

        if isinstance(data, list):
            return [
                object_type.deserialize(x, custom_types, client) for x in data
            ]  # type: ignore

        new_data = {}
        for x in data:
            if x in info:

                # ! Fix this
                if len(info[x]) > 1:
                    raise ValueError(
                        f"Multiple types for {x} in {object_type.__name__} not Supported yet"
                    )

                elif issubclass(info[x][0], TelegramBotsObject):
                    new_data[name_replacements.get(x, x)] = info[x][0].deserialize(
                        data[x], custom_types, client
                    )

                else:
                    new_data[name_replacements.get(x, x)] = data[x]

        result = object_type(**new_data)
        # set client
        if isinstance(result, ClientSetter):
            setattr(result, "_client", client)

        return result
