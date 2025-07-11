from dataclasses import field as field
from fastapi._compat import ModelField as ModelField
from fastapi.security.base import SecurityBase as SecurityBase
from typing import Any

class SecurityRequirement:
    security_scheme: SecurityBase
    scopes: Any
    def __init__(self, security_scheme, scopes) -> None: ...

class Dependant:
    path_params: Any
    query_params: Any
    header_params: Any
    cookie_params: Any
    body_params: Any
    dependencies: Any
    security_requirements: Any
    name: Any
    call: Any
    request_param_name: Any
    websocket_param_name: Any
    http_connection_param_name: Any
    response_param_name: Any
    background_tasks_param_name: Any
    security_scopes_param_name: Any
    security_scopes: Any
    use_cache: bool
    path: Any
    cache_key: Any
    def __post_init__(self) -> None: ...
    def __init__(self, path_params, query_params, header_params, cookie_params, body_params, dependencies, security_requirements, name, call, request_param_name, websocket_param_name, http_connection_param_name, response_param_name, background_tasks_param_name, security_scopes_param_name, security_scopes, use_cache, path, cache_key) -> None: ...
