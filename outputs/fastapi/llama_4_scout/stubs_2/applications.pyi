from enum import Enum
from typing import (
    Any,
    Awaitable,
    Callable,
    Coroutine,
    Dict,
    List,
    Optional,
    Sequence,
    Type,
    TypeVar,
    Union,
)

from fastapi import routing
from fastapi.datastructures import Default, DefaultPlaceholder
from fastapi.exception_handlers import (
    http_exception_handler,
    request_validation_exception_handler,
    websocket_request_validation_exception_handler,
)
from fastapi.exceptions import RequestValidationError, WebSocketRequestValidationError
from fastapi.logger import logger
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)
from fastapi.openapi.utils import get_openapi
from fastapi.params import Depends
from fastapi.types import DecoratedCallable, IncEx
from fastapi.utils import generate_unique_id
from starlette.applications import Starlette
from starlette.datastructures import State
from starlette.exceptions import HTTPException
from starlette.middleware import Middleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import HTMLResponse, JSONResponse, Response
from starlette.routing import BaseRoute
from starlette.types import ASGIApp, Lifespan, Receive, Scope, Send
from typing_extensions import Annotated

AppType = TypeVar("AppType", bound="FastAPI")

class FastAPI(Starlette):
    def __init__(
        self,
        *,
        debug: bool = False,
        routes: Optional[List[BaseRoute]] = None,
        title: str = "FastAPI",
        summary: Optional[str] = None,
        description: str = "",
        version: str = "0.1.0",
        openapi_url: Optional[str] = "/openapi.json",
        openapi_tags: Optional[List[Dict[str, Any]]] = None,
        servers: Optional[List[Dict[str, Any]]] = None,
        dependencies: Optional[List[Depends]] = None,
        default_response_class: Type[Response] = Default(JSONResponse),
        redirect_slashes: bool = True,
        docs_url: Optional[str] = "/docs",
        redoc_url: Optional[str] = "/redoc",
        swagger_ui_oauth2_redirect_url: Optional[str] = "/docs/oauth2-redirect",
        swagger_ui_init_oauth: Optional[Dict[str, Any]] = None,
        middleware: Optional[List[Middleware]] = None,
        exception_handlers: Optional[Dict[Type[Exception], Callable]] = None,
        on_startup: Optional[Callable] = None,
        on_shutdown: Optional[Callable] = None,
        lifespan: Optional[Callable] = None,
        terms_of_service: Optional[str] = None,
        contact: Optional[Dict[str, Any]] = None,
        license_info: Optional[Dict[str, Any]] = None,
        openapi_prefix: str = "",
        root_path: str = "",
        root_path_in_servers: bool = True,
        responses: Optional[Dict[int, Dict[str, Any]]] = None,
        callbacks: Optional[List[Callable]] = None,
        webhooks: Optional[routing.APIRouter] = None,
        deprecated: Optional[bool] = None,
        include_in_schema: bool = True,
        swagger_ui_parameters: Optional[Dict[str, Any]] = None,
        generate_unique_id_function: Callable[..., str] = Default(generate_unique_id),
        separate_input_output_schemas: bool = True,
        **extra: Any,
    ) -> None:
        ...

    def openapi(self) -> Dict[str, Any]:
        ...

    def setup(self) -> None:
        ...

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        ...

    def add_api_route(
        self,
        path: str,
        endpoint: Callable,
        *,
        response_model: Optional[Type[Any]] = Default(None),
        status_code: Optional[int] = None,
        tags: Optional[List[str]] = None,
        dependencies: Optional[List[Depends]] = None,
        summary: Optional[str] = None,
        description: Optional[str] = None,
        response_description: str = "Successful Response",
        responses: Optional[Dict[int, Dict[str, Any]]] = None,
        deprecated: Optional[bool] = None,
        methods: Optional[List[str]] = None,
        operation_id: Optional[str] = None,
        response_model_include: Optional[IncEx] = None,
        response_model_exclude: Optional[IncEx] = None,
        response_model_by_alias: bool = True,
        response_model_exclude_unset: bool = False,
        response_model_exclude_defaults: bool = False,
        response_model_exclude_none: bool = False,
        include_in_schema: bool = True,
        response_class: Type[Response] = Default(JSONResponse),
        name: Optional[str] = None,
        openapi_extra: Optional[Any] = None,
        generate_unique_id_function: Callable[..., str] = Default(generate_unique_id),
    ) -> None:
        ...

    def api_route(
        self,
        path: str,
        *,
        response_model: Optional[Type[Any]] = Default(None),
        status_code: Optional[int] = None,
        tags: Optional[List[str]] = None,
        dependencies: Optional[List[Depends]] = None,
        summary: Optional[str] = None,
        description: Optional[str] = None,
        response_description: str = "Successful Response",
        responses: Optional[Dict[int, Dict[str, Any]]] = None,
        deprecated: Optional[bool] = None,
        methods: Optional[List[str]] = None,
        operation_id: Optional[str] = None,
        response_model_include: Optional[IncEx] = None,
        response_model_exclude: Optional[IncEx] = None,
        response_model_by_alias: bool = True,
        response_model_exclude_unset: bool = False,
        response_model_exclude_defaults: bool = False,
        response_model_exclude_none: bool = False,
        include_in_schema: bool = True,
        response_class: Type[Response] = Default(JSONResponse),
        name: Optional[str] = None,
        openapi_extra: Optional[Any] = None,
        generate_unique_id_function: Callable[..., str] = Default(generate_unique_id),
    ) -> Callable:
        ...

    def add_api_websocket_route(
        self,
        path: str,
        endpoint: Callable,
        name: Optional[str] = None,
        *,
        dependencies: Optional[List[Depends]] = None,
    ) -> None:
        ...

    def websocket(
        self,
        path: str,
        name: Optional[str] = None,
        *,
        dependencies: Optional[List[Depends]] = None,
    ) -> Callable:
        ...

    def include_router(
        self,
        router: routing.APIRouter,
        *,
        prefix: str = "",
        tags: Optional[List[str]] = None,
        dependencies: Optional[List[Depends]] = None,
        responses: Optional[Dict[int, Dict[str, Any]]] = None,
        deprecated: Optional[bool] = None,
        include_in_schema: bool = True,
        default_response_class: Type[Response] = Default(JSONResponse),
        callbacks: Optional[List[Callable]] = None,
        generate_unique_id_function: Callable[..., str] = Default(generate_unique_id),
    ) -> None:
        ...

    def get(
        self,
        path: str,
        *,
        response_model: Optional[Type[Any]] = Default(None),
        status_code: Optional[int] = None,
        tags: Optional[List[str]] = None,
        dependencies: Optional[List[Depends]] = None,
        summary: Optional[str] = None,
        description: Optional[str] = None,
        response_description: str = "Successful Response",
        responses: Optional[Dict[int, Dict[str, Any]]] = None,
        deprecated: Optional[bool] = None,
        operation_id: Optional[str] = None,
        response_model_include: Optional[IncEx] = None,
        response_model_exclude: Optional[IncEx] = None,
        response_model_by_alias: bool = True,
        response_model_exclude_unset: bool = False,
        response_model_exclude_defaults: bool = False,
        response_model_exclude_none: bool = False,
        include_in_schema: bool = True,
        response_class: Type[Response] = Default(JSONResponse),
        name: Optional[str] = None,
        callbacks: Optional[List[Callable]] = None,
        openapi_extra: Optional[Any] = None,
        generate_unique_id_function: Callable[..., str] = Default(generate_unique_id),
    ) -> Callable:
        ...

    # ... rest of your code
