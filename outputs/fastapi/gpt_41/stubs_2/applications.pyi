from typing import Any, Awaitable, Callable, Coroutine, Dict, List, Optional, Sequence, Type, TypeVar, Union
from starlette.applications import Starlette
from starlette.datastructures import State
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import HTMLResponse, JSONResponse, Response
from starlette.routing import BaseRoute
from starlette.types import ASGIApp, Lifespan, Receive, Scope, Send
from fastapi.datastructures import Default, DefaultPlaceholder
from fastapi.routing import APIRouter
from fastapi.types import DecoratedCallable, IncEx

AppType = TypeVar("AppType", bound="FastAPI")

class FastAPI(Starlette):
    debug: bool
    title: str
    summary: Optional[str]
    description: str
    version: str
    terms_of_service: Optional[str]
    contact: Optional[Dict[str, Any]]
    license_info: Optional[Dict[str, Any]]
    openapi_url: Optional[str]
    openapi_tags: Optional[List[Dict[str, Any]]]
    root_path_in_servers: bool
    docs_url: Optional[str]
    redoc_url: Optional[str]
    swagger_ui_oauth2_redirect_url: Optional[str]
    swagger_ui_init_oauth: Optional[Dict[str, Any]]
    swagger_ui_parameters: Optional[Dict[str, Any]]
    servers: List[Dict[str, Any]]
    separate_input_output_schemas: bool
    extra: Dict[str, Any]
    openapi_version: str
    openapi_schema: Any
    webhooks: Any
    root_path: str
    state: State
    dependency_overrides: Dict[Any, Any]
    router: APIRouter
    exception_handlers: Dict[Any, Callable[..., Any]]
    user_middleware: List[Any]
    middleware_stack: Any

    def __init__(
        self,
        *,
        debug: bool = ...,
        routes: Optional[Sequence[BaseRoute]] = ...,
        title: str = ...,
        summary: Optional[str] = ...,
        description: str = ...,
        version: str = ...,
        openapi_url: Optional[str] = ...,
        openapi_tags: Optional[List[Dict[str, Any]]] = ...,
        servers: Optional[List[Dict[str, Any]]] = ...,
        dependencies: Optional[Sequence[Any]] = ...,
        default_response_class: Any = ...,
        redirect_slashes: bool = ...,
        docs_url: Optional[str] = ...,
        redoc_url: Optional[str] = ...,
        swagger_ui_oauth2_redirect_url: Optional[str] = ...,
        swagger_ui_init_oauth: Optional[Dict[str, Any]] = ...,
        middleware: Optional[Sequence[Any]] = ...,
        exception_handlers: Optional[Dict[Any, Callable[..., Any]]] = ...,
        on_startup: Optional[Sequence[Callable[..., Any]]] = ...,
        on_shutdown: Optional[Sequence[Callable[..., Any]]] = ...,
        lifespan: Optional[Lifespan[Any]] = ...,
        terms_of_service: Optional[str] = ...,
        contact: Optional[Dict[str, Any]] = ...,
        license_info: Optional[Dict[str, Any]] = ...,
        openapi_prefix: str = ...,
        root_path: str = ...,
        root_path_in_servers: bool = ...,
        responses: Optional[Dict[Any, Any]] = ...,
        callbacks: Optional[Sequence[Any]] = ...,
        webhooks: Optional[Any] = ...,
        deprecated: Optional[bool] = ...,
        include_in_schema: bool = ...,
        swagger_ui_parameters: Optional[Dict[str, Any]] = ...,
        generate_unique_id_function: Any = ...,
        separate_input_output_schemas: bool = ...,
        **extra: Any,
    ) -> None: ...
    def openapi(self) -> Any: ...
    def setup(self) -> None: ...
    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None: ...
    def add_api_route(
        self,
        path: str,
        endpoint: Callable[..., Any],
        *,
        response_model: Any = ...,
        status_code: Any = ...,
        tags: Any = ...,
        dependencies: Any = ...,
        summary: Any = ...,
        description: Any = ...,
        response_description: str = ...,
        responses: Any = ...,
        deprecated: Any = ...,
        methods: Any = ...,
        operation_id: Any = ...,
        response_model_include: Any = ...,
        response_model_exclude: Any = ...,
        response_model_by_alias: bool = ...,
        response_model_exclude_unset: bool = ...,
        response_model_exclude_defaults: bool = ...,
        response_model_exclude_none: bool = ...,
        include_in_schema: bool = ...,
        response_class: Any = ...,
        name: Any = ...,
        openapi_extra: Any = ...,
        generate_unique_id_function: Any = ...,
    ) -> None: ...
    def api_route(
        self,
        path: str,
        *,
        response_model: Any = ...,
        status_code: Any = ...,
        tags: Any = ...,
        dependencies: Any = ...,
        summary: Any = ...,
        description: Any = ...,
        response_description: str = ...,
        responses: Any = ...,
        deprecated: Any = ...,
        methods: Any = ...,
        operation_id: Any = ...,
        response_model_include: Any = ...,
        response_model_exclude: Any = ...,
        response_model_by_alias: bool = ...,
        response_model_exclude_unset: bool = ...,
        response_model_exclude_defaults: bool = ...,
        response_model_exclude_none: bool = ...,
        include_in_schema: bool = ...,
        response_class: Any = ...,
        name: Any = ...,
        openapi_extra: Any = ...,
        generate_unique_id_function: Any = ...,
    ) -> Callable[[Callable[..., Any]], Callable[..., Any]]: ...
    def add_api_websocket_route(
        self,
        path: str,
        endpoint: Callable[..., Any],
        name: Any = ...,
        *,
        dependencies: Any = ...,
    ) -> None: ...
    def websocket(
        self,
        path: str,
        name: Any = ...,
        *,
        dependencies: Any = ...,
    ) -> Callable[[Callable[..., Any]], Callable[..., Any]]: ...
    def include_router(
        self,
        router: APIRouter,
        *,
        prefix: str = ...,
        tags: Any = ...,
        dependencies: Any = ...,
        responses: Any = ...,
        deprecated: Any = ...,
        include_in_schema: bool = ...,
        default_response_class: Any = ...,
        callbacks: Any = ...,
        generate_unique_id_function: Any = ...,
    ) -> None: ...
    def get(
        self,
        path: str,
        *,
        response_model: Any = ...,
        status_code: Any = ...,
        tags: Any = ...,
        dependencies: Any = ...,
        summary: Any = ...,
        description: Any = ...,
        response_description: str = ...,
        responses: Any = ...,
        deprecated: Any = ...,
        operation_id: Any = ...,
        response_model_include: Any = ...,
        response_model_exclude: Any = ...,
        response_model_by_alias: bool = ...,
        response_model_exclude_unset: bool = ...,
        response_model_exclude_defaults: bool = ...,
        response_model_exclude_none: bool = ...,
        include_in_schema: bool = ...,
        response_class: Any = ...,
        name: Any = ...,
        callbacks: Any = ...,
        openapi_extra: Any = ...,
        generate_unique_id_function: Any = ...,
    ) -> Any: ...
    def put(self, path: str, *, response_model: Any = ..., status_code: Any = ..., tags: Any = ..., dependencies: Any = ..., summary: Any = ..., description: Any = ..., response_description: str = ..., responses: Any = ..., deprecated: Any = ..., operation_id: Any = ..., response_model_include: Any = ..., response_model_exclude: Any = ..., response_model_by_alias: bool = ..., response_model_exclude_unset: bool = ..., response_model_exclude_defaults: bool = ..., response_model_exclude_none: bool = ..., include_in_schema: bool = ..., response_class: Any = ..., name: Any = ..., callbacks: Any = ..., openapi_extra: Any = ..., generate_unique_id_function: Any = ...) -> Any: ...
    def post(self, path: str, *, response_model: Any = ..., status_code: Any = ..., tags: Any = ..., dependencies: Any = ..., summary: Any = ..., description: Any = ..., response_description: str = ..., responses: Any = ..., deprecated: Any = ..., operation_id: Any = ..., response_model_include: Any = ..., response_model_exclude: Any = ..., response_model_by_alias: bool = ..., response_model_exclude_unset: bool = ..., response_model_exclude_defaults: bool = ..., response_model_exclude_none: bool = ..., include_in_schema: bool = ..., response_class: Any = ..., name: Any = ..., callbacks: Any = ..., openapi_extra: Any = ..., generate_unique_id_function: Any = ...) -> Any: ...
    def delete(self, path: str, *, response_model: Any = ..., status_code: Any = ..., tags: Any = ..., dependencies: Any = ..., summary: Any = ..., description: Any = ..., response_description: str = ..., responses: Any = ..., deprecated: Any = ..., operation_id: Any = ..., response_model_include: Any = ..., response_model_exclude: Any = ..., response_model_by_alias: bool = ..., response_model_exclude_unset: bool = ..., response_model_exclude_defaults: bool = ..., response_model_exclude_none: bool = ..., include_in_schema: bool = ..., response_class: Any = ..., name: Any = ..., callbacks: Any = ..., openapi_extra: Any = ..., generate_unique_id_function: Any = ...) -> Any: ...
    def options(self, path: str, *, response_model: Any = ..., status_code: Any = ..., tags: Any = ..., dependencies: Any = ..., summary: Any = ..., description: Any = ..., response_description: str = ..., responses: Any = ..., deprecated: Any = ..., operation_id: Any = ..., response_model_include: Any = ..., response_model_exclude: Any = ..., response_model_by_alias: bool = ..., response_model_exclude_unset: bool = ..., response_model_exclude_defaults: bool = ..., response_model_exclude_none: bool = ..., include_in_schema: bool = ..., response_class: Any = ..., name: Any = ..., callbacks: Any = ..., openapi_extra: Any = ..., generate_unique_id_function: Any = ...) -> Any: ...
    def head(self, path: str, *, response_model: Any = ..., status_code: Any = ..., tags: Any = ..., dependencies: Any = ..., summary: Any = ..., description: Any = ..., response_description: str = ..., responses: Any = ..., deprecated: Any = ..., operation_id: Any = ..., response_model_include: Any = ..., response_model_exclude: Any = ..., response_model_by_alias: bool = ..., response_model_exclude_unset: bool = ..., response_model_exclude_defaults: bool = ..., response_model_exclude_none: bool = ..., include_in_schema: bool = ..., response_class: Any = ..., name: Any = ..., callbacks: Any = ..., openapi_extra: Any = ..., generate_unique_id_function: Any = ...) -> Any: ...
    def patch(self, path: str, *, response_model: Any = ..., status_code: Any = ..., tags: Any = ..., dependencies: Any = ..., summary: Any = ..., description: Any = ..., response_description: str = ..., responses: Any = ..., deprecated: Any = ..., operation_id: Any = ..., response_model_include: Any = ..., response_model_exclude: Any = ..., response_model_by_alias: bool = ..., response_model_exclude_unset: bool = ..., response_model_exclude_defaults: bool = ..., response_model_exclude_none: bool = ..., include_in_schema: bool = ..., response_class: Any = ..., name: Any = ..., callbacks: Any = ..., openapi_extra: Any = ..., generate_unique_id_function: Any = ...) -> Any: ...
    def trace(self, path: str, *, response_model: Any = ..., status_code: Any = ..., tags: Any = ..., dependencies: Any = ..., summary: Any = ..., description: Any = ..., response_description: str = ..., responses: Any = ..., deprecated: Any = ..., operation_id: Any = ..., response_model_include: Any = ..., response_model_exclude: Any = ..., response_model_by_alias: bool = ..., response_model_exclude_unset: bool = ..., response_model_exclude_defaults: bool = ..., response_model_exclude_none: bool = ..., include_in_schema: bool = ..., response_class: Any = ..., name: Any = ..., callbacks: Any = ..., openapi_extra: Any = ..., generate_unique_id_function: Any = ...) -> Any: ...
    def websocket_route(self, path: str, name: Any = ...) -> Callable[[Callable[..., Any]], Callable[..., Any]]: ...
    def on_event(self, event_type: str) -> Callable[[Callable[..., Any]], Callable[..., Any]]: ...
    def middleware(self, middleware_type: str) -> Callable[[Callable[..., Any]], Callable[..., Any]]: ...
    def exception_handler(self, exc_class_or_status_code: Any) -> Callable[[Callable[..., Any]], Callable[..., Any]]: ...
