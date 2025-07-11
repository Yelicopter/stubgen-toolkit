from enum import Enum as Enum
from fastapi import routing as routing
from fastapi.datastructures import DefaultPlaceholder as DefaultPlaceholder
from fastapi.exception_handlers import http_exception_handler as http_exception_handler, request_validation_exception_handler as request_validation_exception_handler, websocket_request_validation_exception_handler as websocket_request_validation_exception_handler
from fastapi.exceptions import RequestValidationError as RequestValidationError, WebSocketRequestValidationError as WebSocketRequestValidationError
from fastapi.logger import logger as logger
from fastapi.openapi.docs import get_redoc_html as get_redoc_html, get_swagger_ui_html as get_swagger_ui_html, get_swagger_ui_oauth2_redirect_html as get_swagger_ui_oauth2_redirect_html
from fastapi.openapi.utils import get_openapi as get_openapi
from fastapi.params import Depends as Depends
from fastapi.types import DecoratedCallable as DecoratedCallable, IncEx as IncEx
from starlette.applications import Starlette
from starlette.datastructures import State as State
from starlette.exceptions import HTTPException as HTTPException
from starlette.middleware import Middleware as Middleware
from starlette.middleware.base import BaseHTTPMiddleware as BaseHTTPMiddleware
from starlette.requests import Request as Request
from starlette.responses import HTMLResponse as HTMLResponse, Response as Response
from starlette.routing import BaseRoute as BaseRoute
from starlette.types import ASGIApp as ASGIApp, Lifespan as Lifespan, Receive as Receive, Scope as Scope, Send as Send
from typing import Any, Callable, Dict, List, Optional, Type, TypeVar

AppType = TypeVar('AppType', bound='FastAPI')

class FastAPI(Starlette):
    def __init__(self, *, debug: bool = ..., routes: Optional[List[BaseRoute]] = ..., title: str = ..., summary: Optional[str] = ..., description: str = ..., version: str = ..., openapi_url: Optional[str] = ..., openapi_tags: Optional[List[Dict[str, Any]]] = ..., servers: Optional[List[Dict[str, Any]]] = ..., dependencies: Optional[List[Depends]] = ..., default_response_class: Type[Response] = ..., redirect_slashes: bool = ..., docs_url: Optional[str] = ..., redoc_url: Optional[str] = ..., swagger_ui_oauth2_redirect_url: Optional[str] = ..., swagger_ui_init_oauth: Optional[Dict[str, Any]] = ..., middleware: Optional[List[Middleware]] = ..., exception_handlers: Optional[Dict[Type[Exception], Callable]] = ..., on_startup: Optional[Callable] = ..., on_shutdown: Optional[Callable] = ..., lifespan: Optional[Callable] = ..., terms_of_service: Optional[str] = ..., contact: Optional[Dict[str, Any]] = ..., license_info: Optional[Dict[str, Any]] = ..., openapi_prefix: str = ..., root_path: str = ..., root_path_in_servers: bool = ..., responses: Optional[Dict[int, Dict[str, Any]]]) -> None: ...
    def openapi(self) -> Dict[str, Any]: ...
    def setup(self) -> None: ...
    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None: ...
    def add_api_route(self, path: str, endpoint: Callable, *, response_model: Optional[Type[Any]] = ..., status_code: Optional[int] = ..., tags: Optional[List[str]] = ..., dependencies: Optional[List[Depends]] = ..., summary: Optional[str] = ..., description: Optional[str] = ..., response_description: str = ..., responses: Optional[Dict[int, Dict[str, Any]]] = ..., deprecated: Optional[bool] = ..., methods: Optional[List[str]] = ..., operation_id: Optional[str] = ..., response_model_include: Optional[IncEx] = ..., response_model_exclude: Optional[IncEx] = ..., response_model_by_alias: bool = ..., response_model_exclude_unset: bool = ..., response_model_exclude_defaults: bool = ..., response_model_exclude_none: bool = ..., include_in_schema: bool = ..., response_class: Type[Response] = ..., name: Optional[str] = ..., openapi_extra: Optional[Any] = ..., generate_unique_id_function: Callable[..., str] = ...) -> None: ...
    def api_route(self, path: str, *, response_model: Optional[Type[Any]] = ..., status_code: Optional[int] = ..., tags: Optional[List[str]] = ..., dependencies: Optional[List[Depends]] = ..., summary: Optional[str] = ..., description: Optional[str] = ..., response_description: str = ..., responses: Optional[Dict[int, Dict[str, Any]]] = ..., deprecated: Optional[bool] = ..., methods: Optional[List[str]] = ..., operation_id: Optional[str] = ..., response_model_include: Optional[IncEx] = ..., response_model_exclude: Optional[IncEx] = ..., response_model_by_alias: bool = ..., response_model_exclude_unset: bool = ..., response_model_exclude_defaults: bool = ..., response_model_exclude_none: bool = ..., include_in_schema: bool = ..., response_class: Type[Response] = ..., name: Optional[str] = ..., openapi_extra: Optional[Any] = ..., generate_unique_id_function: Callable[..., str] = ...) -> Callable: ...
    def add_api_websocket_route(self, path: str, endpoint: Callable, name: Optional[str] = ..., *, dependencies: Optional[List[Depends]] = ...) -> None: ...
    def websocket(self, path: str, name: Optional[str] = ..., *, dependencies: Optional[List[Depends]] = ...) -> Callable: ...
    def include_router(self, router: routing.APIRouter, *, prefix: str = ..., tags: Optional[List[str]] = ..., dependencies: Optional[List[Depends]] = ..., responses: Optional[Dict[int, Dict[str, Any]]] = ..., deprecated: Optional[bool] = ..., include_in_schema: bool = ..., default_response_class: Type[Response] = ..., callbacks: Optional[List[Callable]] = ..., generate_unique_id_function: Callable[..., str] = ...) -> None: ...
    def get(self, path: str, *, response_model: Optional[Type[Any]] = ..., status_code: Optional[int] = ..., tags: Optional[List[str]] = ..., dependencies: Optional[List[Depends]] = ..., summary: Optional[str] = ..., description: Optional[str] = ..., response_description: str = ..., responses: Optional[Dict[int, Dict[str, Any]]] = ..., deprecated: Optional[bool] = ..., operation_id: Optional[str] = ..., response_model_include: Optional[IncEx] = ..., response_model_exclude: Optional[IncEx] = ..., response_model_by_alias: bool = ..., response_model_exclude_unset: bool = ..., response_model_exclude_defaults: bool = ..., response_model_exclude_none: bool = ..., include_in_schema: bool = ..., response_class: Type[Response] = ..., name: Optional[str] = ..., callbacks: Optional[List[Callable]] = ..., openapi_extra: Optional[Any] = ..., generate_unique_id_function: Callable[..., str] = ...) -> Callable: ...
