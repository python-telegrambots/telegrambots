from abc import ABCMeta
import dataclasses
import json
from typing import Any, Optional, TypeVar, cast

from .._client_utilities._client_setter import ClientSetter


T = TypeVar("T", bound="TelegramBotsObject")
TValue = TypeVar("TValue")
TResult = TypeVar("TResult")


class TelegramBotsObject(metaclass=ABCMeta):
    def __init__(self, **kwargs: dict[str, Any]) -> None:
        self._metadata: dict[str, Any] = {}

    # region Metadata

    def __ensure_metadata(self):
        if not hasattr(self, "_metadata"):
            self._metadata = {}

    def _set_metadata(self, key: str, value: TValue) -> TValue:
        self.__ensure_metadata()
        self._metadata[key] = value
        return value

    def has_metadata(self, key: str) -> bool:
        self.__ensure_metadata()
        return key in self._metadata

    def get_metadata(self, key: str, default_value: TValue) -> TValue:
        self.__ensure_metadata()
        if key in self._metadata:
            return cast(TValue, self._metadata[key])
        else:
            self._metadata[key] = default_value
        return default_value

    def append_list_metadata(self, key: str, value: TValue) -> TValue:
        if self.has_metadata(key):
            self._metadata[key].append(value)
        else:
            self._metadata[key] = [value]
        return value

    def get_list_metadata(self, key: str) -> list[Any]:
        default: list[Any] = []
        return self.get_metadata(key, default)

    # endregion

    # region Serialize

    def serialize(
        self,
        master_obj: Any = None,
        parent_key: Optional[str] = None,
    ) -> dict[str, Any] | Any:
        return self.serialize_dataclass(self, master_obj, parent_key)

    @staticmethod
    def __get_fields_values(obj: Any):
        for x in dataclasses.fields(obj):
            field_name: str = x.metadata["ac_name"]
            if not field_name.startswith("_"):
                yield (field_name, getattr(obj, field_name))

    @staticmethod
    def serialize_dataclass(
        obj: Any | list[Any] | list[list[Any]],
        master_obj: Any = None,
        parent_key: Optional[str] = None,
    ) -> dict[str, Any] | list[Any]:

        if isinstance(obj, (list, tuple)):
            return [
                TelegramBotsObject.serialize_dataclass(item, master_obj, parent_key)
                for item in obj
            ]
        elif isinstance(obj, TelegramBotsObject):
            # Hmmm
            return {
                x: y
                for x, y in (  # type: ignore
                    (
                        key,
                        (
                            value.serialize(master_obj, key)
                            if isinstance(value, TelegramBotsObject)
                            else (
                                TelegramBotsObject.serialize_dataclass(
                                    value, master_obj, key  # type: ignore
                                )
                                if isinstance(value, (list, tuple))
                                else value
                            )
                        ),
                    )
                    for key, value in (TelegramBotsObject.__get_fields_values(obj))
                    if value is not None
                )
                if y is not None
            }
        else:
            return obj

    # endregion

    # region Deserialize

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
    def _deserialize(
        object_type: type[T],
        data: dict[str, Any] | list[Any],
        custom_types: dict[str, list[type[Any]]] | None = None,
        client: Any = None,
    ) -> T:

        if isinstance(data, list):
            if issubclass(object_type, TelegramBotsObject):
                return [
                    object_type.deserialize(item, custom_types, client)  # type: ignore
                    for item in data
                ]  # type: ignore
            else:
                return data  # type: ignore
        elif isinstance(data, dict):  # type: ignore

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

            new_data = {}
            for x in data:
                if x in info:

                    if len(info[x]) > 1:
                        # it occurs only ones: Message | bool
                        if isinstance(data[x], dict):
                            type_to_convert: type[TelegramBotsObject] = next(
                                t for t in info[x] if issubclass(t, TelegramBotsObject)
                            )
                            new_data[
                                name_replacements.get(x, x)
                            ] = type_to_convert.deserialize(
                                data[x], custom_types, client
                            )
                        else:
                            new_data[name_replacements.get(x, x)] = None

                    elif issubclass(info[x][0], TelegramBotsObject):
                        new_data[name_replacements.get(x, x)] = info[x][0].deserialize(
                            data[x], custom_types, client
                        )

                    else:
                        new_data[name_replacements.get(x, x)] = data[x]
        else:
            return data  # type: ignore

        result = object_type(**new_data)
        # set client
        if isinstance(result, ClientSetter):
            setattr(result, "_client", client)

        return result

    # endregion

    def pretty_str(self):
        return json.dumps(
            self.serialize(), indent=4, sort_keys=True, ensure_ascii=False
        )
