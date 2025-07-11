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
    Address as Address,  # noqa: F401
    FormData as FormData,  # noqa: F401
    Headers as Headers,  # noqa: F401
    QueryParams as QueryParams,  # noqa: F401
    State as State,  # noqa: F401
    URL as URL,  # noqa: F401
    UploadFile as StarletteUploadFile,
)
from typing_extensions import Annotated, Doc

class UploadFile(StarletteUploadFile):
    ...