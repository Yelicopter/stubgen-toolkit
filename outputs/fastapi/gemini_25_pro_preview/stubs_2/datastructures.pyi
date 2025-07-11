from typing import (
    Any,
    BinaryIO,
    Callable,
    Dict,
    Generic,
    Iterable,
    Optional,
    Type,
    TypeVar,
    Union,
    cast,
)

from fastapi._compat import (
    PYDANTIC_V2,
    CoreSchema,
    GetJsonSchemaHandler,
    JsonSchemaValue,
    with_info_plain_validator_function,
)
from starlette.datastructures import URL as URL
from starlette.datastructures import Address as Address
from starlette.datastructures import FormData as FormData
from starlette.datastructures import Headers as Headers
from starlette.datastructures import QueryParams as QueryParams
from starlette.datastructures import State as State
from starlette.datastructures import UploadFile as StarletteUploadFile

class UploadFile(StarletteUploadFile):
    file: BinaryIO
    filename: Optional[str]
    size: Optional[int]
    headers: Headers
    content_type: Optional[str]
    async def write(self, data: Union[bytes, str]) -> None: ...
    async def read(self, size: int = -1) -> bytes: ...
    async def seek(self, offset: int) -> Any: ...
    async def close(self) -> None: ...
    @classmethod
    def __get_validators__(cls: Type["UploadFile"]) -> Iterable[Callable[[Any], Any]]: ...
    @classmethod
    def validate(cls: Type["UploadFile"], v: Any) -> "UploadFile": ...
    @classmethod
    def _validate(cls: Type["UploadFile"], __input_value: Any, _: Any) -> "UploadFile": ...
    if not PYDANTIC_V2:
        @classmethod
        def __modify_schema__(
            cls: Type["UploadFile"], field_schema: Dict[str, Any]
        ) -> None: ...
    @classmethod
    def __get_pydantic_json_schema__(
        cls: Type["UploadFile"], core_schema: CoreSchema, handler: GetJsonSchemaHandler
    ) -> JsonSchemaValue: ...
    @classmethod
    def __get_pydantic_core_schema__(
        cls: Type["UploadFile"], source: Type[Any], handler: Callable[[Any], CoreSchema]
    ) -> CoreSchema: ...

DefaultType = TypeVar("DefaultType")

class DefaultPlaceholder(Generic[DefaultType]):
    value: DefaultType
    def __init__(self, value: DefaultType) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, o: object) -> bool: ...

def Default(value: DefaultType) -> DefaultPlaceholder[DefaultType]: ...