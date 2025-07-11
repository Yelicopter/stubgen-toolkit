import warnings
from enum import Enum
from typing import Any, Callable, Dict, List, Optional, Sequence, Union

from fastapi.openapi.models import Example
from pydantic.fields import FieldInfo
from typing_extensions import Annotated, deprecated

from ._compat import (
    PYDANTIC_V2,
    PYDANTIC_VERSION_MINOR_TUPLE,
    Undefined,
)

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
        annotation: Optional[Any] = ...,
        alias: Optional[str] = ...,
        alias_priority: Optional[int] = ...,
        validation_alias: Optional[str] = ...,
        serialization_alias: Optional[str] = ...,
        title: Optional[str] = ...,
        description: Optional[str] = ...,
        gt: Optional[float] = ...,
        ge: Optional[float] = ...,
        lt: Optional[float] = ...,
        le: Optional[float] = ...,
        min_length: Optional[int] = ...,
        max_length: Optional[int] = ...,
        pattern: Optional[str] = ...,
        regex: Optional[str] = ...,
        discriminator: Optional[str] = ...,
        strict: Optional[bool] = ...,
        multiple_of: Optional[float] = ...,
        allow_inf_nan: Optional[bool] = ...,
        max_digits: Optional[int] = ...,
        decimal_places: Optional[int] = ...,
        examples: Optional[List[Any]] = ...,
        example: Any = ...,
        openapi_examples: Optional[Dict[str, Example]] = ...,
        deprecated: Optional[bool] = ...,
        include_in_schema: bool = ...,
        json_schema_extra: Optional[Dict[str, Any]] = ...,
        **extra: Any,
    ) -> None:
        ...

    def __repr__(self) -> str:
        ...

class Path(Param):
    in_: ParamTypes

    def __init__(
        self,
        default: Any = ...,
        *,
        default_factory: Optional[Callable[[], Any]] = ...,
        annotation: Optional[Any] = ...,
        alias: Optional[str] = ...,
        alias_priority: Optional[int] = ...,
        validation_alias: Optional[str] = ...,
        serialization_alias: Optional[str] = ...,
        title: Optional[str] = ...,
        description: Optional[str] = ...,
        gt: Optional[float] = ...,
        ge: Optional[float] = ...,
        lt: Optional[float] = ...,
        le: Optional[float] = ...,
        min_length: Optional[int] = ...,
        max_length: Optional[int] = ...,
        pattern: Optional[str] = ...,
        regex: Optional[str] = ...,
        discriminator: Optional[str] = ...,
        strict: Optional[bool] = ...,
        multiple_of: Optional[float] = ...,
        allow_inf_nan: Optional[bool] = ...,
        max_digits: Optional[int] = ...,
        decimal_places: Optional[int] = ...,
        examples: Optional[List[Any]] = ...,
        example: Any = ...,
        openapi_examples: Optional[Dict[str, Example]] = ...,
        deprecated: Optional[bool] = ...,
        include_in_schema: bool = ...,
        json_schema_extra: Optional[Dict[str, Any]] = ...,
        **extra: Any,
    ) -> None:
        ...

class Query(Param):
    in_: ParamTypes

    def __init__(
        self,
        default: Any = ...,
        *,
        default_factory: Optional[Callable[[], Any]] = ...,
        annotation: Optional[Any] = ...,
        alias: Optional[str] = ...,
        alias_priority: Optional[int] = ...,
        validation_alias: Optional[str] = ...,
        serialization_alias: Optional[str] = ...,
        title: Optional[str] = ...,
        description: Optional[str] = ...,
        gt: Optional[float] = ...,
        ge: Optional[float] = ...,
        lt: Optional[float] = ...,
        le: Optional[float] = ...,
        min_length: Optional[int] = ...,
        max_length: Optional[int] = ...,
        pattern: Optional[str] = ...,
        regex: Optional[str] = ...,
        discriminator: Optional[str] = ...,
        strict: Optional[bool] = ...,
        multiple_of: Optional[float] = ...,
        allow_inf_nan: Optional[bool] = ...,
        max_digits: Optional[int] = ...,
        decimal_places: Optional[int] = ...,
        examples: Optional[List[Any]] = ...,
        example: Any = ...,
        openapi_examples: Optional[Dict[str, Example]] = ...,
        deprecated: Optional[bool] = ...,
        include_in_schema: bool = ...,
        json_schema_extra: Optional[Dict[str, Any]] = ...,
        **extra: Any,
    ) -> None:
        ...

class Header(Param):
    in_: ParamTypes

    def __init__(
        self,
        default: Any = ...,
        *,
        default_factory: Optional[Callable[[], Any]] = ...,
        annotation: Optional[Any] = ...,
        alias: Optional[str] = ...,
        alias_priority: Optional[int] = ...,
        validation_alias: Optional[str] = ...,
        serialization_alias: Optional[str] = ...,
        convert_underscores: bool = ...,
        title: Optional[str] = ...,
        description: Optional[str] = ...,
        gt: Optional[float] = ...,
        ge: Optional[float] = ...,
        lt: Optional[float] = ...,
        le: Optional[float] = ...,
        min_length: Optional[int] = ...,
        max_length: Optional[int] = ...,
        pattern: Optional[str] = ...,
        regex: Optional[str] = ...,
        discriminator: Optional[str] = ...,
        strict: Optional[bool] = ...,
        multiple_of: Optional[float] = ...,
        allow_inf_nan: Optional[bool] = ...,
        max_digits: Optional[int] = ...,
        decimal_places: Optional[int] = ...,
        examples: Optional[List[Any]] = ...,
        example: Any = ...,
        openapi_examples: Optional[Dict[str, Example]] = ...,
        deprecated: Optional[bool] = ...,
        include_in_schema: bool = ...,
        json_schema_extra: Optional[Dict[str, Any]] = ...,
        **extra: Any,
    ) -> None:
        ...

class Cookie(Param):
    in_: ParamTypes

    def __init__(
        self,
        default: Any = ...,
        *,
        default_factory: Optional[Callable[[], Any]] = ...,
        annotation: Optional[Any] = ...,
        alias: Optional[str] = ...,
        alias_priority: Optional[int] = ...,
        validation_alias: Optional[str] = ...,
        serialization_alias: Optional[str] = ...,
        title: Optional[str] = ...,
        description: Optional[str] = ...,
        gt: Optional[float] = ...,
        ge: Optional[float] = ...,
        lt: Optional[float] = ...,
        le: Optional[float] = ...,
        min_length: Optional[int] = ...,
        max_length: Optional[int] = ...,
        pattern: Optional[str] = ...,
        regex: Optional[str] = ...,
        discriminator: Optional[str] = ...,
        strict: Optional[bool] = ...,
        multiple_of: Optional[float] = ...,
        allow_inf_nan: Optional[bool] = ...,
        max_digits: Optional[int] = ...,
        decimal_places: Optional[int] = ...,
        examples: Optional[List[Any]] = ...,
        example: Any = ...,
        openapi_examples: Optional[Dict[str, Example]] = ...,
        deprecated: Optional[bool] = ...,
        include_in_schema: bool = ...,
        json_schema_extra: Optional[Dict[str, Any]] = ...,
        **extra: Any,
    ) -> None:
        ...

class Body(FieldInfo):
    def __init__(
        self,
        default: Any = ...,
        *,
        default_factory: Optional[Callable[[], Any]] = ...,
        annotation: Optional[Any] = ...,
        embed: Optional[bool] = ...,
        media_type: str = ...,
        alias: Optional[str] = ...,
        alias_priority: Optional[int] = ...,
        validation_alias: Optional[str] = ...,
        serialization_alias: Optional[str] = ...,
        title: Optional[str] = ...,
        description: Optional[str] = ...,
        gt: Optional[float] = ...,
        ge: Optional[float] = ...,
        lt: Optional[float] = ...,
        le: Optional[float] = ...,
        min_length: Optional[int] = ...,
        max_length: Optional[int] = ...,
        pattern: Optional[str] = ...,
        regex: Optional[str] = ...,
        discriminator: Optional[str] = ...,
        strict: Optional[bool] = ...,
        multiple_of: Optional[float] = ...,
        allow_inf_nan: Optional[bool] = ...,
        max_digits: Optional[int] = ...,
        decimal_places: Optional[int] = ...,
        examples: Optional[List[Any]] = ...,
        example: Any = ...,
        openapi_examples: Optional[Dict[str, Example]] = ...,
        deprecated: Optional[bool] = ...,
        include_in_schema: bool = ...,
        json_schema_extra: Optional[Dict[str, Any]] = ...,
        **extra: Any,
    ) -> None:
        ...

    def __repr__(self) -> str:
        ...

class Form(Body):
    def __init__(
        self,
        default: Any = ...,
        *,
        default_factory: Optional[Callable[[], Any]] = ...,
        annotation: Optional[Any] = ...,
        media_type: str = ...,
        alias: Optional[str] = ...,
        alias_priority: Optional[int] = ...,
        validation_alias: Optional[str] = ...,
        serialization_alias: Optional[str] = ...,
        title: Optional[str] = ...,
        description: Optional[str] = ...,
        gt: Optional[float] = ...,
        ge: Optional[float] = ...,
        lt: Optional[float] = ...,
        le: Optional[float] = ...,
        min_length: Optional[int] = ...,
        max_length: Optional[int] = ...,
        pattern: Optional[str] = ...,
        regex: Optional[str] = ...,
        discriminator: Optional[str] = ...,
        strict: Optional[bool] = ...,
        multiple_of: Optional[float] = ...,
        allow_inf_nan: Optional[bool] = ...,
        max_digits: Optional[int] = ...,
        decimal_places: Optional[int] = ...,
        examples: Optional[List[Any]] = ...,
        example: Any = ...,
        openapi_examples: Optional[Dict[str, Example]] = ...,
        deprecated: Optional[bool] = ...,
        include_in_schema: bool = ...,
        json_schema_extra: Optional[Dict[str, Any]] = ...,
        **extra: Any,
    ) -> None:
        ...

class File(Form):
    def __init__(
        self,
        default: Any = ...,
        *,
        default_factory: Optional[Callable[[], Any]] = ...,
        annotation: Optional[Any] = ...,
        media_type: str = ...,
        alias: Optional[str] = ...,
        alias_priority: Optional[int] = ...,
        validation_alias: Optional[str] = ...,
        serialization_alias: Optional[str] = ...,
        title: Optional[str] = ...,
        description: Optional[str] = ...,
        gt: Optional[float] = ...,
        ge: Optional[float] = ...,
        lt: Optional[float] = ...,
        le: Optional[float] = ...,
        min_length: Optional[int] = ...,
        max_length: Optional[int] = ...,
        pattern: Optional[str] = ...,
        regex: Optional[str] = ...,
        discriminator: Optional[str] = ...,
        strict: Optional[bool] = ...,
        multiple_of: Optional[float] = ...,
        allow_inf_nan: Optional[bool] = ...,
        max_digits: Optional[int] = ...,
        decimal_places: Optional[int] = ...,
        examples: Optional[List[Any]] = ...,
        example: Any = ...,
        openapi_examples: Optional[Dict[str, Example]] = ...,
        deprecated: Optional[bool] = ...,
        include_in_schema: bool = ...,
        json_schema_extra: Optional[Dict[str, Any]] = ...,
        **extra: Any,
    ) -> None:
        ...

class Depends:
    def __init__(
        self, dependency: Optional[Callable[..., Any]] = ..., *, use_cache: bool = ...
    ) -> None:
        ...

    def __repr__(self) -> str:
        ...

class Security(Depends):
    def __init__(
        self,
        dependency: Optional[Callable[..., Any]] = ...,
        *,
        scopes: Optional[Sequence[str]] = ...,
        use_cache: bool = ...,
    ) -> None:
        ...