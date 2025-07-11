from typing import Any, Callable, Dict, List, Optional, Sequence, Union

from fastapi import params
from fastapi._compat import Undefined
from fastapi.openapi.models import Example
from typing_extensions import Annotated, deprecated

_Unset = Undefined

def Path(
    default: Any = ...,
    *,
    default_factory: Optional[Callable] = None,
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
) -> Any:
    ...

def Query(
    default: Any = None,
    *,
    default_factory: Optional[Callable] = None,
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
) -> Any:
    ...

def Header(
    default: Any = None,
    *,
    default_factory: Optional[Callable] = None,
    alias: Optional[str] = None,
    alias_priority: Optional[int] = None,
    validation_alias: Optional[str] = None,
    serialization_alias: Optional[str] = None,
    convert_underscores: bool = True,
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
) -> Any:
    ...

def Body(
    default: Any = None,
    *,
    default_factory: Optional[Callable] = None,
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
) -> Any:
    ...

def Depends(
    dependency: Optional[Callable] = None,
    *,
    use_cache: bool = True,
) -> Any:
    ...

def Security(
    dependency: Optional[Callable] = None,
    *,
    scopes: Optional[List[str]] = None,
    use_cache: bool = True,
) -> Any:
    ...