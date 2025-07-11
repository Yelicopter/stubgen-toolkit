from _typeshed import Incomplete
from fastapi.openapi.models import Example as Example
from pydantic.fields import FieldInfo
from typing import Any, Callable, Dict, Optional

class ParamTypes(Enum):
    query: str
    header: str
    path: str
    cookie: str

class Param(FieldInfo):
    def __init__(self, default: Any = ..., *, default_factory: Optional[Callable] = ..., annotation: Optional[Any] = ..., alias: Optional[str] = ..., alias_priority: Optional[int] = ..., validation_alias: Optional[str] = ..., serialization_alias: Optional[str] = ..., title: Optional[str] = ..., description: Optional[str] = ..., gt: Optional[Any] = ..., ge: Optional[Any] = ..., lt: Optional[Any] = ..., le: Optional[Any] = ..., min_length: Optional[int] = ..., max_length: Optional[int] = ..., pattern: Optional[str] = ..., regex: Optional[str] = ..., discriminator: Optional[str] = ..., strict: Optional[bool] = ..., multiple_of: Optional[Any] = ..., allow_inf_nan: Optional[bool] = ..., max_digits: Optional[int] = ..., decimal_places: Optional[int] = ..., examples: Optional[Dict[str, Any]] = ..., example: Optional[Any] = ..., openapi_examples: Optional[Dict[str, Any]] = ..., deprecated: Optional[bool] = ..., include_in_schema: bool = ..., json_schema_extra: Optional[Dict[str, Any]] = ..., **extra: Any) -> None: ...

class Path(Param):
    in_: Incomplete

class Query(Param):
    in_: Incomplete

class Header(Param):
    in_: Incomplete

class Cookie(Param):
    in_: Incomplete

class Body(FieldInfo):
    def __init__(self, default: Any = ..., *, default_factory: Optional[Callable] = ..., annotation: Optional[Any] = ..., embed: Optional[bool] = ..., media_type: str = ..., alias: Optional[str] = ..., alias_priority: Optional[int] = ..., validation_alias: Optional[str] = ..., serialization_alias: Optional[str] = ..., title: Optional[str] = ..., description: Optional[str] = ..., gt: Optional[Any] = ..., ge: Optional[Any] = ..., lt: Optional[Any] = ..., le: Optional[Any] = ..., min_length: Optional[int] = ..., max_length: Optional[int] = ..., pattern: Optional[str] = ..., regex: Optional[str] = ..., discriminator: Optional[str] = ..., strict: Optional[bool] = ..., multiple_of: Optional[Any] = ..., allow_inf_nan: Optional[bool] = ..., max_digits: Optional[int] = ..., decimal_places: Optional[int] = ..., examples: Optional[Dict[str, Any]] = ..., example: Optional[Any] = ..., openapi_examples: Optional[Dict[str, Any]] = ..., deprecated: Optional[bool] = ..., include_in_schema: bool = ..., json_schema_extra: Optional[Dict[str, Any]] = ..., **extra: Any) -> None: ...

class Form(Body): ...
class File(Form): ...

class Depends:
    def __init__(self, dependency: Optional[Callable] = ..., *, use_cache: bool = ...) -> None: ...

class Security(Depends): ...
