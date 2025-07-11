from fastapi.security.base import SecurityBase as SecurityBase
from typing import Any, Callable, List, Tuple

class SecurityRequirement:
    security_scheme: SecurityBase
    scopes: List[str]
    def __init__(self, security_scheme, scopes) -> None: ...

class Dependant:
    path_params: List[Any]
    query_params: List[Any]
    header_params: List[Any]
    cookie_params: List[Any]
    body_params: List[Any]
    dependencies: List[Any]
    security_requirements: List[SecurityRequirement]
    name: str
    call: Callable[..., Any]
    request_param_name: str
    websocket_param_name: str
    http_connection_param_name: str
    response_param_name: str
    background_tasks_param_name: str
    security_scopes_param_name: str
    security_scopes: List[Any]
    use_cache: bool
    path: str
    cache_key: Tuple[Any, ...]
    def __post_init__(self) -> None: ...
    def __init__(self, path_params, query_params, header_params, cookie_params, body_params, dependencies, security_requirements, name, call, request_param_name, websocket_param_name, http_connection_param_name, response_param_name, background_tasks_param_name, security_scopes_param_name, security_scopes, use_cache, path) -> None: ...
