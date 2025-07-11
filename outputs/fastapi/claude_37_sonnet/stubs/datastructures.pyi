from typing import Any, BinaryIO, Callable, Dict, Iterable, Optional, Type, TypeVar, cast

from fastapi._compat import (
    PYDANTIC_V2,
    CoreSchema,
    GetJsonSchemaHandler,
    JsonSchemaValue,
    with_info_plain_validator_function,
)
from starlette.datastructures import URL
from starlette.datastructures import Address
from starlette.datastructures import FormData
from starlette.datastructures import Headers
from starlette.datastructures import QueryParams
from starlette.datastructures import State
from starlette.datastructures import UploadFile as StarletteUploadFile
from typing_extensions import Annotated, Doc

class UploadFile(StarletteUploadFile):
    file: Annotated[BinaryIO, Doc("The standard Python file object (non-async).")]
    filename: Annotated[Optional[str], Doc("The original file name.")]
    size: Annotated[Optional[int], Doc("The size of the file in bytes.")]
    headers: Annotated[Headers, Doc("The headers of the request.")]
    content_type: Annotated[Optional[str], Doc("The content type of the request, from the headers.")]

    async def write(
        self,
        data: bytes,
    ) -> None: ...
    async def read(
        self,
        size: int = ...,
    ) -> bytes: ...
    async def seek(
        self,
        offset: int,
    ) -> None: ...
    async def close(self) -> None: ...
    @classmethod
    def __get_validators__(cls: Type[UploadFile]) -> Iterable[Callable[[Any], Any]]: ...
    @classmethod
    def validate(cls: Type[UploadFile], v: Any) -> Any: ...
    @classmethod
    def _validate(cls, __input_value: Any, _: Any) -> UploadFile: ...
    @classmethod
    def __get_pydantic_json_schema__(
        cls, core_schema: CoreSchema, handler: GetJsonSchemaHandler
    ) -> JsonSchemaValue: ...
    @classmethod
    def __get_pydantic_core_schema__(
        cls, source: Any, handler: Any
    ) -> CoreSchema: ...

class DefaultPlaceholder:
    def __init__(self, value: Any): ...
    def __bool__(self) -> bool: ...
    def __eq__(self, o: object) -> bool: ...

DefaultType = TypeVar("DefaultType")

def Default(value: DefaultType) -> DefaultType: ...