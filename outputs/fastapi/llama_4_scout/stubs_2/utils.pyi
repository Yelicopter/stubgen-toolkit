import re
import warnings
from dataclasses import is_dataclass
from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    MutableMapping,
    Optional,
    Set,
    Type,
    Union,
    cast,
)
from weakref import WeakKeyDictionary

import fastapi
from fastapi._compat import (
    PYDANTIC_V2,
    BaseConfig,
    ModelField,
    PydanticSchemaGenerationError,
    Undefined,
    UndefinedType,
    Validator,
    lenient_issubclass,
)
from fastapi.datastructures import DefaultPlaceholder, DefaultType
from pydantic import BaseModel, create_model
from pydantic.fields import FieldInfo
from typing_extensions import Literal

if TYPE_CHECKING: 
    from .routing import APIRoute

_CLONED_TYPES_CACHE: Any

def is_body_allowed_for_status_code(status_code: int) -> bool:
    ...

def get_path_param_names(path: str) -> Set[str]:
    ...

def create_model_field(
    name: str,
    type_: Type[Any],
    class_validators: Optional[List[Callable]] = None,
    default: Any = None,
    required: Any = None,
    model_config: Type[BaseConfig] = BaseConfig,
    field_info: Optional[FieldInfo] = None,
    mode: str = "validation",
) -> ModelField:
    ...

def create_cloned_field(
    field: ModelField,
    *,
    cloned_types: Optional[Dict[Type[BaseModel], Type[BaseModel]]] = None,
) -> ModelField:
    ...

def generate_operation_id_for_path(
    *, 
    name: str, 
    path: str, 
    method: str
) -> str:
    ...

def generate_unique_id(route: Any) -> str:
    ...

def deep_dict_update(
    main_dict: Dict[str, Any], 
    update_dict: Dict[str, Any]
) -> None:
    ...

def get_value_or_default(
    first_item: Any,
    *extra_items: Any,
) -> Any:
    ...