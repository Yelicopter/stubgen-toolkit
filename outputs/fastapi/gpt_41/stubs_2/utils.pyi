from typing import Any, Dict, Optional, Set, Type, Union, cast

def is_body_allowed_for_status_code(status_code: Any) -> bool: ...
def get_path_param_names(path: str) -> Set[str]: ...
def create_model_field(
    name: str,
    type_: Any,
    class_validators: Optional[Dict[str, Any]] = ...,
    default: Any = ...,
    required: Any = ...,
    model_config: Any = ...,
    field_info: Any = ...,
    alias: Any = ...,
    mode: str = ...,
) -> Any: ...
def create_cloned_field(
    field: Any,
    *,
    cloned_types: Optional[Any] = ...,
) -> Any: ...
def generate_operation_id_for_path(
    *, name: str, path: str, method: str
) -> str: ...
def generate_unique_id(route: Any) -> str: ...
def deep_dict_update(main_dict: Dict[Any, Any], update_dict: Dict[Any, Any]) -> None: ...
def get_value_or_default(
    first_item: Any,
    *extra_items: Any,
) -> Any: ...