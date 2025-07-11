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
from pydantic import BaseModel, create_model
from pydantic.fields import FieldInfo
from typing_extensions import Literal

if TYPE_CHECKING:
    from .routing import APIRoute

_CLONED_TYPES_CACHE: WeakKeyDictionary[Any, Any]

def is_body_allowed_for_status_code(status_code: Union[int, str]) -> bool: ...

def get_path_param_names(path: str) -> Set[str]: ...

def create_model_field(
    name: str,
    type_: Any,
    class_validators: Optional[Dict[str, Any]] = None,
    default: Any = ...,
    required: Union[bool, Any] = ...,
    model_config: Type[Any] = ...,
    field_info: Optional[FieldInfo] = None,
    alias: Optional[str] = None,
    mode: Literal["validation", "serialization"] = "validation",
) -> Any: ...

def create_cloned_field(
    field: Any,
    *,
    cloned_types: Optional[MutableMapping[Type[BaseModel], Type[BaseModel]]] = None,
) -> Any: ...

def generate_operation_id_for_path(
    *, name: str, path: str, method: str
) -> str: ...  # pragma: nocover

def generate_unique_id(route: "APIRoute") -> str: ...

def deep_dict_update(main_dict: Dict[Any, Any], update_dict: Dict[Any, Any]) -> None: ...

def get_value_or_default(
    first_item: Union[Any, Any],
    *extra_items: Union[Any, Any],
) -> Union[Any, Any]: ...