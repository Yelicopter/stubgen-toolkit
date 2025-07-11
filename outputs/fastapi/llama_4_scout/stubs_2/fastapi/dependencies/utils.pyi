import inspect
from contextlib import AsyncExitStack, contextmanager
from copy import copy, deepcopy
from dataclasses import dataclass
from typing import (
    Any,
    Callable,
    Coroutine,
    Dict,
    ForwardRef,
    List,
    Mapping,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
)

import anyio
from fastapi import params
from fastapi._compat import (
    PYDANTIC_V2,
    ErrorWrapper,
    ModelField,
    RequiredParam,
    Undefined,
    _regenerate_error_with_loc,
    copy_field_info,
    create_body_model,
    evaluate_forwardref,
    field_annotation_is_scalar,
    get_cached_model_fields,
    get_missing_field_error,
    is_bytes_field,
    is_bytes_sequence_field,
    is_scalar_field,
    is_scalar_sequence_field,
    is_sequence_field,
    is_uploadfile_or_nonable_uploadfile_annotation,
    is_uploadfile_sequence_annotation,
    lenient_issubclass,
    sequence_types,
    serialize_sequence_value,
    value_is_sequence,
)
from fastapi.background import BackgroundTasks
from fastapi.concurrency import (
    asynccontextmanager,
    contextmanager_in_threadpool,
)
from fastapi.dependencies.models import Dependant, SecurityRequirement
from fastapi.logger import logger
from fastapi.security.base import SecurityBase
from fastapi.security.oauth2 import OAuth2, SecurityScopes
from fastapi.security.open_id_connect_url import OpenIdConnect
from fastapi.utils import create_model_field, get_path_param_names
from pydantic import BaseModel
from pydantic.fields import FieldInfo
from starlette.background import BackgroundTasks as StarletteBackgroundTasks
from starlette.concurrency import run_in_threadpool
from starlette.datastructures import (
    FormData,
    Headers,
    ImmutableMultiDict,
    QueryParams,
    UploadFile,
)
from starlette.requests import HTTPConnection, Request
from starlette.responses import Response
from starlette.websockets import WebSocket
from typing_extensions import Annotated

def get_param_sub_dependant(
    *,
    param_name: str,
    depends: params.Depends,
    path: str,
    security_scopes: List[str] = None,
) -> Dependant:
    ...

def get_parameterless_sub_dependant(
    *,
    depends: Dependant,
    path: str,
) -> Dependant:
    ...

def get_sub_dependant(
    *,
    depends: Dependant,
    dependency: Callable[..., Any],
    path: str,
    name: str = None,
    security_scopes: List[str] = None,
) -> Dependant:
    ...

def get_flat_dependant(
    dependant: Dependant,
    *,
    skip_repeats: bool = False,
    visited: List[Tuple[Optional[Callable[..., Any]], Tuple[str, ...]]] = None,
) -> Dependant:
    ...

def get_typed_signature(call: Callable[..., Any]) -> inspect.Signature:
    ...

def get_typed_annotation(
    annotation: Any,
    globalns: Dict[str, Any],
) -> Any:
    ...

def get_typed_return_annotation(call: Callable[..., Any]) -> Any:
    ...

async def solve_generator(
    *,
    call: Callable[..., Any],
    stack: AsyncExitStack,
    sub_values: Dict[str, Any],
) -> Any:
    ...

@dataclass
class SolvedDependency:
    values: Dict[str, Any]
    errors: List[Any]
    background_tasks: Optional[StarletteBackgroundTasks]
    response: Response
    dependency_cache: Dict[Tuple[Callable[..., Any], Tuple[str]], Any]

async def solve_dependencies(
    *,
    request: Request,
    dependant: Dependant,
    body: Any = None,
    background_tasks: BackgroundTasks = None,
    response: Response = None,
    dependency_overrides_provider: Any = None,
    dependency_cache: Dict[Tuple[Callable[..., Any], Tuple[str]], Any] = None,
    async_exit_stack: AsyncExitStack,
    embed_body_fields: bool,
) -> SolvedDependency:
    ...

def _validate_value_with_model_field(
    *,
    field: ModelField,
    value: Any,
    values: Dict[str, Any],
    loc: Tuple[str, ...],
) -> Any:
    ...

def request_params_to_args(
    fields: List[ModelField],
    received_params: Any,
) -> Any:
    ...

def get_body_field(
    *,
    flat_dependant: Dependant,
    name: str,
    embed_body_fields: bool,
) -> ModelField:
    ...