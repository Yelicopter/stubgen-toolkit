from dataclasses import dataclass, field
from typing import Any, Callable, List, Optional, Sequence, Tuple

from fastapi.security.base import SecurityBase

@dataclass
class SecurityRequirement:
    security_scheme: SecurityBase
    scopes: List[str] = None

@dataclass
class Dependant:
    path_params: List[Any] = field(default_factory=list)
    query_params: List[Any] = field(default_factory=list)
    header_params: List[Any] = field(default_factory=list)
    cookie_params: List[Any] = field(default_factory=list)
    body_params: List[Any] = field(default_factory=list)
    dependencies: List[Any] = field(default_factory=list)
    security_requirements: List[SecurityRequirement] = field(default_factory=list)
    name: str = None
    call: Callable[..., Any] = None
    request_param_name: str = None
    websocket_param_name: str = None
    http_connection_param_name: str = None
    response_param_name: str = None
    background_tasks_param_name: str = None
    security_scopes_param_name: str = None
    security_scopes: List[Any] = None
    use_cache: bool = True
    path: str = None
    cache_key: Tuple[Any, ...] = field(init=False)

    def __post_init__(self) -> None:
        ...