import json
import pathlib
from typing import Any, Generator, TypeVar

T = TypeVar("T")

tab = "    "

object_template = '''from dataclasses import dataclass{field_import}{typing_imports}

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject
{other_imports}
{ref_imports}


@dataclass(init=True, repr=True, slots=True)
class {name}({base}):
    # --- description here ---
    """{description}
    """

    # --- properties here ---
{properties}
'''

object_template_no_prop = '''import dataclasses

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject
{other_imports}
{ref_imports}


@dataclasses.dataclass(init=True, repr=True, slots=True)
class {name}({base}):
    # --- description here ---
    """{description}
    """
'''


object_template_abstract = '''import abc
import dataclasses

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject
{other_imports}


@dataclasses.dataclass(init=True, repr=True, slots=True)
class {name}(abc.ABC, TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """{description}
    """
'''

method_template = '''from dataclasses import dataclass{field_import}{typing_imports}

{method_import}
from ..api_result import TelegramBotsApiResult{other_imports}
{ref_imports}


@dataclass(init=True, repr=True, slots=True)
class {name}({base_method}[TelegramBotsApiResult[{return_type}]]):
    # --- description here ---
    """{description}
    """

    def __new__(cls, *args: Any, **kwargs: Any):
        obj = object.__new__(cls)
        {base_method}.__init__(  # type: ignore
            obj, "{end_point}", {actual_return_type})
        return obj


    # --- arguments here ---
{arguments}
'''


types_mapping = {"integer": "int", "string": "str"}


def escape_naming(name: str):
    if name == "from":
        return "from_user"
    return name


def generate_enumeration(values: list[str]):
    return "Literal[" + ",".join(map(lambda x: f'"{x}"', values)) + "]"


def build_type(
    parent_type: str,
    type: str,
    reference: str | None = None,
    array: dict[str, str] | None = None,
    enumeration: list[str] | None = None,
    any_of: list[dict[str, Any]] | None = None,
    default: str | None = None,
):

    real_types: list[str] = []
    typing_imports: list[str] = []
    if type == "reference":
        if reference is None:
            raise ValueError("reference is None")

        if parent_type == reference:
            actual_type = f"'{reference}'"
        else:
            actual_type = reference
        refs: list[str] = [reference]
        real_types.append(actual_type)
    elif type == "array":
        if array is None:
            raise ValueError("array is None")

        type_str, reference, rank, ti = build_type(  # type: ignore
            parent_type, **array
        )  # type: ignore
        real_types.extend(rank)
        actual_type = "list[{type}]".format(type=type_str)  # type: ignore
        refs = [reference] if reference is not None else []
        typing_imports.extend(ti)  # type: ignore
    elif type == "any_of":
        if any_of is None:
            raise ValueError("any_of is None")

        any_ofs: list[tuple[str, str | None, list[str], list[str]]] = [
            build_type(parent_type, **x) for x in any_of
        ]  # type: ignore
        all_types = [x[0] for x in any_ofs]
        real_types.extend(all_types)
        actual_type = " | ".join(all_types)
        refs = [x[1] for x in any_ofs if x[1] is not None]
        for ti in any_ofs:
            typing_imports.extend(ti[3])
    else:
        if type == "string":
            if enumeration is not None:
                actual_type = generate_enumeration(enumeration)
                typing_imports.append("Literal")
            else:
                actual_type = "str"
            real_types.append("str")
        else:
            actual_type = types_mapping.get(type, type)
            real_types.append(actual_type)
        refs = []
    return actual_type, refs, real_types, typing_imports


def generate_property(
    parent_name: str,
    *,
    name: str,
    type: str,
    description: str,
    required: bool,
    reference: str | None = None,
    array: dict[str, str] | None = None,
    enumeration: list[str] | None = None,
    any_of: list[dict[str, Any]] | None = None,
    default: str | None = None,
    min_len: int | None = None,
    max_len: int | None = None,
    min: int | None = None,
    max: int | None = None,
):

    actual_type, refs, real_types, typing_imports = build_type(
        parent_name,
        type,
        reference=reference,
        array=array,
        enumeration=enumeration,
        any_of=any_of,
    )

    if not required:
        if default is None:
            actual_type = f"Optional[{actual_type}]"
            typing_imports.append("Optional")

    first_style = f"{tab}{escape_naming(name)}: {actual_type}"
    real_types_str = "[" + ", ".join(real_types) + "]"
    if not required:
        if default is not None:
            if actual_type == "str":
                default = f"'{default}'"

            first_style += ' = field(default={default}, metadata={ob}"ac_type": {actual_type}, "ac_name": "{name}"{cb})'.format(
                actual_type=real_types_str, ob="{", cb="}", default=default, name=name
            )
        else:
            first_style += ' = field(default=None, metadata={ob}"ac_type": {actual_type}, "ac_name": "{name}"{cb})'.format(
                actual_type=real_types_str, ob="{", cb="}", name=name
            )
    else:
        first_style += ' = field(metadata={ob}"ac_type": {actual_type}, "ac_name": "{name}"{cb})'.format(
            actual_type=real_types_str, ob="{", cb="}", name=name
        )

    first_style += '\n{tab}"""{desc}\n{tab}"""\n'.format(
        tab=tab, desc=description.replace("\\", "\\\\")
    )

    if reference is not None:
        if reference not in refs:
            refs.append(reference)

    return first_style, refs, typing_imports


def generate_return_type(
    parent_name: str,
    *,
    type: str,
    reference: str | None = None,
    array: dict[str, str] | None = None,
    enumeration: list[str] | None = None,
    any_of: list[dict[str, Any]] | None = None,
    default: str | None = None,
    min_len: int | None = None,
    max_len: int | None = None,
    min: int | None = None,
    max: int | None = None,
):

    actual_type, refs, actual_return_type, typing_imports = build_type(
        parent_name,
        type,
        reference=reference,
        array=array,
        enumeration=enumeration,
        any_of=any_of,
    )

    first_style = actual_type

    if reference is not None:
        if reference not in refs:
            refs.append(reference)

    return first_style, refs, actual_return_type, typing_imports


any_of_found: dict[str, list[str]] = {}


def is_any_of(name: str):
    for key, val in any_of_found.items():
        if name in val:
            return key
    return ""


def generate_ref_imports(refs: list[str], in_methods: bool = False):
    strs = [x for x in refs if isinstance(x, str)]  # type: ignore
    result = "\n".join(
        f"from .{camel_case_to_snake_case(x)} import {x}"
        if not in_methods
        else f"from ..objects.{camel_case_to_snake_case(x)} import {x}"
        for x in set(strs)
    )
    return result


def flat_list(l: list[list[T]]) -> Generator[T, None, None]:
    for x in l:
        if isinstance(x, list):  # type: ignore
            yield from flat_list(x)  # type: ignore
        else:
            yield x  # type: ignore


def generate_object(
    name: str,
    description: str,
    type: str | None = None,
    properties: list[dict[str, Any]] | None = None,
    any_of: list[dict[str, Any]] | None = None,
    documentation_link: str | None = None,
):

    description += (
        "\n\nMore info at: " + documentation_link if documentation_link else ""
    )

    if type is None:
        any_of_text = is_any_of(name)
        return object_template_no_prop.format(
            name=name,
            description=description.replace("\n", "\n" + tab),
            base=any_of_text if any_of_text else "TelegramBotsObject, ClientTargetable",
            other_imports=f"from .{camel_case_to_snake_case(any_of_text)} import {any_of_text}"
            if any_of_text
            else "",
            ref_imports="",
        )

    elif type == "properties":
        if properties is None:
            raise ValueError("properties is None")

        props = [
            generate_property(name, **prop)
            for prop in sorted(properties, key=lambda x: not x["required"])
        ]

        propes_str = "\n".join([x[0] for x in props])
        references = list(flat_list([x[1] for x in props if x[1] is not None and x[1]]))
        references = [x for x in references if x != name]

        typing_imports = list(
            flat_list([x[2] for x in props if x[2] is not None and x[2]])
        )
        if any(typing_imports):
            typing_imports = list(set(typing_imports))
            typing_imports_str = "\nfrom typing import " + ", ".join(typing_imports)
        else:
            typing_imports_str = ""

        if props:
            field_str = ", field"
        else:
            field_str = ""

        any_of_text = is_any_of(name)
        return object_template.format(
            name=name,
            field_import=field_str,
            typing_imports=typing_imports_str,
            description=description.replace("\n", "\n" + tab).replace("\\", "\\\\"),
            properties=propes_str,
            base=any_of_text if any_of_text else "TelegramBotsObject, ClientTargetable",
            other_imports=f"from .{camel_case_to_snake_case(any_of_text)} import {any_of_text}"
            if any_of_text
            else "",
            ref_imports=generate_ref_imports(references),
        )

    elif type == "any_of":
        if any_of is None:
            raise ValueError("Any of not found")

        any_of_found[name] = [x["reference"] for x in any_of]
        return object_template_abstract.format(
            name=name,
            description=description.replace("\n", "\n" + tab),
            other_imports="",
        )

    raise ValueError(f"Unknown type: {type}")


def camel_case_to_pascal_case(name: str):
    # testMethod -> TestMethod
    # helloWorld -> HelloWorld
    return name[0].upper() + name[1::]


def camel_case_to_snake_case(name: str):
    result: list[str] = []
    for char in name:
        if char.isupper():
            if result:
                result.append("_")
            result.append(char.lower())
        else:
            result.append(char)
    return "".join(result)


def generate_method(
    name: str,
    description: str,
    arguments: list[dict[str, Any]] | None = None,
    return_type: dict[str, Any] | None = None,
    multipart_only: bool = False,
    documentation_link: str | None = None,
):

    if arguments is None:
        arguments = []

    typing_imports: list[str] = ["Any"]

    if return_type is None:
        return_type_str = "None"
        actual_return_type = "None"
    else:
        return_type_str, refs, actual_return_type, ti = generate_return_type(
            name, **return_type
        )
        typing_imports += ti

    props = [
        generate_property(name, **args)
        for args in sorted(arguments, key=lambda x: x["required"], reverse=True)
    ]

    propes_str = "\n".join([x[0] for x in props])
    all_refs: list[Any] = [
        x[1] for x in props if x[1] is not None and x[1]
    ] + refs  # type: ignore

    references = list(flat_list(all_refs))
    references = [x for x in references if x != name]

    typing_imports += list(
        flat_list([x[2] for x in props if x[2] is not None and x[2]])
    )
    if any(typing_imports):
        typing_imports = list(set(typing_imports))
        typing_imports_str = "\nfrom typing import " + ", ".join(typing_imports)
    else:
        typing_imports_str = ""

    description += (
        "\n\nMore info at: " + documentation_link if documentation_link else ""
    )

    if props:
        field_str = ", field"
    else:
        field_str = ""

    method_import = (
        "from ..api_multipart_method import TelegramBotsMultipartMethod"
        if multipart_only
        else "from ..api_method import TelegramBotsMethod"
    )

    base_method = (
        "TelegramBotsMultipartMethod" if multipart_only else "TelegramBotsMethod"
    )

    any_of_text = is_any_of(name)
    return method_template.format(
        name=camel_case_to_pascal_case(name),
        end_point=name,
        field_import=field_str,
        typing_imports=typing_imports_str,
        method_import=method_import,
        base_method=base_method,
        description=description.replace("\n", "\n" + tab).replace("\\", "\\\\"),
        arguments=propes_str,
        return_type=return_type_str,
        actual_return_type="[" + ",".join(actual_return_type) + "]",
        other_imports=f"from .{camel_case_to_snake_case(any_of_text)} import {any_of_text}"
        if any_of_text
        else "",
        ref_imports=generate_ref_imports(references, True),
    )


def main(methods_only: bool = False, objects_only: bool = False):
    current_dir = pathlib.Path(__file__).parent.resolve()

    schema_path = current_dir.joinpath("custom.json")

    # output_dir = current_dir.joinpath('_out')
    output_dir = pathlib.Path(
        "C:/Users/immmdreza/Desktop/Sources/python-telegrambots/src/telegrambots/wrapper/types"
    )

    if not output_dir.exists():
        output_dir.mkdir()

    with open(schema_path, "r", encoding="utf8") as schema_file:
        schema = json.load(schema_file)

    # parsing objects
    if not methods_only:
        objects_path = output_dir.joinpath("objects")

        if not objects_path.exists():
            objects_path.mkdir()

        for obj in schema["objects"]:
            print(f'Generating {obj["name"]}')
            obj_path = objects_path.joinpath(
                camel_case_to_snake_case(obj["name"]) + ".py"
            )

            with open(obj_path, "w", encoding="utf8") as obj_file:
                obj_file.write(generate_object(**obj))

        # generate init file
        init_path = objects_path.joinpath("__init__.py")
        with open(init_path, "w", encoding="utf8") as init_file:
            for obj in schema["objects"]:
                init_file.write(
                    f'from .{camel_case_to_snake_case(obj["name"])} '
                    f'import {camel_case_to_pascal_case(obj["name"])}\n'
                )
            init_file.write("\n")
            init_file.write("__all__ = [\n")

            for obj in schema["objects"]:
                init_file.write(f"{tab}'{camel_case_to_pascal_case(obj['name'])}',\n")
            init_file.write("]\n")

    # parsing methods
    if not objects_only:
        methods_path = output_dir.joinpath("methods")

        if not methods_path.exists():
            methods_path.mkdir()

        for method in schema["methods"]:
            print(f'Generating {method["name"]}')
            method_path = methods_path.joinpath(
                camel_case_to_snake_case(method["name"]) + ".py"
            )

            with open(method_path, "w", encoding="utf8") as method_file:
                method_file.write(generate_method(**method))

        # generate init file
        init_path = methods_path.joinpath("__init__.py")
        with open(init_path, "w", encoding="utf8") as init_file:
            for obj in schema["methods"]:
                init_file.write(
                    f'from .{camel_case_to_snake_case(obj["name"])} '
                    f'import {camel_case_to_pascal_case(obj["name"])}\n'
                )
            init_file.write("\n")
            init_file.write("__all__ = [\n")

            for obj in schema["methods"]:
                init_file.write(f"{tab}'{camel_case_to_pascal_case(obj['name'])}',\n")
            init_file.write("]\n")


if __name__ == "__main__":
    main(methods_only=True)
