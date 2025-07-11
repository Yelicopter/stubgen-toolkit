from typing import Any, Callable, Coroutine, Dict, List, Mapping, Optional, Sequence, Set, Tuple, Type, Union
from starlette.routing import BaseRoute, Match
from starlette.types import AppType, ASGIApp, Lifespan, Scope
from starlette.responses import JSONResponse, Response
from fastapi.datastructures import Default, DefaultPlaceholder
from fastapi.types import DecoratedCallable, IncEx

def _prepare_response_content(
    res: Any,
    *,
    exclude_unset: bool,
    exclude_defaults: bool = ...,
    exclude_none: bool = ...,
) -> Any: ...
def _merge_lifespan_context(
    original_context: Any, nested_context: Any
) -> Any: ...
async def serialize_response(
    *,
    field: Any = ...,
    response_content: Any,
    include: Any = ...,
    exclude: Any = ...,
    by_alias: bool = ...,
    exclude_unset: bool = ...,
    exclude_defaults: bool = ...,
    exclude_none: bool = ...,
    is_coroutine: bool = ...,
) -> Any: ...
async def run_endpoint_function(
    *, dependant: Any, values: Any, is_coroutine: bool
) -> Any: ...
def get_request_handler(
    dependant: Any,
    body_field: Any = ...,
    status_code: Any = ...,
    response_class: Any = ...,
    response_field: Any = ...,
    response_model_include: Any = ...,
    response_model_exclude: Any = ...,
    response_model_by_alias: bool = ...,
    response_model_exclude_unset: bool = ...,
    response_model_exclude_defaults: bool = ...,
    response_model_exclude_none: bool = ...,
    dependency_overrides_provider: Any = ...,
    embed_body_fields: bool = ...,
) -> Callable[..., Coroutine[Any, Any, Response]]: ...
def get_websocket_app(
    dependant: Any,
    dependency_overrides_provider: Any = ...,
    embed_body_fields: bool = ...,
) -> Callable[..., Coroutine[Any, Any, None]]: ...

class APIWebSocketRoute(BaseRoute):
    path: str
    endpoint: Callable[..., Any]
    name: str
    dependencies: list
    path_regex: Any
    path_format: str
    param_convertors: Any
    dependant: Any
    _flat_dependant: Any
    _embed_body_fields: bool
    app: Any
    def __init__(
        self,
        path: str,
        endpoint: Callable[..., Any],
        *,
        name: Any = ...,
        dependencies: Any = ...,
        dependency_overrides_provider: Any = ...,
    ) -> None: ...
    def matches(self, scope: Scope) -> Tuple[Match, dict]: ...

class APIRoute(BaseRoute):
    path: str
    endpoint: Callable[..., Any]
    response_model: Any
    summary: Any
    response_description: str
    deprecated: Any
    operation_id: Any
    response_model_include: Any
    response_model_exclude: Any
    response_model_by_alias: bool
    response_model_exclude_unset: bool
    response_model_exclude_defaults: bool
    response_model_exclude_none: bool
    include_in_schema: bool
    response_class: Any
    dependency_overrides_provider: Any
    callbacks: Any
    openapi_extra: Any
    generate_unique_id_function: Any
    tags: list
    responses: dict
    name: str
    path_regex: Any
    path_format: str
    param_convertors: Any
    methods: Set[str]
    unique_id: str
    status_code: Any
    response_field: Any
    secure_cloned_response_field: Any
    dependencies: list
    description: str
    response_fields: dict
    dependant: Any
    _flat_dependant: Any
    _embed_body_fields: bool
    body_field: Any
    app: Any
    def __init__(
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
        name: Any = ...,
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
        dependency_overrides_provider: Any = ...,
        callbacks: Any = ...,
        openapi_extra: Any = ...,
        generate_unique_id_function: Any = ...,
    ) -> None: ...
    def get_route_handler(self) -> Callable[..., Coroutine[Any, Any, Response]]: ...
    def matches(self, scope: Scope) -> Tuple[Match, dict]: ...

class APIRouter(BaseRoute):
    prefix: str
    tags: list
    dependencies: list
    deprecated: Any
    include_in_schema: bool
    responses: dict
    callbacks: list
    dependency_overrides_provider: Any
    route_class: Any
    default_response_class: Any
    generate_unique_id_function: Any
    def __init__(
        self,
        *,
        prefix: str = ...,
        tags: Any = ...,
        dependencies: Any = ...,
        default_response_class: Any = ...,
        responses: Any = ...,
        callbacks: Any = ...,
        routes: Any = ...,
        redirect_slashes: bool = ...,
        default: Any = ...,
        dependency_overrides_provider: Any = ...,
        route_class: Any = ...,
        on_startup: Any = ...,
        on_shutdown: Any = ...,
        lifespan: Any = ...,
        deprecated: Any = ...,
        include_in_schema: bool = ...,
        generate_unique_id_function: Any = ...,
    ) -> None: ...
    def route(
        self,
        path: str,
        methods: Any = ...,
        name: Any = ...,
        include_in_schema: bool = ...,
    ) -> Callable[[Callable[..., Any]], Callable[..., Any]]: ...
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
        route_class_override: Any = ...,
        callbacks: Any = ...,
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
        callbacks: Any = ...,
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
    def websocket_route(self, path: str, name: Any = ...) -> Callable[[Callable[..., Any]], Callable[..., Any]]: ...
    def include_router(
        self,
        router: "APIRouter",
        *,
        prefix: str = ...,
        tags: Any = ...,
        dependencies: Any = ...,
        default_response_class: Any = ...,
        responses: Any = ...,
        callbacks: Any = ...,
        deprecated: Any = ...,
        include_in_schema: bool = ...,
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
    def on_event(self, event_type: str) -> Callable[[Callable[..., Any]], Callable[..., Any]]: ...