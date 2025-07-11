from typing import Any, Callable, Coroutine, Dict, ForwardRef, List, Mapping, Optional, Sequence, Tuple, Type, Union, cast
from dataclasses import dataclass

def ensure_multipart_is_installed() -> None: ...
def get_param_sub_dependant(
    *,
    param_name: str,
    depends: Any,
    path: str,
    security_scopes: Any = ...,
) -> Any: ...
def get_parameterless_sub_dependant(*, depends: Any, path: str) -> Any: ...
def get_sub_dependant(
    *,
    depends: Any,
    dependency: Any,
    path: str,
    name: Any = ...,
    security_scopes: Any = ...,
) -> Any: ...
CacheKey = Tuple[Optional[Callable[..., Any]], Tuple[str, ...]]
def get_flat_dependant(
    dependant: Any,
    *,
    skip_repeats: bool = ...,
    visited: Any = ...,
) -> Any: ...
def _get_flat_fields_from_params(fields: Any) -> Any: ...
def get_flat_params(dependant: Any) -> Any: ...
def get_typed_signature(call: Any) -> Any: ...
def get_typed_annotation(annotation: Any, globalns: Any) -> Any: ...
def get_typed_return_annotation(call: Any) -> Any: ...
def get_dependant(
    *,
    path: str,
    call: Any,
    name: Any = ...,
    security_scopes: Any = ...,
    use_cache: bool = ...,
) -> Any: ...
def add_non_field_param_to_dependency(
    *, param_name: str, type_annotation: Any, dependant: Any
) -> Any: ...
@dataclass
class ParamDetails:
    type_annotation: Any
    depends: Any
    field: Any
def analyze_param(
    *,
    param_name: str,
    annotation: Any,
    value: Any,
    is_path_param: bool,
) -> ParamDetails: ...
def add_param_to_fields(*, field: Any, dependant: Any) -> None: ...
def is_coroutine_callable(call: Any) -> bool: ...
def is_async_gen_callable(call: Any) -> bool: ...
def is_gen_callable(call: Any) -> bool: ...
async def solve_generator(
    *, call: Any, stack: Any, sub_values: Any
) -> Any: ...
@dataclass
class SolvedDependency:
    values: Dict[str, Any]
    errors: List[Any]
    background_tasks: Any
    response: Any
    dependency_cache: Dict[Tuple[Callable[..., Any], Tuple[str]], Any]
async def solve_dependencies(
    *,
    request: Any,
    dependant: Any,
    body: Any = ...,
    background_tasks: Any = ...,
    response: Any = ...,
    dependency_overrides_provider: Any = ...,
    dependency_cache: Any = ...,
    async_exit_stack: Any,
    embed_body_fields: bool,
) -> SolvedDependency: ...
def _validate_value_with_model_field(
    *, field: Any, value: Any, values: Any, loc: Any
) -> Tuple[Any, Any]: ...
def _get_multidict_value(
    field: Any, values: Any, alias: Any = ...
) -> Any: ...
def request_params_to_args(
    fields: Any,
    received_params: Any,
) -> Tuple[Any, Any]: ...
def _should_embed_body_fields(fields: Any) -> bool: ...
async def _extract_form_body(
    body_fields: Any,
    received_body: Any,
) -> Any: ...
async def request_body_to_args(
    body_fields: Any,
    received_body: Any,
    embed_body_fields: bool,
) -> Tuple[Any, Any]: ...
def get_body_field(
    *, flat_dependant: Any, name: str, embed_body_fields: bool
) -> Any: ...