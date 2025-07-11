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

def is_body_allowed_for_status_code(
    status_code: Optional[Union[int, str]]
) -> bool: ...
def get_path_param_names(path: str) -> Set[str]: ...
def create_model_field(
    name: str,
    type_: Type[Any],
    class_validators: Optional[Dict[str, Validator]] = None,
    default: Any = ...,
    required: Union[bool, UndefinedType] = ...,
    model_config: Type[BaseConfig] = ...,
    field_info: Optional[FieldInfo] = None,
    alias: Optional[str] = None,
    mode: Literal["validation", "serialization"] = "validation",
) -> ModelField: ...
def create_cloned_field(
    field: ModelField,
    *,
    cloned_types: Optional[MutableMapping[Type[BaseModel], Type[BaseModel]]] = None,
) -> ModelField: ...
def generate_operation_id_for_path(*, name: str, path: str, method: str) -> str: ...
def generate_unique_id(route: "APIRoute") -> str: ...
def deep_dict_update(main_dict: Dict[Any, Any], update_dict: Dict[Any, Any]) -> None: ...
def get_value_or_default(
    first_item: Union[Any, DefaultType], *extra_items: Union[Any, DefaultType]
) -> Union[Any, DefaultType]: ...