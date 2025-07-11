from typing import (
    Any,
    BinaryIO,
    Callable,
    Dict,
    Iterable,
    Optional,
    Type,
    TypeVar,
)

from fastapi._compat import (
    PYDANTIC_V2,
    CoreSchema,
    GetJsonSchemaHandler,
    JsonSchemaValue,
    with_info_plain_validator_function,
)
from starlette.datastructures import (
    Address as Address, 
    FormData as FormData, 
    Headers as Headers, 
    QueryParams as QueryParams, 
    State as State, 
    URL as URL, 
    UploadFile as StarletteUploadFile,
)

class UploadFile(StarletteUploadFile):
    ...