import dataclasses
import io
import pathlib
from typing import Any, Optional, overload
import uuid

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject


@dataclasses.dataclass(repr=True)
class InputFile(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object represents the contents of a file to be uploaded. Must be posted using multipart/form-data in the usual way that files are uploaded via the browser.

    More info at: https://core.telegram.org/bots/api/#inputfile
    """

    @overload
    def __init__(self, file: io.BufferedReader, filename: str) -> None:
        ...

    @overload
    def __init__(self, file: pathlib.Path, filename: Optional[str] = None) -> None:
        ...

    def __init__(
        self, file: pathlib.Path | io.BufferedReader, filename: Optional[str] = None
    ) -> None:

        if isinstance(file, io.BufferedReader):
            self._file: Optional[io.BufferedReader] = file
            self._path: Optional[pathlib.Path] = None
            if not filename:
                raise ValueError(
                    "filename must be provided when file is a BufferedReader"
                )
            self._filename = filename

        elif isinstance(file, pathlib.Path):  # type: ignore
            self._file = None
            self._path = file
            if not filename:
                self._filename = file.name
            else:
                self._filename = filename

        else:
            raise TypeError(
                f"file must be a pathlib.Path or io.BufferedReader, got {type(file)}"
            )

    def __enter__(self):
        if self._file:
            self.file = self._file
            return self
        else:
            if not self._path:
                raise ValueError("path must be provided when file is None")

            self._file = self._path.open(mode="rb")
            self.file = self._file
            return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any):
        self.close()

    def close(self):
        if self._file:
            self._file.close()

    @property
    def ensured_file(self) -> io.BufferedReader:
        if not self._file:
            raise ValueError("File not provided or it's not opened")
        return self._file

    def serialize(
        self,
        is_multipart_obj: bool = False,
        master_obj: Any = None,
        parent_key: Optional[str] = None,
    ) -> dict[str, Any] | Any:

        if isinstance(master_obj, TelegramBotsObject):
            key = str(uuid.uuid4())
            master_obj.append_list_metadata(
                "files", (key, self._filename, self.ensured_file)
            )
            master_obj.append_list_metadata("dispose_these", self)
            return "attach://" + key
        else:
            return self.ensured_file
