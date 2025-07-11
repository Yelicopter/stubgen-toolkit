from typing import Any, Callable, Dict, List, Optional, Sequence, Union

from fastapi.openapi.models import Example
from pydantic.fields import FieldInfo
from typing_extensions import Annotated, deprecated

_Unset = Union[None, object]

class ParamTypes(Enum):
    query = "query"
    header = "header"
    path = "path"
    cookie = "cookie"

class Param(FieldInfo):
    pass

    def __init__(
        self,
        default: Any = None,
        *,
        default_factory: Optional[Callable] = None,
        annotation: Optional[Any] = None,
        alias: Optional[str] = None,
        alias_priority: Optional[int] = None,
        validation_alias: Optional[str] = None,
        serialization_alias: Optional[str] = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        gt: Optional[Any] = None,
        ge: Optional[Any] = None,
        lt: Optional[Any] = None,
        le: Optional[Any] = None,
        min_length: Optional[int] = None,
        max_length: Optional[int] = None,
        pattern: Optional[str] = None,
        regex: Optional[str] = None,
        discriminator: Optional[str] = None,
        strict: Optional[bool] = None,
        multiple_of: Optional[Any] = None,
        allow_inf_nan: Optional[bool] = None,
        max_digits: Optional[int] = None,
        decimal_places: Optional[int] = None,
        examples: Optional[Dict[str, Any]] = None,
        example: Optional[Any] = None,
        openapi_examples: Optional[Dict[str, Any]] = None,
        deprecated: Optional[bool] = None,
        include_in_schema: bool = True,
        json_schema_extra: Optional[Dict[str, Any]] = None,
        **extra: Any,
    ) -> None:
        ...

class Path(Param):
    in_ = ParamTypes.path

class Query(Param):
    in_ = ParamTypes.query

class Header(Param):
    in_ = ParamTypes.header

class Cookie(Param):
    in_ = ParamTypes.cookie

class Body(FieldInfo):
    def __init__(
        self,
        default: Any = None,
        *,
        default_factory: Optional[Callable] = None,
        annotation: Optional[Any] = None,
        embed: Optional[bool] = None,
        media_type: str = "application/json",
        alias: Optional[str] = None,
        alias_priority: Optional[int] = None,
        validation_alias: Optional[str] = None,
        serialization_alias: Optional[str] = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        gt: Optional[Any] = None,
        ge: Optional[Any] = None,
        lt: Optional[Any] = None,
        le: Optional[Any] = None,
        min_length: Optional[int] = None,
        max_length: Optional[int] = None,
        pattern: Optional[str] = None,
        regex: Optional[str] = None,
        discriminator: Optional[str] = None,
        strict: Optional[bool] = None,
        multiple_of: Optional[Any] = None,
        allow_inf_nan: Optional[bool] = None,
        max_digits: Optional[int] = None,
        decimal_places: Optional[int] = None,
        examples: Optional[Dict[str, Any]] = None,
        example: Optional[Any] = None,
        openapi_examples: Optional[Dict[str, Any]] = None,
        deprecated: Optional[bool] = None,
        include_in_schema: bool = True,
        json_schema_extra: Optional[Dict[str, Any]] = None,
        **extra: Any,
    ) -> None:
        ...

class Form(Body):
    ...

class File(Form):
    ...

class Depends:
    def __init__(
        self,
        dependency: Optional[Callable] = None,
        *,
        use_cache: bool = True,
    ) -> None:
        ...

class Security(Depends):
    ...