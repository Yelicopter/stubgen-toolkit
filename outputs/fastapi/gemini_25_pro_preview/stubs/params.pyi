import warnings
from enum import Enum
from typing import Any, Callable, Dict, List, Optional, Sequence, Union

from fastapi.openapi.models import Example
from pydantic.fields import FieldInfo
from typing_extensions import Annotated, deprecated

from ._compat import PYDANTIC_V2, PYDANTIC_VERSION_MINOR_TUPLE, Undefined

_Unset: Any

class ParamTypes(Enum):
    query: str
    header: str
    path: str
    cookie: str

class Param(FieldInfo):
    in_: ParamTypes
    def __init__(
        self,
        default: Any = ...,
        *,
        default_factory: Optional[Callable[[], Any]] = ...,
        annotation: Optional[type] = None,
        alias: Optional[str] = None,
        alias_priority: Optional[int] = ...,
        validation_alias: Optional[str] = None,
        serialization_alias: Optional[str] = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        gt: Optional[float] = None,
        ge: Optional[float] = None,
        lt: Optional[float] = None,
        le: Optional[float] = None,
        min_length: Optional[int] = None,
        max_length: Optional[int] = None,
        pattern: Optional[str] = None,
        regex: Optional[str] = None,
        discriminator: Optional[str] = None,
        strict: Optional[bool] = ...,
        multiple_of: Optional[float] = ...,
        allow_inf_nan: Optional[bool] = ...,
        max_digits: Optional[int] = ...,
        decimal_places: Optional[int] = ...,
        examples: Optional[List[Any]] = None,
        example: Any = ...,
        openapi_examples: Optional[Dict[str, Example]] = None,
        deprecated: Optional[bool] = None,
        include_in_schema: bool = True,
        json_schema_extra: Optional[Dict[str, Any]] = None,
        **extra: Any,
    ) -> None: ...
    def __repr__(self) -> str: ...

class Path(Param):
    in_: ParamTypes
    def __init__(
        self,
        default: Any = ...,
        *,
        default_factory: Optional[Callable[[], Any]] = ...,
        annotation: Optional[type] = None,
        alias: Optional[str] = None,
        alias_priority: Optional[int] = ...,
        validation_alias: Optional[str] = None,
        serialization_alias: Optional[str] = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        gt: Optional[float] = None,
        ge: Optional[float] = None,
        lt: Optional[float] = None,
        le: Optional[float] = None,
        min_length: Optional[int] = None,
        max_length: Optional[int] = None,
        pattern: Optional[str] = None,
        regex: Optional[str] = None,
        discriminator: Optional[str] = None,
        strict: Optional[bool] = ...,
        multiple_of: Optional[float] = ...,
        allow_inf_nan: Optional[bool] = ...,
        max_digits: Optional[int] = ...,
        decimal_places: Optional[int] = ...,
        examples: Optional[List[Any]] = None,
        example: Any = ...,
        openapi_examples: Optional[Dict[str, Example]] = None,
        deprecated: Optional[bool] = None,
        include_in_schema: bool = True,
        json_schema_extra: Optional[Dict[str, Any]] = None,
        **extra: Any,
    ) -> None: ...

class Query(Param):
    in_: ParamTypes
    def __init__(
        self,
        default: Any = ...,
        *,
        default_factory: Optional[Callable[[], Any]] = ...,
        annotation: Optional[type] = None,
        alias: Optional[str] = None,
        alias_priority: Optional[int] = ...,
        validation_alias: Optional[str] = None,
        serialization_alias: Optional[str] = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        gt: Optional[float] = None,
        ge: Optional[float] = None,
        lt: Optional[float] = None,
        le: Optional[float] = None,
        min_length: Optional[int] = None,
        max_length: Optional[int] = None,
        pattern: Optional[str] = None,
        regex: Optional[str] = None,
        discriminator: Optional[str] = None,
        strict: Optional[bool] = ...,
        multiple_of: Optional[float] = ...,
        allow_inf_nan: Optional[bool] = ...,
        max_digits: Optional[int] = ...,
        decimal_places: Optional[int] = ...,
        examples: Optional[List[Any]] = None,
        example: Any = ...,
        openapi_examples: Optional[Dict[str, Example]] = None,
        deprecated: Optional[bool] = None,
        include_in_schema: bool = True,
        json_schema_extra: Optional[Dict[str, Any]] = None,
        **extra: Any,
    ) -> None: ...

class Header(Param):
    in_: ParamTypes
    def __init__(
        self,
        default: Any = ...,
        *,
        default_factory: Optional[Callable[[], Any]] = ...,
        annotation: Optional[type] = None,
        alias: Optional[str] = None,
        alias_priority: Optional[int] = ...,
        validation_alias: Optional[str] = None,
        serialization_alias: Optional[str] = None,
        convert_underscores: bool = True,
        title: Optional[str] = None,
        description: Optional[str] = None,
        gt: Optional[float] = None,
        ge: Optional[float] = None,
        lt: Optional[float] = None,
        le: Optional[float] = None,
        min_length: Optional[int] = None,
        max_length: Optional[int] = None,
        pattern: Optional[str] = None,
        regex: Optional[str] = None,
        discriminator: Optional[str] = None,
        strict: Optional[bool] = ...,
        multiple_of: Optional[float] = ...,
        allow_inf_nan: Optional[bool] = ...,
        max_digits: Optional[int] = ...,
        decimal_places: Optional[int] = ...,
        examples: Optional[List[Any]] = None,
        example: Any = ...,
        openapi_examples: Optional[Dict[str, Example]] = None,
        deprecated: Optional[bool] = None,
        include_in_schema: bool = True,
        json_schema_extra: Optional[Dict[str, Any]] = None,
        **extra: Any,
    ) -> None: ...

class Cookie(Param):
    in_: ParamTypes
    def __init__(
        self,
        default: Any = ...,
        *,
        default_factory: Optional[Callable[[], Any]] = ...,
        annotation: Optional[type] = None,
        alias: Optional[str] = None,
        alias_priority: Optional[int] = ...,
        validation_alias: Optional[str] = None,
        serialization_alias: Optional[str] = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        gt: Optional[float] = None,
        ge: Optional[float] = None,
        lt: Optional[float] = None,
        le: Optional[float] = None,
        min_length: Optional[int] = None,
        max_length: Optional[int] = None,
        pattern: Optional[str] = None,
        regex: Optional[str] = None,
        discriminator: Optional[str] = None,
        strict: Optional[bool] = ...,
        multiple_of: Optional[float] = ...,
        allow_inf_nan: Optional[bool] = ...,
        max_digits: Optional[int] = ...,
        decimal_places: Optional[int] = ...,
        examples: Optional[List[Any]] = None,
        example: Any = ...,
        openapi_examples: Optional[Dict[str, Example]] = None,
        deprecated: Optional[bool] = None,
        include_in_schema: bool = True,
        json_schema_extra: Optional[Dict[str, Any]] = None,
        **extra: Any,
    ) -> None: ...

class Body(FieldInfo):
    def __init__(
        self,
        default: Any = ...,
        *,
        default_factory: Optional[Callable[[], Any]] = ...,
        annotation: Optional[type] = None,
        embed: Optional[bool] = None,
        media_type: str = "application/json",
        alias: Optional[str] = None,
        alias_priority: Optional[int] = ...,
        validation_alias: Optional[str] = None,
        serialization_alias: Optional[str] = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        gt: Optional[float] = None,
        ge: Optional[float] = None,
        lt: Optional[float] = None,
        le: Optional[float] = None,
        min_length: Optional[int] = None,
        max_length: Optional[int] = None,
        pattern: Optional[str] = None,
        regex: Optional[str] = None,
        discriminator: Optional[str] = None,
        strict: Optional[bool] = ...,
        multiple_of: Optional[float] = ...,
        allow_inf_nan: Optional[bool] = ...,
        max_digits: Optional[int] = ...,
        decimal_places: Optional[int] = ...,
        examples: Optional[List[Any]] = None,
        example: Any = ...,
        openapi_examples: Optional[Dict[str, Example]] = None,
        deprecated: Optional[bool] = None,
        include_in_schema: bool = True,
        json_schema_extra: Optional[Dict[str, Any]] = None,
        **extra: Any,
    ) -> None: ...
    def __repr__(self) -> str: ...

class Form(Body):
    def __init__(
        self,
        default: Any = ...,
        *,
        default_factory: Optional[Callable[[], Any]] = ...,
        annotation: Optional[type] = None,
        media_type: str = "application/x-www-form-urlencoded",
        alias: Optional[str] = None,
        alias_priority: Optional[int] = ...,
        validation_alias: Optional[str] = None,
        serialization_alias: Optional[str] = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        gt: Optional[float] = None,
        ge: Optional[float] = None,
        lt: Optional[float] = None,
        le: Optional[float] = None,
        min_length: Optional[int] = None,
        max_length: Optional[int] = None,
        pattern: Optional[str] = None,
        regex: Optional[str] = None,
        discriminator: Optional[str] = None,
        strict: Optional[bool] = ...,
        multiple_of: Optional[float] = ...,
        allow_inf_nan: Optional[bool] = ...,
        max_digits: Optional[int] = ...,
        decimal_places: Optional[int] = ...,
        examples: Optional[List[Any]] = None,
        example: Any = ...,
        openapi_examples: Optional[Dict[str, Example]] = None,
        deprecated: Optional[bool] = None,
        include_in_schema: bool = True,
        json_schema_extra: Optional[Dict[str, Any]] = None,
        **extra: Any,
    ) -> None: ...

class File(Form):
    def __init__(
        self,
        default: Any = ...,
        *,
        default_factory: Optional[Callable[[], Any]] = ...,
        annotation: Optional[type] = None,
        media_type: str = "multipart/form-data",
        alias: Optional[str] = None,
        alias_priority: Optional[int] = ...,
        validation_alias: Optional[str] = None,
        serialization_alias: Optional[str] = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        gt: Optional[float] = None,
        ge: Optional[float] = None,
        lt: Optional[float] = None,
        le: Optional[float] = None,
        min_length: Optional[int] = None,
        max_length: Optional[int] = None,
        pattern: Optional[str] = None,
        regex: Optional[str] = None,
        discriminator: Optional[str] = None,
        strict: Optional[bool] = ...,
        multiple_of: Optional[float] = ...,
        allow_inf_nan: Optional[bool] = ...,
        max_digits: Optional[int] = ...,
        decimal_places: Optional[int] = ...,
        examples: Optional[List[Any]] = None,
        example: Any = ...,
        openapi_examples: Optional[Dict[str, Example]] = None,
        deprecated: Optional[bool] = None,
        include_in_schema: bool = True,
        json_schema_extra: Optional[Dict[str, Any]] = None,
        **extra: Any,
    ) -> None: ...

class Depends:
    dependency: Optional[Callable[..., Any]]
    use_cache: bool
    def __init__(
        self, dependency: Optional[Callable[..., Any]] = None, *, use_cache: bool = True
    ) -> None: ...
    def __repr__(self) -> str: ...

class Security(Depends):
    scopes: Sequence[str]
    def __init__(
        self,
        dependency: Optional[Callable[..., Any]] = None,
        *,
        scopes: Optional[Sequence[str]] = None,
        use_cache: bool = True,
    ) -> None: ...