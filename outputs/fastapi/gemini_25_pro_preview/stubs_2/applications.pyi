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
    Set,
    Type,
    TypeVar,
    Union,
)

from fastapi import routing
from fastapi.datastructures import Default, DefaultPlaceholder
from fastapi.openapi.models import OpenAPI
from fastapi.params import Depends
from fastapi.routing import APIRoute
from fastapi.types import DecoratedCallable, IncEx
from fastapi.utils import generate_unique_id
from starlette.applications import Starlette
from starlette.datastructures import State
from starlette.exceptions import HTTPException
from starlette.middleware import Middleware
from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.routing import BaseRoute
from starlette.types import ASGIApp, ExceptionHandler, Lifespan, Receive, Scope, Send
from typing_extensions import deprecated

AppType = TypeVar("AppType", bound="FastAPI")

class FastAPI(Starlette):
    def __init__(
        self: AppType,
        *,
        debug: bool = False,
        routes: Optional[List[BaseRoute]] = None,
        title: str = "FastAPI",
        summary: Optional[str] = None,
        description: str = "",
        version: str = "0.1.0",
        openapi_url: Optional[str] = "/openapi.json",
        openapi_tags: Optional[List[Dict[str, Any]]] = None,
        servers: Optional[List[Dict[str, Union[str, Any]]]] = None,
        dependencies: Optional[Sequence[Depends]] = None,
        default_response_class: Type[Response] = ...,
        redirect_slashes: bool = True,
        docs_url: Optional[str] = "/docs",
        redoc_url: Optional[str] = "/redoc",
        swagger_ui_oauth2_redirect_url: Optional[str] = "/docs/oauth2-redirect",
        swagger_ui_init_oauth: Optional[Dict[str, Any]] = None,
        middleware: Optional[Sequence[Middleware]] = None,
        exception_handlers: Optional[
            Dict[Union[int, Type[Exception]], ExceptionHandler]
        ] = None,
        on_startup: Optional[Sequence[Callable[[], Any]]] = None,
        on_shutdown: Optional[Sequence[Callable[[], Any]]] = None,
        lifespan: Optional[Lifespan[AppType]] = None,
        terms_of_service: Optional[str] = None,
        contact: Optional[Dict[str, Union[str, Any]]] = None,
        license_info: Optional[Dict[str, Union[str, Any]]] = None,
        openapi_prefix: str = "",
        root_path: str = "",
        root_path_in_servers: bool = True,
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = None,
        callbacks: Optional[List[BaseRoute]] = None,
        webhooks: Optional[routing.APIRouter] = None,
        deprecated: Optional[bool] = None,
        include_in_schema: bool = True,
        swagger_ui_parameters: Optional[Dict[str, Any]] = None,
        generate_unique_id_function: Union[
            Callable[[APIRoute], str], DefaultPlaceholder[Any]
        ] = ...,
        separate_input_output_schemas: bool = True,
        **extra: Any,
    ) -> None: ...
    def openapi(self) -> Dict[str, Any]: ...
    def setup(self) -> None: ...
    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None: ...
    def add_api_route(
        self,
        path: str,
        endpoint: Callable[..., Any],
        *,
        response_model: Any = ...,
        status_code: Optional[int] = None,
        tags: Optional[List[Union[str, Enum]]] = None,
        dependencies: Optional[Sequence[Depends]] = None,
        summary: Optional[str] = None,
        description: Optional[str] = None,
        response_description: str = "Successful Response",
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = None,
        deprecated: Optional[bool] = None,
        methods: Optional[Union[Set[str], List[str]]] = None,
        operation_id: Optional[str] = None,
        response_model_include: Optional[IncEx] = None,
        response_model_exclude: Optional[IncEx] = None,
        response_model_by_alias: bool = True,
        response_model_exclude_unset: bool = False,
        response_model_exclude_defaults: bool = False,
        response_model_exclude_none: bool = False,
        include_in_schema: bool = True,
        response_class: Union[Type[Response], DefaultPlaceholder[Any]] = ...,
        name: Optional[str] = None,
        openapi_extra: Optional[Dict[str, Any]] = None,
        generate_unique_id_function: Union[
            Callable[[APIRoute], str], DefaultPlaceholder[Any]
        ] = ...,
    ) -> None: ...
    def api_route(
        self,
        path: str,
        *,
        response_model: Any = ...,
        status_code: Optional[int] = None,
        tags: Optional[List[Union[str, Enum]]] = None,
        dependencies: Optional[Sequence[Depends]] = None,
        summary: Optional[str] = None,
        description: Optional[str] = None,
        response_description: str = "Successful Response",
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = None,
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
        response_class: Union[Type[Response], DefaultPlaceholder[Any]] = ...,
        name: Optional[str] = None,
        openapi_extra: Optional[Dict[str, Any]] = None,
        generate_unique_id_function: Union[
            Callable[[APIRoute], str], DefaultPlaceholder[Any]
        ] = ...,
    ) -> Callable[[DecoratedCallable], DecoratedCallable]: ...
    def add_api_websocket_route(
        self,
        path: str,
        endpoint: Callable[..., Any],
        name: Optional[str] = None,
        *,
        dependencies: Optional[Sequence[Depends]] = None,
    ) -> None: ...
    def websocket(
        self,
        path: str,
        name: Optional[str] = None,
        *,
        dependencies: Optional[Sequence[Depends]] = None,
    ) -> Callable[[DecoratedCallable], DecoratedCallable]: ...
    def include_router(
        self,
        router: routing.APIRouter,
        *,
        prefix: str = "",
        tags: Optional[List[Union[str, Enum]]] = None,
        dependencies: Optional[Sequence[Depends]] = None,
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = None,
        deprecated: Optional[bool] = None,
        include_in_schema: bool = True,
        default_response_class: Union[Type[Response], DefaultPlaceholder[Any]] = ...,
        callbacks: Optional[List[BaseRoute]] = None,
        generate_unique_id_function: Union[
            Callable[[APIRoute], str], DefaultPlaceholder[Any]
        ] = ...,
    ) -> None: ...
    def get(
        self,
        path: str,
        *,
        response_model: Any = ...,
        status_code: Optional[int] = None,
        tags: Optional[List[Union[str, Enum]]] = None,
        dependencies: Optional[Sequence[Depends]] = None,
        summary: Optional[str] = None,
        description: Optional[str] = None,
        response_description: str = "Successful Response",
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = None,
        deprecated: Optional[bool] = None,
        operation_id: Optional[str] = None,
        response_model_include: Optional[IncEx] = None,
        response_model_exclude: Optional[IncEx] = None,
        response_model_by_alias: bool = True,
        response_model_exclude_unset: bool = False,
        response_model_exclude_defaults: bool = False,
        response_model_exclude_none: bool = False,
        include_in_schema: bool = True,
        response_class: Union[Type[Response], DefaultPlaceholder[Any]] = ...,
        name: Optional[str] = None,
        callbacks: Optional[List[BaseRoute]] = None,
        openapi_extra: Optional[Dict[str, Any]] = None,
        generate_unique_id_function: Union[
            Callable[[APIRoute], str], DefaultPlaceholder[Any]
        ] = ...,
    ) -> Callable[[DecoratedCallable], DecoratedCallable]: ...
    def put(
        self,
        path: str,
        *,
        response_model: Any = ...,
        status_code: Optional[int] = None,
        tags: Optional[List[Union[str, Enum]]] = None,
        dependencies: Optional[Sequence[Depends]] = None,
        summary: Optional[str] = None,
        description: Optional[str] = None,
        response_description: str = "Successful Response",
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = None,
        deprecated: Optional[bool] = None,
        operation_id: Optional[str] = None,
        response_model_include: Optional[IncEx] = None,
        response_model_exclude: Optional[IncEx] = None,
        response_model_by_alias: bool = True,
        response_model_exclude_unset: bool = False,
        response_model_exclude_defaults: bool = False,
        response_model_exclude_none: bool = False,
        include_in_schema: bool = True,
        response_class: Union[Type[Response], DefaultPlaceholder[Any]] = ...,
        name: Optional[str] = None,
        callbacks: Optional[List[BaseRoute]] = None,
        openapi_extra: Optional[Dict[str, Any]] = None,
        generate_unique_id_function: Union[
            Callable[[APIRoute], str], DefaultPlaceholder[Any]
        ] = ...,
    ) -> Callable[[DecoratedCallable], DecoratedCallable]: ...
    def post(
        self,
        path: str,
        *,
        response_model: Any = ...,
        status_code: Optional[int] = None,
        tags: Optional[List[Union[str, Enum]]] = None,
        dependencies: Optional[Sequence[Depends]] = None,
        summary: Optional[str] = None,
        description: Optional[str] = None,
        response_description: str = "Successful Response",
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = None,
        deprecated: Optional[bool] = None,
        operation_id: Optional[str] = None,
        response_model_include: Optional[IncEx] = None,
        response_model_exclude: Optional[IncEx] = None,
        response_model_by_alias: bool = True,
        response_model_exclude_unset: bool = False,
        response_model_exclude_defaults: bool = False,
        response_model_exclude_none: bool = False,
        include_in_schema: bool = True,
        response_class: Union[Type[Response], DefaultPlaceholder[Any]] = ...,
        name: Optional[str] = None,
        callbacks: Optional[List[BaseRoute]] = None,
        openapi_extra: Optional[Dict[str, Any]] = None,
        generate_unique_id_function: Union[
            Callable[[APIRoute], str], DefaultPlaceholder[Any]
        ] = ...,
    ) -> Callable[[DecoratedCallable], DecoratedCallable]: ...
    def delete(
        self,
        path: str,
        *,
        response_model: Any = ...,
        status_code: Optional[int] = None,
        tags: Optional[List[Union[str, Enum]]] = None,
        dependencies: Optional[Sequence[Depends]] = None,
        summary: Optional[str] = None,
        description: Optional[str] = None,
        response_description: str = "Successful Response",
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = None,
        deprecated: Optional[bool] = None,
        operation_id: Optional[str] = None,
        response_model_include: Optional[IncEx] = None,
        response_model_exclude: Optional[IncEx] = None,
        response_model_by_alias: bool = True,
        response_model_exclude_unset: bool = False,
        response_model_exclude_defaults: bool = False,
        response_model_exclude_none: bool = False,
        include_in_schema: bool = True,
        response_class: Union[Type[Response], DefaultPlaceholder[Any]] = ...,
        name: Optional[str] = None,
        callbacks: Optional[List[BaseRoute]] = None,
        openapi_extra: Optional[Dict[str, Any]] = None,
        generate_unique_id_function: Union[
            Callable[[APIRoute], str], DefaultPlaceholder[Any]
        ] = ...,
    ) -> Callable[[DecoratedCallable], DecoratedCallable]: ...
    def options(
        self,
        path: str,
        *,
        response_model: Any = ...,
        status_code: Optional[int] = None,
        tags: Optional[List[Union[str, Enum]]] = None,
        dependencies: Optional[Sequence[Depends]] = None,
        summary: Optional[str] = None,
        description: Optional[str] = None,
        response_description: str = "Successful Response",
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = None,
        deprecated: Optional[bool] = None,
        operation_id: Optional[str] = None,
        response_model_include: Optional[IncEx] = None,
        response_model_exclude: Optional[IncEx] = None,
        response_model_by_alias: bool = True,
        response_model_exclude_unset: bool = False,
        response_model_exclude_defaults: bool = False,
        response_model_exclude_none: bool = False,
        include_in_schema: bool = True,
        response_class: Union[Type[Response], DefaultPlaceholder[Any]] = ...,
        name: Optional[str] = None,
        callbacks: Optional[List[BaseRoute]] = None,
        openapi_extra: Optional[Dict[str, Any]] = None,
        generate_unique_id_function: Union[
            Callable[[APIRoute], str], DefaultPlaceholder[Any]
        ] = ...,
    ) -> Callable[[DecoratedCallable], DecoratedCallable]: ...
    def head(
        self,
        path: str,
        *,
        response_model: Any = ...,
        status_code: Optional[int] = None,
        tags: Optional[List[Union[str, Enum]]] = None,
        dependencies: Optional[Sequence[Depends]] = None,
        summary: Optional[str] = None,
        description: Optional[str] = None,
        response_description: str = "Successful Response",
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = None,
        deprecated: Optional[bool] = None,
        operation_id: Optional[str] = None,
        response_model_include: Optional[IncEx] = None,
        response_model_exclude: Optional[IncEx] = None,
        response_model_by_alias: bool = True,
        response_model_exclude_unset: bool = False,
        response_model_exclude_defaults: bool = False,
        response_model_exclude_none: bool = False,
        include_in_schema: bool = True,
        response_class: Union[Type[Response], DefaultPlaceholder[Any]] = ...,
        name: Optional[str] = None,
        callbacks: Optional[List[BaseRoute]] = None,
        openapi_extra: Optional[Dict[str, Any]] = None,
        generate_unique_id_function: Union[
            Callable[[APIRoute], str], DefaultPlaceholder[Any]
        ] = ...,
    ) -> Callable[[DecoratedCallable], DecoratedCallable]: ...
    def patch(
        self,
        path: str,
        *,
        response_model: Any = ...,
        status_code: Optional[int] = None,
        tags: Optional[List[Union[str, Enum]]] = None,
        dependencies: Optional[Sequence[Depends]] = None,
        summary: Optional[str] = None,
        description: Optional[str] = None,
        response_description: str = "Successful Response",
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = None,
        deprecated: Optional[bool] = None,
        operation_id: Optional[str] = None,
        response_model_include: Optional[IncEx] = None,
        response_model_exclude: Optional[IncEx] = None,
        response_model_by_alias: bool = True,
        response_model_exclude_unset: bool = False,
        response_model_exclude_defaults: bool = False,
        response_model_exclude_none: bool = False,
        include_in_schema: bool = True,
        response_class: Union[Type[Response], DefaultPlaceholder[Any]] = ...,
        name: Optional[str] = None,
        callbacks: Optional[List[BaseRoute]] = None,
        openapi_extra: Optional[Dict[str, Any]] = None,
        generate_unique_id_function: Union[
            Callable[[APIRoute], str], DefaultPlaceholder[Any]
        ] = ...,
    ) -> Callable[[DecoratedCallable], DecoratedCallable]: ...
    def trace(
        self,
        path: str,
        *,
        response_model: Any = ...,
        status_code: Optional[int] = None,
        tags: Optional[List[Union[str, Enum]]] = None,
        dependencies: Optional[Sequence[Depends]] = None,
        summary: Optional[str] = None,
        description: Optional[str] = None,
        response_description: str = "Successful Response",
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = None,
        deprecated: Optional[bool] = None,
        operation_id: Optional[str] = None,
        response_model_include: Optional[IncEx] = None,
        response_model_exclude: Optional[IncEx] = None,
        response_model_by_alias: bool = True,
        response_model_exclude_unset: bool = False,
        response_model_exclude_defaults: bool = False,
        response_model_exclude_none: bool = False,
        include_in_schema: bool = True,
        response_class: Union[Type[Response], DefaultPlaceholder[Any]] = ...,
        name: Optional[str] = None,
        callbacks: Optional[List[BaseRoute]] = None,
        openapi_extra: Optional[Dict[str, Any]] = None,
        generate_unique_id_function: Union[
            Callable[[APIRoute], str], DefaultPlaceholder[Any]
        ] = ...,
    ) -> Callable[[DecoratedCallable], DecoratedCallable]: ...
    def websocket_route(
        self, path: str, name: Optional[str] = None
    ) -> Callable[[DecoratedCallable], DecoratedCallable]: ...
    @deprecated(
        "on_event is deprecated, use lifespan event handlers instead.\n\nRead more about it in the FastAPI docs for Lifespan Events: https://fastapi.tiangolo.com/advanced/events/."
    )
    def on_event(
        self, event_type: str
    ) -> Callable[[DecoratedCallable], DecoratedCallable]: ...
    def middleware(
        self, middleware_type: str
    ) -> Callable[[Callable[..., Any]], Callable[..., Any]]: ...
    def exception_handler(
        self, exc_class_or_status_code: Union[int, Type[Exception]]
    ) -> Callable[[ExceptionHandler], ExceptionHandler]: ...