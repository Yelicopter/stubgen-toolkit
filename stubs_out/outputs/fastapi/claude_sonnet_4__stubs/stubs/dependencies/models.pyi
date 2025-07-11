from fastapi._compat import ModelField as ModelField
from fastapi.security.base import SecurityBase as SecurityBase
from typing import Any, Callable, List, Optional, Tuple

class SecurityRequirement:
    security_scheme: SecurityBase
    scopes: Optional[List[str]]
    def __init__(self, security_scheme, scopes) -> None: ...

class Dependant:
    path_params: List[ModelField]
    query_params: List[ModelField]
    header_params: List[ModelField]
    cookie_params: List[ModelField]
    body_params: List[ModelField]
    dependencies: List['Dependant']
    security_requirements: List[SecurityRequirement]
    name: Optional[str]
    call: Optional[Callable[..., Any]]
    request_param_name: Optional[str]
    websocket_param_name: Optional[str]
    http_connection_param_name: Optional[str]
    response_param_name: Optional[str]
    background_tasks_param_name: Optional[str]
    security_scopes_param_name: Optional[str]
    security_scopes: Optional[List[str]]
    use_cache: bool
    path: Optional[str]
    cache_key: Tuple[Optional[Callable[..., Any]], Tuple[str, ...]]
    def __post_init__(self) -> None: ...
    def __init__(self, path_params, query_params, header_params, cookie_params, body_params, dependencies, security_requirements, name, call, request_param_name, websocket_param_name, http_connection_param_name, response_param_name, background_tasks_param_name, security_scopes_param_name, security_scopes, use_cache, path) -> None: ...
