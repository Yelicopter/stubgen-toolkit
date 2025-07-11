from ._compat import PYDANTIC_V2 as PYDANTIC_V2, PYDANTIC_VERSION_MINOR_TUPLE as PYDANTIC_VERSION_MINOR_TUPLE, Undefined as Undefined
from _typeshed import Incomplete
from enum import Enum
from fastapi.openapi.models import Example as Example
from pydantic.fields import FieldInfo
from typing import Any, Callable, Dict, List, Optional, Sequence, Union
from typing_extensions import Annotated, deprecated

class ParamTypes(Enum):
    query: str
    header: str
    path: str
    cookie: str

class Param(FieldInfo):
    in_: ParamTypes
    example: Incomplete
    include_in_schema: Incomplete
    openapi_examples: Incomplete
    deprecated: Incomplete
    def __init__(self, default: Any = ..., *, default_factory: Union[Callable[[], Any], None] = ..., annotation: Optional[Any] = ..., alias: Optional[str] = ..., alias_priority: Union[int, None] = ..., validation_alias: Union[str, None] = ..., serialization_alias: Union[str, None] = ..., title: Optional[str] = ..., description: Optional[str] = ..., gt: Optional[float] = ..., ge: Optional[float] = ..., lt: Optional[float] = ..., le: Optional[float] = ..., min_length: Optional[int] = ..., max_length: Optional[int] = ..., pattern: Optional[str] = ..., regex: Annotated[Optional[str], None] = ..., discriminator: Union[str, None] = ..., strict: Union[bool, None] = ..., multiple_of: Union[float, None] = ..., allow_inf_nan: Union[bool, None] = ..., max_digits: Union[int, None] = ..., decimal_places: Union[int, None] = ..., examples: Optional[List[Any]] = ..., example: Annotated[Optional[Any], None] = ..., openapi_examples: Optional[Dict[str, Example]] = ..., deprecated: Union[deprecated, str, bool, None] = ..., include_in_schema: bool = ..., json_schema_extra: Union[Dict[str, Any], None] = ..., **extra: Any) -> None: ...

class Path(Param):
    in_: Incomplete
    def __init__(self, default: Any = ..., *, default_factory: Union[Callable[[], Any], None] = ..., annotation: Optional[Any] = ..., alias: Optional[str] = ..., alias_priority: Union[int, None] = ..., validation_alias: Union[str, None] = ..., serialization_alias: Union[str, None] = ..., title: Optional[str] = ..., description: Optional[str] = ..., gt: Optional[float] = ..., ge: Optional[float] = ..., lt: Optional[float] = ..., le: Optional[float] = ..., min_length: Optional[int] = ..., max_length: Optional[int] = ..., pattern: Optional[str] = ..., regex: Annotated[Optional[str], None] = ..., discriminator: Union[str, None] = ..., strict: Union[bool, None] = ..., multiple_of: Union[float, None] = ..., allow_inf_nan: Union[bool, None] = ..., max_digits: Union[int, None] = ..., decimal_places: Union[int, None] = ..., examples: Optional[List[Any]] = ..., example: Annotated[Optional[Any], None] = ..., openapi_examples: Optional[Dict[str, Example]] = ..., deprecated: Union[deprecated, str, bool, None] = ..., include_in_schema: bool = ..., json_schema_extra: Union[Dict[str, Any], None] = ..., **extra: Any) -> None: ...

class Query(Param):
    in_: Incomplete
    def __init__(self, default: Any = ..., *, default_factory: Union[Callable[[], Any], None] = ..., annotation: Optional[Any] = ..., alias: Optional[str] = ..., alias_priority: Union[int, None] = ..., validation_alias: Union[str, None] = ..., serialization_alias: Union[str, None] = ..., title: Optional[str] = ..., description: Optional[str] = ..., gt: Optional[float] = ..., ge: Optional[float] = ..., lt: Optional[float] = ..., le: Optional[float] = ..., min_length: Optional[int] = ..., max_length: Optional[int] = ..., pattern: Optional[str] = ..., regex: Annotated[Optional[str], None] = ..., discriminator: Union[str, None] = ..., strict: Union[bool, None] = ..., multiple_of: Union[float, None] = ..., allow_inf_nan: Union[bool, None] = ..., max_digits: Union[int, None] = ..., decimal_places: Union[int, None] = ..., examples: Optional[List[Any]] = ..., example: Annotated[Optional[Any], None] = ..., openapi_examples: Optional[Dict[str, Example]] = ..., deprecated: Union[deprecated, str, bool, None] = ..., include_in_schema: bool = ..., json_schema_extra: Union[Dict[str, Any], None] = ..., **extra: Any) -> None: ...

class Header(Param):
    in_: Incomplete
    convert_underscores: Incomplete
    def __init__(self, default: Any = ..., *, default_factory: Union[Callable[[], Any], None] = ..., annotation: Optional[Any] = ..., alias: Optional[str] = ..., alias_priority: Union[int, None] = ..., validation_alias: Union[str, None] = ..., serialization_alias: Union[str, None] = ..., convert_underscores: bool = ..., title: Optional[str] = ..., description: Optional[str] = ..., gt: Optional[float] = ..., ge: Optional[float] = ..., lt: Optional[float] = ..., le: Optional[float] = ..., min_length: Optional[int] = ..., max_length: Optional[int] = ..., pattern: Optional[str] = ..., regex: Annotated[Optional[str], None] = ..., discriminator: Union[str, None] = ..., strict: Union[bool, None] = ..., multiple_of: Union[float, None] = ..., allow_inf_nan: Union[bool, None] = ..., max_digits: Union[int, None] = ..., decimal_places: Union[int, None] = ..., examples: Optional[List[Any]] = ..., example: Annotated[Optional[Any], None] = ..., openapi_examples: Optional[Dict[str, Example]] = ..., deprecated: Union[deprecated, str, bool, None] = ..., include_in_schema: bool = ..., json_schema_extra: Union[Dict[str, Any], None] = ..., **extra: Any) -> None: ...

class Cookie(Param):
    in_: Incomplete
    def __init__(self, default: Any = ..., *, default_factory: Union[Callable[[], Any], None] = ..., annotation: Optional[Any] = ..., alias: Optional[str] = ..., alias_priority: Union[int, None] = ..., validation_alias: Union[str, None] = ..., serialization_alias: Union[str, None] = ..., title: Optional[str] = ..., description: Optional[str] = ..., gt: Optional[float] = ..., ge: Optional[float] = ..., lt: Optional[float] = ..., le: Optional[float] = ..., min_length: Optional[int] = ..., max_length: Optional[int] = ..., pattern: Optional[str] = ..., regex: Annotated[Optional[str], None] = ..., discriminator: Union[str, None] = ..., strict: Union[bool, None] = ..., multiple_of: Union[float, None] = ..., allow_inf_nan: Union[bool, None] = ..., max_digits: Union[int, None] = ..., decimal_places: Union[int, None] = ..., examples: Optional[List[Any]] = ..., example: Annotated[Optional[Any], None] = ..., openapi_examples: Optional[Dict[str, Example]] = ..., deprecated: Union[deprecated, str, bool, None] = ..., include_in_schema: bool = ..., json_schema_extra: Union[Dict[str, Any], None] = ..., **extra: Any) -> None: ...

class Body(FieldInfo):
    embed: Incomplete
    media_type: Incomplete
    example: Incomplete
    include_in_schema: Incomplete
    openapi_examples: Incomplete
    deprecated: Incomplete
    def __init__(self, default: Any = ..., *, default_factory: Union[Callable[[], Any], None] = ..., annotation: Optional[Any] = ..., embed: Union[bool, None] = ..., media_type: str = ..., alias: Optional[str] = ..., alias_priority: Union[int, None] = ..., validation_alias: Union[str, None] = ..., serialization_alias: Union[str, None] = ..., title: Optional[str] = ..., description: Optional[str] = ..., gt: Optional[float] = ..., ge: Optional[float] = ..., lt: Optional[float] = ..., le: Optional[float] = ..., min_length: Optional[int] = ..., max_length: Optional[int] = ..., pattern: Optional[str] = ..., regex: Annotated[Optional[str], None] = ..., discriminator: Union[str, None] = ..., strict: Union[bool, None] = ..., multiple_of: Union[float, None] = ..., allow_inf_nan: Union[bool, None] = ..., max_digits: Union[int, None] = ..., decimal_places: Union[int, None] = ..., examples: Optional[List[Any]] = ..., example: Annotated[Optional[Any], None] = ..., openapi_examples: Optional[Dict[str, Example]] = ..., deprecated: Union[deprecated, str, bool, None] = ..., include_in_schema: bool = ..., json_schema_extra: Union[Dict[str, Any], None] = ..., **extra: Any) -> None: ...

class Form(Body):
    def __init__(self, default: Any = ..., *, default_factory: Union[Callable[[], Any], None] = ..., annotation: Optional[Any] = ..., media_type: str = ..., alias: Optional[str] = ..., alias_priority: Union[int, None] = ..., validation_alias: Union[str, None] = ..., serialization_alias: Union[str, None] = ..., title: Optional[str] = ..., description: Optional[str] = ..., gt: Optional[float] = ..., ge: Optional[float] = ..., lt: Optional[float] = ..., le: Optional[float] = ..., min_length: Optional[int] = ..., max_length: Optional[int] = ..., pattern: Optional[str] = ..., regex: Annotated[Optional[str], None] = ..., discriminator: Union[str, None] = ..., strict: Union[bool, None] = ..., multiple_of: Union[float, None] = ..., allow_inf_nan: Union[bool, None] = ..., max_digits: Union[int, None] = ..., decimal_places: Union[int, None] = ..., examples: Optional[List[Any]] = ..., example: Annotated[Optional[Any], None] = ..., openapi_examples: Optional[Dict[str, Example]] = ..., deprecated: Union[deprecated, str, bool, None] = ..., include_in_schema: bool = ..., json_schema_extra: Union[Dict[str, Any], None] = ..., **extra: Any) -> None: ...

class File(Form):
    def __init__(self, default: Any = ..., *, default_factory: Union[Callable[[], Any], None] = ..., annotation: Optional[Any] = ..., media_type: str = ..., alias: Optional[str] = ..., alias_priority: Union[int, None] = ..., validation_alias: Union[str, None] = ..., serialization_alias: Union[str, None] = ..., title: Optional[str] = ..., description: Optional[str] = ..., gt: Optional[float] = ..., ge: Optional[float] = ..., lt: Optional[float] = ..., le: Optional[float] = ..., min_length: Optional[int] = ..., max_length: Optional[int] = ..., pattern: Optional[str] = ..., regex: Annotated[Optional[str], None] = ..., discriminator: Union[str, None] = ..., strict: Union[bool, None] = ..., multiple_of: Union[float, None] = ..., allow_inf_nan: Union[bool, None] = ..., max_digits: Union[int, None] = ..., decimal_places: Union[int, None] = ..., examples: Optional[List[Any]] = ..., example: Annotated[Optional[Any], None] = ..., openapi_examples: Optional[Dict[str, Example]] = ..., deprecated: Union[deprecated, str, bool, None] = ..., include_in_schema: bool = ..., json_schema_extra: Union[Dict[str, Any], None] = ..., **extra: Any) -> None: ...

class Depends:
    dependency: Incomplete
    use_cache: Incomplete
    def __init__(self, dependency: Optional[Callable[..., Any]] = ..., *, use_cache: bool = ...) -> None: ...

class Security(Depends):
    scopes: Incomplete
    def __init__(self, dependency: Optional[Callable[..., Any]] = ..., *, scopes: Optional[Sequence[str]] = ..., use_cache: bool = ...) -> None: ...
