import asyncio
import dataclasses
import email.message
import inspect
import json
from contextlib import AsyncExitStack, asynccontextmanager
from enum import Enum, IntEnum
from typing import (
    Any,
    AsyncIterator,
    Callable,
    Coroutine,
    Dict,
    List,
    Mapping,
    Optional,
    Sequence,
    Set,
    Tuple,
    Type,
    Union,
)

from fastapi import params
from fastapi._compat import (
    ModelField,
    Undefined,
    _get_model_config,
    _model_dump,
    _normalize_errors,
    lenient_issubclass,
)
from fastapi.datastructures import Default, DefaultPlaceholder
from fastapi.dependencies.models import Dependant
from fastapi.dependencies.utils import (
    _should_embed_body_fields,
    get_body_field,
    get_dependant,
    get_flat_dependant,
    get_parameterless_sub_dependant,
    get_typed_return_annotation,
    solve_dependencies,
)
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import (
    FastAPIError,
    RequestValidationError,
    ResponseValidationError,
    WebSocketRequestValidationError,
)
from fastapi.types import DecoratedCallable, IncEx
from fastapi.utils import (
    create_cloned_field,
    create_model_field,
    generate_unique_id,
    get_value_or_default,
    is_body_allowed_for_status_code,
)
from pydantic import BaseModel
from starlette import routing
from starlette.concurrency import run_in_threadpool
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.routing import (
    BaseRoute,
    Match,
    compile_path,
    get_name,
    request_response,
    websocket_session,
)
from starlette.routing import Mount as Mount
from starlette.types import AppType, ASGIApp, Lifespan, Scope
from starlette.websockets import WebSocket
from typing_extensions import Annotated, Doc, deprecated

def _prepare_response_content(
    res: Any,
    *,
    exclude_unset: bool,
    exclude_defaults: bool = ...,
    exclude_none: bool = ...,
) -> Any:
    ...

def _merge_lifespan_context(
    original_context: Lifespan[Any], nested_context: Lifespan[Any]
) -> Lifespan[Any]:
    ...

async def serialize_response(
    *,
    field: Optional[ModelField] = ...,
    response_content: Any,
    include: Optional[IncEx] = ...,
    exclude: Optional[IncEx] = ...,
    by_alias: bool = ...,
    exclude_unset: bool = ...,
    exclude_defaults: bool = ...,
    exclude_none: bool = ...,
    is_coroutine: bool = ...,
) -> Any:
    ...

async def run_endpoint_function(
    *, dependant: Dependant, values: Dict[str, Any], is_coroutine: bool
) -> Any:
    ...

def get_request_handler(
    dependant: Dependant,
    body_field: Optional[ModelField] = ...,
    status_code: Optional[int] = ...,
    response_class: Union[Type[Response], DefaultPlaceholder] = ...,
    response_field: Optional[ModelField] = ...,
    response_model_include: Optional[IncEx] = ...,
    response_model_exclude: Optional[IncEx] = ...,
    response_model_by_alias: bool = ...,
    response_model_exclude_unset: bool = ...,
    response_model_exclude_defaults: bool = ...,
    response_model_exclude_none: bool = ...,
    dependency_overrides_provider: Optional[Any] = ...,
    embed_body_fields: bool = ...,
) -> Callable[[Request], Coroutine[Any, Any, Response]]:
    ...

def get_websocket_app(
    dependant: Dependant,
    dependency_overrides_provider: Optional[Any] = ...,
    embed_body_fields: bool = ...,
) -> Callable[[WebSocket], Coroutine[Any, Any, None]]:
    ...

class APIWebSocketRoute(routing.WebSocketRoute):
    def __init__(
        self,
        path: str,
        endpoint: Callable[..., Any],
        *,
        name: Optional[str] = ...,
        dependencies: Optional[Sequence[params.Depends]] = ...,
        dependency_overrides_provider: Optional[Any] = ...,
    ) -> None:
        ...

    def matches(self, scope: Scope) -> Tuple[Match, Scope]:
        ...

class APIRoute(routing.Route):
    def __init__(
        self,
        path: str,
        endpoint: Callable[..., Any],
        *,
        response_model: Any = ...,
        status_code: Optional[int] = ...,
        tags: Optional[List[Union[str, Enum]]] = ...,
        dependencies: Optional[Sequence[params.Depends]] = ...,
        summary: Optional[str] = ...,
        description: Optional[str] = ...,
        response_description: str = ...,
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = ...,
        deprecated: Optional[bool] = ...,
        name: Optional[str] = ...,
        methods: Optional[Union[Set[str], List[str]]] = ...,
        operation_id: Optional[str] = ...,
        response_model_include: Optional[IncEx] = ...,
        response_model_exclude: Optional[IncEx] = ...,
        response_model_by_alias: bool = ...,
        response_model_exclude_unset: bool = ...,
        response_model_exclude_defaults: bool = ...,
        response_model_exclude_none: bool = ...,
        include_in_schema: bool = ...,
        response_class: Union[Type[Response], DefaultPlaceholder] = ...,
        dependency_overrides_provider: Optional[Any] = ...,
        callbacks: Optional[List[BaseRoute]] = ...,
        openapi_extra: Optional[Dict[str, Any]] = ...,
        generate_unique_id_function: Callable[["APIRoute"], str] = ...,
    ) -> None:
        ...

    def get_route_handler(self) -> Callable[[Request], Coroutine[Any, Any, Response]]:
        ...

    def matches(self, scope: Scope) -> Tuple[Match, Scope]:
        ...

class APIRouter(routing.Router):
    def __init__(
        self,
        *,
        prefix: str = ...,
        tags: Optional[List[Union[str, Enum]]] = ...,
        dependencies: Optional[Sequence[params.Depends]] = ...,
        default_response_class: Type[Response] = ...,
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = ...,
        callbacks: Optional[List[BaseRoute]] = ...,
        routes: Optional[List[BaseRoute]] = ...,
        redirect_slashes: bool = ...,
        default: Optional[ASGIApp] = ...,
        dependency_overrides_provider: Optional[Any] = ...,
        route_class: Type[APIRoute] = ...,
        on_startup: Optional[Sequence[Callable[[], Any]]] = ...,
        on_shutdown: Optional[Sequence[Callable[[], Any]]] = ...,
        lifespan: Optional[Lifespan[Any]] = ...,
        deprecated: Optional[bool] = ...,
        include_in_schema: bool = ...,
        generate_unique_id_function: Callable[[APIRoute], str] = ...,
    ) -> None:
        ...

    def route(
        self,
        path: str,
        methods: Optional[List[str]] = ...,
        name: Optional[str] = ...,
        include_in_schema: bool = ...,
    ) -> Callable[[DecoratedCallable], DecoratedCallable]:
        ...

    def add_api_route(
        self,
        path: str,
        endpoint: Callable[..., Any],
        *,
        response_model: Any = ...,
        status_code: Optional[int] = ...,
        tags: Optional[List[Union[str, Enum]]] = ...,
        dependencies: Optional[Sequence[params.Depends]] = ...,
        summary: Optional[str] = ...,
        description: Optional[str] = ...,
        response_description: str = ...,
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = ...,
        deprecated: Optional[bool] = ...,
        methods: Optional[Union[Set[str], List[str]]] = ...,
        operation_id: Optional[str] = ...,
        response_model_include: Optional[IncEx] = ...,
        response_model_exclude: Optional[IncEx] = ...,
        response_model_by_alias: bool = ...,
        response_model_exclude_unset: bool = ...,
        response_model_exclude_defaults: bool = ...,
        response_model_exclude_none: bool = ...,
        include_in_schema: bool = ...,
        response_class: Union[Type[Response], DefaultPlaceholder] = ...,
        name: Optional[str] = ...,
        route_class_override: Optional[Type[APIRoute]] = ...,
        callbacks: Optional[List[BaseRoute]] = ...,
        openapi_extra: Optional[Dict[str, Any]] = ...,
        generate_unique_id_function: Callable[[APIRoute], str] = ...,
    ) -> None:
        ...

    def api_route(
        self,
        path: str,
        *,
        response_model: Any = ...,
        status_code: Optional[int] = ...,
        tags: Optional[List[Union[str, Enum]]] = ...,
        dependencies: Optional[Sequence[params.Depends]] = ...,
        summary: Optional[str] = ...,
        description: Optional[str] = ...,
        response_description: str = ...,
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = ...,
        deprecated: Optional[bool] = ...,
        methods: Optional[List[str]] = ...,
        operation_id: Optional[str] = ...,
        response_model_include: Optional[IncEx] = ...,
        response_model_exclude: Optional[IncEx] = ...,
        response_model_by_alias: bool = ...,
        response_model_exclude_unset: bool = ...,
        response_model_exclude_defaults: bool = ...,
        response_model_exclude_none: bool = ...,
        include_in_schema: bool = ...,
        response_class: Type[Response] = ...,
        name: Optional[str] = ...,
        callbacks: Optional[List[BaseRoute]] = ...,
        openapi_extra: Optional[Dict[str, Any]] = ...,
        generate_unique_id_function: Callable[[APIRoute], str] = ...,
    ) -> Callable[[DecoratedCallable], DecoratedCallable]:
        ...

    def add_api_websocket_route(
        self,
        path: str,
        endpoint: Callable[..., Any],
        name: Optional[str] = ...,
        *,
        dependencies: Optional[Sequence[params.Depends]] = ...,
    ) -> None:
        ...

    def websocket(
        self,
        path: str,
        name: Optional[str] = ...,
        *,
        dependencies: Optional[Sequence[params.Depends]] = ...,
    ) -> Callable[[DecoratedCallable], DecoratedCallable]:
        ...

    def websocket_route(
        self, path: str, name: Optional[str] = ...
    ) -> Callable[[DecoratedCallable], DecoratedCallable]:
        ...

    def include_router(
        self,
        router: "APIRouter",
        *,
        prefix: str = ...,
        tags: Optional[List[Union[str, Enum]]] = ...,
        dependencies: Optional[Sequence[params.Depends]] = ...,
        default_response_class: Type[Response] = ...,
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = ...,
        callbacks: Optional[List[BaseRoute]] = ...,
        deprecated: Optional[bool] = ...,
        include_in_schema: bool = ...,
        generate_unique_id_function: Callable[[APIRoute], str] = ...,
    ) -> None:
        ...

    def get(
        self,
        path: str,
        *,
        response_model: Any = ...,
        status_code: Optional[int] = ...,
        tags: Optional[List[Union[str, Enum]]] = ...,
        dependencies: Optional[Sequence[params.Depends]] = ...,
        summary: Optional[str] = ...,
        description: Optional[str] = ...,
        response_description: str = ...,
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = ...,
        deprecated: Optional[bool] = ...,
        operation_id: Optional[str] = ...,
        response_model_include: Optional[IncEx] = ...,
        response_model_exclude: Optional[IncEx] = ...,
        response_model_by_alias: bool = ...,
        response_model_exclude_unset: bool = ...,
        response_model_exclude_defaults: bool = ...,
        response_model_exclude_none: bool = ...,
        include_in_schema: bool = ...,
        response_class: Type[Response] = ...,
        name: Optional[str] = ...,
        callbacks: Optional[List[BaseRoute]] = ...,
        openapi_extra: Optional[Dict[str, Any]] = ...,
        generate_unique_id_function: Callable[[APIRoute], str] = ...,
    ) -> Callable[[DecoratedCallable], DecoratedCallable]:
        ...

    def put(
        self,
        path: str,
        *,
        response_model: Any = ...,
        status_code: Optional[int] = ...,
        tags: Optional[List[Union[str, Enum]]] = ...,
        dependencies: Optional[Sequence[params.Depends]] = ...,
        summary: Optional[str] = ...,
        description: Optional[str] = ...,
        response_description: str = ...,
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = ...,
        deprecated: Optional[bool] = ...,
        operation_id: Optional[str] = ...,
        response_model_include: Optional[IncEx] = ...,
        response_model_exclude: Optional[IncEx] = ...,
        response_model_by_alias: bool = ...,
        response_model_exclude_unset: bool = ...,
        response_model_exclude_defaults: bool = ...,
        response_model_exclude_none: bool = ...,
        include_in_schema: bool = ...,
        response_class: Type[Response] = ...,
        name: Optional[str] = ...,
        callbacks: Optional[List[BaseRoute]] = ...,
        openapi_extra: Optional[Dict[str, Any]] = ...,
        generate_unique_id_function: Callable[[APIRoute], str] = ...,
    ) -> Callable[[DecoratedCallable], DecoratedCallable]:
        ...

    def post(
        self,
        path: str,
        *,
        response_model: Any = ...,
        status_code: Optional[int] = ...,
        tags: Optional[List[Union[str, Enum]]] = ...,
        dependencies: Optional[Sequence[params.Depends]] = ...,
        summary: Optional[str] = ...,
        description: Optional[str] = ...,
        response_description: str = ...,
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = ...,
        deprecated: Optional[bool] = ...,
        operation_id: Optional[str] = ...,
        response_model_include: Optional[IncEx] = ...,
        response_model_exclude: Optional[IncEx] = ...,
        response_model_by_alias: bool = ...,
        response_model_exclude_unset: bool = ...,
        response_model_exclude_defaults: bool = ...,
        response_model_exclude_none: bool = ...,
        include_in_schema: bool = ...,
        response_class: Type[Response] = ...,
        name: Optional[str] = ...,
        callbacks: Optional[List[BaseRoute]] = ...,
        openapi_extra: Optional[Dict[str, Any]] = ...,
        generate_unique_id_function: Callable[[APIRoute], str] = ...,
    ) -> Callable[[DecoratedCallable], DecoratedCallable]:
        ...

    def delete(
        self,
        path: str,
        *,
        response_model: Any = ...,
        status_code: Optional[int] = ...,
        tags: Optional[List[Union[str, Enum]]] = ...,
        dependencies: Optional[Sequence[params.Depends]] = ...,
        summary: Optional[str] = ...,
        description: Optional[str] = ...,
        response_description: str = ...,
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = ...,
        deprecated: Optional[bool] = ...,
        operation_id: Optional[str] = ...,
        response_model_include: Optional[IncEx] = ...,
        response_model_exclude: Optional[IncEx] = ...,
        response_model_by_alias: bool = ...,
        response_model_exclude_unset: bool = ...,
        response_model_exclude_defaults: bool = ...,
        response_model_exclude_none: bool = ...,
        include_in_schema: bool = ...,
        response_class: Type[Response] = ...,
        name: Optional[str] = ...,
        callbacks: Optional[List[BaseRoute]] = ...,
        openapi_extra: Optional[Dict[str, Any]] = ...,
        generate_unique_id_function: Callable[[APIRoute], str] = ...,
    ) -> Callable[[DecoratedCallable], DecoratedCallable]:
        ...

    def options(
        self,
        path: str,
        *,
        response_model: Any = ...,
        status_code: Optional[int] = ...,
        tags: Optional[List[Union[str, Enum]]] = ...,
        dependencies: Optional[Sequence[params.Depends]] = ...,
        summary: Optional[str] = ...,
        description: Optional[str] = ...,
        response_description: str = ...,
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = ...,
        deprecated: Optional[bool] = ...,
        operation_id: Optional[str] = ...,
        response_model_include: Optional[IncEx] = ...,
        response_model_exclude: Optional[IncEx] = ...,
        response_model_by_alias: bool = ...,
        response_model_exclude_unset: bool = ...,
        response_model_exclude_defaults: bool = ...,
        response_model_exclude_none: bool = ...,
        include_in_schema: bool = ...,
        response_class: Type[Response] = ...,
        name: Optional[str] = ...,
        callbacks: Optional[List[BaseRoute]] = ...,
        openapi_extra: Optional[Dict[str, Any]] = ...,
        generate_unique_id_function: Callable[[APIRoute], str] = ...,
    ) -> Callable[[DecoratedCallable], DecoratedCallable]:
        ...

    def head(
        self,
        path: str,
        *,
        response_model: Any = ...,
        status_code: Optional[int] = ...,
        tags: Optional[List[Union[str, Enum]]] = ...,
        dependencies: Optional[Sequence[params.Depends]] = ...,
        summary: Optional[str] = ...,
        description: Optional[str] = ...,
        response_description: str = ...,
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = ...,
        deprecated: Optional[bool] = ...,
        operation_id: Optional[str] = ...,
        response_model_include: Optional[IncEx] = ...,
        response_model_exclude: Optional[IncEx] = ...,
        response_model_by_alias: bool = ...,
        response_model_exclude_unset: bool = ...,
        response_model_exclude_defaults: bool = ...,
        response_model_exclude_none: bool = ...,
        include_in_schema: bool = ...,
        response_class: Type[Response] = ...,
        name: Optional[str] = ...,
        callbacks: Optional[List[BaseRoute]] = ...,
        openapi_extra: Optional[Dict[str, Any]] = ...,
        generate_unique_id_function: Callable[[APIRoute], str] = ...,
    ) -> Callable[[DecoratedCallable], DecoratedCallable]:
        ...

    def patch(
        self,
        path: str,
        *,
        response_model: Any = ...,
        status_code: Optional[int] = ...,
        tags: Optional[List[Union[str, Enum]]] = ...,
        dependencies: Optional[Sequence[params.Depends]] = ...,
        summary: Optional[str] = ...,
        description: Optional[str] = ...,
        response_description: str = ...,
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = ...,
        deprecated: Optional[bool] = ...,
        operation_id: Optional[str] = ...,
        response_model_include: Optional[IncEx] = ...,
        response_model_exclude: Optional[IncEx] = ...,
        response_model_by_alias: bool = ...,
        response_model_exclude_unset: bool = ...,
        response_model_exclude_defaults: bool = ...,
        response_model_exclude_none: bool = ...,
        include_in_schema: bool = ...,
        response_class: Type[Response] = ...,
        name: Optional[str] = ...,
        callbacks: Optional[List[BaseRoute]] = ...,
        openapi_extra: Optional[Dict[str, Any]] = ...,
        generate_unique_id_function: Callable[[APIRoute], str] = ...,
    ) -> Callable[[DecoratedCallable], DecoratedCallable]:
        ...

    def trace(
        self,
        path: str,
        *,
        response_model: Any = ...,
        status_code: Optional[int] = ...,
        tags: Optional[List[Union[str, Enum]]] = ...,
        dependencies: Optional[Sequence[params.Depends]] = ...,
        summary: Optional[str] = ...,
        description: Optional[str] = ...,
        response_description: str = ...,
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = ...,
        deprecated: Optional[bool] = ...,
        operation_id: Optional[str] = ...,
        response_model_include: Optional[IncEx] = ...,
        response_model_exclude: Optional[IncEx] = ...,
        response_model_by_alias: bool = ...,
        response_model_exclude_unset: bool = ...,
        response_model_exclude_defaults: bool = ...,
        response_model_exclude_none: bool = ...,
        include_in_schema: bool = ...,
        response_class: Type[Response] = ...,
        name: Optional[str] = ...,
        callbacks: Optional[List[BaseRoute]] = ...,
        openapi_extra: Optional[Dict[str, Any]] = ...,
        generate_unique_id_function: Callable[[APIRoute], str] = ...,
    ) -> Callable[[DecoratedCallable], DecoratedCallable]:
        ...

    @deprecated
    def on_event(
        self,
        event_type: str,
    ) -> Callable[[DecoratedCallable], DecoratedCallable]:
        ...