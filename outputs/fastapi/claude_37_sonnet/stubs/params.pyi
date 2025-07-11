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
    query = "query"
    header = "header"
    path = "path"
    cookie = "cookie"

class Param(FieldInfo):
    in_: ParamTypes

    def __init__(
        self,
        default: Any = Undefined,
        *,
        default_factory: Optional[Callable[[], Any]] = _Unset,
        annotation: Any = None,
        alias: Optional[str] = None,
        alias_priority: Any = _Unset,
        validation_alias: Any = None,
        serialization_alias: Any = None,
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
        discriminator: Any = None,
        strict: Any = _Unset,
        multiple_of: Any = _Unset,
        allow_inf_nan: Any = _Unset,
        max_digits: Any = _Unset,
        decimal_places: Any = _Unset,
        examples: Optional[List[Example]] = None,
        example: Any = _Unset,
        openapi_examples: Optional[Dict[str, Example]] = None,
        deprecated: Optional[bool] = None,
        include_in_schema: bool = True,
        json_schema_extra: Optional[Dict[str, Any]] = None,
        **extra: Any,
    ) -> None: ...

    def __repr__(self) -> str: ...

class Path(Param):
    in_: ParamTypes = ParamTypes.path

    def __init__(
        self,
        default: Any = ...,
        *,
        default_factory: Optional[Callable[[], Any]] = _Unset,
        annotation: Any = None,
        alias: Optional[str] = None,
        alias_priority: Any = _Unset,
        validation_alias: Any = None,
        serialization_alias: Any = None,
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
        discriminator: Any = None,
        strict: Any = _Unset,
        multiple_of: Any = _Unset,
        allow_inf_nan: Any = _Unset,
        max_digits: Any = _Unset,
        decimal_places: Any = _Unset,
        examples: Optional[List[Example]] = None,
        example: Any = _Unset,
        openapi_examples: Optional[Dict[str, Example]] = None,
        deprecated: Optional[bool] = None,
        include_in_schema: bool = True,
        json_schema_extra: Optional[Dict[str, Any]] = None,
        **extra: Any,
    ) -> None: ...

class Query(Param):
    in_: ParamTypes = ParamTypes.query

    def __init__(
        self,
        default: Any = Undefined,
        *,
        default_factory: Optional[Callable[[], Any]] = _Unset,
        annotation: Any = None,
        alias: Optional[str] = None,
        alias_priority: Any = _Unset,
        validation_alias: Any = None,
        serialization_alias: Any = None,
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
        discriminator: Any = None,
        strict: Any = _Unset,
        multiple_of: Any = _Unset,
        allow_inf_nan: Any = _Unset,
        max_digits: Any = _Unset,
        decimal_places: Any = _Unset,
        examples: Optional[List[Example]] = None,
        example: Any = _Unset,
        openapi_examples: Optional[Dict[str, Example]] = None,
        deprecated: Optional[bool] = None,
        include_in_schema: bool = True,
        json_schema_extra: Optional[Dict[str, Any]] = None,
        **extra: Any,
    ) -> None: ...

class Header(Param):
    in_: ParamTypes = ParamTypes.header

    def __init__(
        self,
        default: Any = Undefined,
        *,
        default_factory: Optional[Callable[[], Any]] = _Unset,
        annotation: Any = None,
        alias: Optional[str] = None,
        alias_priority: Any = _Unset,
        validation_alias: Any = None,
        serialization_alias: Any = None,
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
        discriminator: Any = None,
        strict: Any = _Unset,
        multiple_of: Any = _Unset,
        allow_inf_nan: Any = _Unset,
        max_digits: Any = _Unset,
        decimal_places: Any = _Unset,
        examples: Optional[List[Example]] = None,
        example: Any = _Unset,
        openapi_examples: Optional[Dict[str, Example]] = None,
        deprecated: Optional[bool] = None,
        include_in_schema: bool = True,
        json_schema_extra: Optional[Dict[str, Any]] = None,
        **extra: Any,
    ) -> None: ...

class Cookie(Param):
    in_: ParamTypes = ParamTypes.cookie

    def __init__(
        self,
        default: Any = Undefined,
        *,
        default_factory: Optional[Callable[[], Any]] = _Unset,
        annotation: Any = None,
        alias: Optional[str] = None,
        alias_priority: Any = _Unset,
        validation_alias: Any = None,
        serialization_alias: Any = None,
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
        discriminator: Any = None,
        strict: Any = _Unset,
        multiple_of: Any = _Unset,
        allow_inf_nan: Any = _Unset,
        max_digits: Any = _Unset,
        decimal_places: Any = _Unset,
        examples: Optional[List[Example]] = None,
        example: Any = _Unset,
        openapi_examples: Optional[Dict[str, Example]] = None,
        deprecated: Optional[bool] = None,
        include_in_schema: bool = True,
        json_schema_extra: Optional[Dict[str, Any]] = None,
        **extra: Any,
    ) -> None: ...

class Body(FieldInfo):
    def __init__(
        self,
        default: Any = Undefined,
        *,
        default_factory: Optional[Callable[[], Any]] = _Unset,
        annotation: Any = None,
        embed: Optional[bool] = None,
        media_type: str = "application/json",
        alias: Optional[str] = None,
        alias_priority: Any = _Unset,
        validation_alias: Any = None,
        serialization_alias: Any = None,
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
        discriminator: Any = None,
        strict: Any = _Unset,
        multiple_of: Any = _Unset,
        allow_inf_nan: Any = _Unset,
        max_digits: Any = _Unset,
        decimal_places: Any = _Unset,
        examples: Optional[List[Example]] = None,
        example: Any = _Unset,
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
        default: Any = Undefined,
        *,
        default_factory: Optional[Callable[[], Any]] = _Unset,
        annotation: Any = None,
        media_type: str = "application/x-www-form-urlencoded",
        alias: Optional[str] = None,
        alias_priority: Any = _Unset,
        validation_alias: Any = None,
        serialization_alias: Any = None,
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
        discriminator: Any = None,
        strict: Any = _Unset,
        multiple_of: Any = _Unset,
        allow_inf_nan: Any = _Unset,
        max_digits: Any = _Unset,
        decimal_places: Any = _Unset,
        examples: Optional[List[Example]] = None,
        example: Any = _Unset,
        openapi_examples: Optional[Dict[str, Example]] = None,
        deprecated: Optional[bool] = None,
        include_in_schema: bool = True,
        json_schema_extra: Optional[Dict[str, Any]] = None,
        **extra: Any,
    ) -> None: ...

class File(Form):
    def __init__(
        self,
        default: Any = Undefined,
        *,
        default_factory: Optional[Callable[[], Any]] = _Unset,
        annotation: Any = None,
        media_type: str = "multipart/form-data",
        alias: Optional[str] = None,
        alias_priority: Any = _Unset,
        validation_alias: Any = None,
        serialization_alias: Any = None,
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
        discriminator: Any = None,
        strict: Any = _Unset,
        multiple_of: Any = _Unset,
        allow_inf_nan: Any = _Unset,
        max_digits: Any = _Unset,
        decimal_places: Any = _Unset,
        examples: Optional[List[Example]] = None,
        example: Any = _Unset,
        openapi_examples: Optional[Dict[str, Example]] = None,
        deprecated: Optional[bool] = None,
        include_in_schema: bool = True,
        json_schema_extra: Optional[Dict[str, Any]] = None,
        **extra: Any,
    ) -> None: ...

class Depends:
    def __init__(
        self, dependency: Optional[Callable[..., Any]] = None, *, use_cache: bool = True
    ) -> None: ...

    def __repr__(self) -> str: ...

class Security(Depends):
    def __init__(
        self,
        dependency: Optional[Callable[..., Any]] = None,
        *,
        scopes: Optional[List[str]] = None,
        use_cache: bool = True,
    ) -> None: ...