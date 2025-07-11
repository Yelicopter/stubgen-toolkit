from ._compat import PYDANTIC_V2 as PYDANTIC_V2, PYDANTIC_VERSION_MINOR_TUPLE as PYDANTIC_VERSION_MINOR_TUPLE, Undefined as Undefined
from enum import Enum
from fastapi.openapi.models import Example as Example
from pydantic.fields import FieldInfo
from typing import Any, Callable, Dict, List, Optional

class ParamTypes(Enum):
    query: str
    header: str
    path: str
    cookie: str

class Param(FieldInfo):
    in_: ParamTypes
    def __init__(self, default: Any = ..., *, default_factory: Optional[Callable[[], Any]] = ..., annotation: Any = ..., alias: Optional[str] = ..., alias_priority: Any = ..., validation_alias: Any = ..., serialization_alias: Any = ..., title: Optional[str] = ..., description: Optional[str] = ..., gt: Optional[float] = ..., ge: Optional[float] = ..., lt: Optional[float] = ..., le: Optional[float] = ..., min_length: Optional[int] = ..., max_length: Optional[int] = ..., pattern: Optional[str] = ..., regex: Optional[str] = ..., discriminator: Any = ..., strict: Any = ..., multiple_of: Any = ..., allow_inf_nan: Any = ..., max_digits: Any = ..., decimal_places: Any = ..., examples: Optional[List[Example]] = ..., example: Any = ..., openapi_examples: Optional[Dict[str, Example]] = ..., deprecated: Optional[bool] = ..., include_in_schema: bool = ..., json_schema_extra: Optional[Dict[str, Any]] = ..., **extra: Any) -> None: ...

class Path(Param):
    in_: ParamTypes
    def __init__(self, default: Any = ..., *, default_factory: Optional[Callable[[], Any]] = ..., annotation: Any = ..., alias: Optional[str] = ..., alias_priority: Any = ..., validation_alias: Any = ..., serialization_alias: Any = ..., title: Optional[str] = ..., description: Optional[str] = ..., gt: Optional[float] = ..., ge: Optional[float] = ..., lt: Optional[float] = ..., le: Optional[float] = ..., min_length: Optional[int] = ..., max_length: Optional[int] = ..., pattern: Optional[str] = ..., regex: Optional[str] = ..., discriminator: Any = ..., strict: Any = ..., multiple_of: Any = ..., allow_inf_nan: Any = ..., max_digits: Any = ..., decimal_places: Any = ..., examples: Optional[List[Example]] = ..., example: Any = ..., openapi_examples: Optional[Dict[str, Example]] = ..., deprecated: Optional[bool] = ..., include_in_schema: bool = ..., json_schema_extra: Optional[Dict[str, Any]] = ..., **extra: Any) -> None: ...

class Query(Param):
    in_: ParamTypes
    def __init__(self, default: Any = ..., *, default_factory: Optional[Callable[[], Any]] = ..., annotation: Any = ..., alias: Optional[str] = ..., alias_priority: Any = ..., validation_alias: Any = ..., serialization_alias: Any = ..., title: Optional[str] = ..., description: Optional[str] = ..., gt: Optional[float] = ..., ge: Optional[float] = ..., lt: Optional[float] = ..., le: Optional[float] = ..., min_length: Optional[int] = ..., max_length: Optional[int] = ..., pattern: Optional[str] = ..., regex: Optional[str] = ..., discriminator: Any = ..., strict: Any = ..., multiple_of: Any = ..., allow_inf_nan: Any = ..., max_digits: Any = ..., decimal_places: Any = ..., examples: Optional[List[Example]] = ..., example: Any = ..., openapi_examples: Optional[Dict[str, Example]] = ..., deprecated: Optional[bool] = ..., include_in_schema: bool = ..., json_schema_extra: Optional[Dict[str, Any]] = ..., **extra: Any) -> None: ...

class Header(Param):
    in_: ParamTypes
    def __init__(self, default: Any = ..., *, default_factory: Optional[Callable[[], Any]] = ..., annotation: Any = ..., alias: Optional[str] = ..., alias_priority: Any = ..., validation_alias: Any = ..., serialization_alias: Any = ..., convert_underscores: bool = ..., title: Optional[str] = ..., description: Optional[str] = ..., gt: Optional[float] = ..., ge: Optional[float] = ..., lt: Optional[float] = ..., le: Optional[float] = ..., min_length: Optional[int] = ..., max_length: Optional[int] = ..., pattern: Optional[str] = ..., regex: Optional[str] = ..., discriminator: Any = ..., strict: Any = ..., multiple_of: Any = ..., allow_inf_nan: Any = ..., max_digits: Any = ..., decimal_places: Any = ..., examples: Optional[List[Example]] = ..., example: Any = ..., openapi_examples: Optional[Dict[str, Example]] = ..., deprecated: Optional[bool] = ..., include_in_schema: bool = ..., json_schema_extra: Optional[Dict[str, Any]] = ..., **extra: Any) -> None: ...

class Cookie(Param):
    in_: ParamTypes
    def __init__(self, default: Any = ..., *, default_factory: Optional[Callable[[], Any]] = ..., annotation: Any = ..., alias: Optional[str] = ..., alias_priority: Any = ..., validation_alias: Any = ..., serialization_alias: Any = ..., title: Optional[str] = ..., description: Optional[str] = ..., gt: Optional[float] = ..., ge: Optional[float] = ..., lt: Optional[float] = ..., le: Optional[float] = ..., min_length: Optional[int] = ..., max_length: Optional[int] = ..., pattern: Optional[str] = ..., regex: Optional[str] = ..., discriminator: Any = ..., strict: Any = ..., multiple_of: Any = ..., allow_inf_nan: Any = ..., max_digits: Any = ..., decimal_places: Any = ..., examples: Optional[List[Example]] = ..., example: Any = ..., openapi_examples: Optional[Dict[str, Example]] = ..., deprecated: Optional[bool] = ..., include_in_schema: bool = ..., json_schema_extra: Optional[Dict[str, Any]] = ..., **extra: Any) -> None: ...

class Body(FieldInfo):
    def __init__(self, default: Any = ..., *, default_factory: Optional[Callable[[], Any]] = ..., annotation: Any = ..., embed: Optional[bool] = ..., media_type: str = ..., alias: Optional[str] = ..., alias_priority: Any = ..., validation_alias: Any = ..., serialization_alias: Any = ..., title: Optional[str] = ..., description: Optional[str] = ..., gt: Optional[float] = ..., ge: Optional[float] = ..., lt: Optional[float] = ..., le: Optional[float] = ..., min_length: Optional[int] = ..., max_length: Optional[int] = ..., pattern: Optional[str] = ..., regex: Optional[str] = ..., discriminator: Any = ..., strict: Any = ..., multiple_of: Any = ..., allow_inf_nan: Any = ..., max_digits: Any = ..., decimal_places: Any = ..., examples: Optional[List[Example]] = ..., example: Any = ..., openapi_examples: Optional[Dict[str, Example]] = ..., deprecated: Optional[bool] = ..., include_in_schema: bool = ..., json_schema_extra: Optional[Dict[str, Any]] = ..., **extra: Any) -> None: ...

class Form(Body):
    def __init__(self, default: Any = ..., *, default_factory: Optional[Callable[[], Any]] = ..., annotation: Any = ..., media_type: str = ..., alias: Optional[str] = ..., alias_priority: Any = ..., validation_alias: Any = ..., serialization_alias: Any = ..., title: Optional[str] = ..., description: Optional[str] = ..., gt: Optional[float] = ..., ge: Optional[float] = ..., lt: Optional[float] = ..., le: Optional[float] = ..., min_length: Optional[int] = ..., max_length: Optional[int] = ..., pattern: Optional[str] = ..., regex: Optional[str] = ..., discriminator: Any = ..., strict: Any = ..., multiple_of: Any = ..., allow_inf_nan: Any = ..., max_digits: Any = ..., decimal_places: Any = ..., examples: Optional[List[Example]] = ..., example: Any = ..., openapi_examples: Optional[Dict[str, Example]] = ..., deprecated: Optional[bool] = ..., include_in_schema: bool = ..., json_schema_extra: Optional[Dict[str, Any]] = ..., **extra: Any) -> None: ...

class File(Form):
    def __init__(self, default: Any = ..., *, default_factory: Optional[Callable[[], Any]] = ..., annotation: Any = ..., media_type: str = ..., alias: Optional[str] = ..., alias_priority: Any = ..., validation_alias: Any = ..., serialization_alias: Any = ..., title: Optional[str] = ..., description: Optional[str] = ..., gt: Optional[float] = ..., ge: Optional[float] = ..., lt: Optional[float] = ..., le: Optional[float] = ..., min_length: Optional[int] = ..., max_length: Optional[int] = ..., pattern: Optional[str] = ..., regex: Optional[str] = ..., discriminator: Any = ..., strict: Any = ..., multiple_of: Any = ..., allow_inf_nan: Any = ..., max_digits: Any = ..., decimal_places: Any = ..., examples: Optional[List[Example]] = ..., example: Any = ..., openapi_examples: Optional[Dict[str, Example]] = ..., deprecated: Optional[bool] = ..., include_in_schema: bool = ..., json_schema_extra: Optional[Dict[str, Any]] = ..., **extra: Any) -> None: ...

class Depends:
    def __init__(self, dependency: Optional[Callable[..., Any]] = ..., *, use_cache: bool = ...) -> None: ...

class Security(Depends):
    def __init__(self, dependency: Optional[Callable[..., Any]] = ..., *, scopes: Optional[List[str]] = ..., use_cache: bool = ...) -> None: ...
