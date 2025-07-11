from dataclasses import dataclass, field
from typing import Any, Callable, List, Optional, Sequence, Tuple
from fastapi._compat import ModelField
from fastapi.security.base import SecurityBase

@dataclass
class SecurityRequirement:
    security_scheme: SecurityBase
    scopes: Any

@dataclass
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