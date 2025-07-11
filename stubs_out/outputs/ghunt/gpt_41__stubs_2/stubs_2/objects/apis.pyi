from datetime import datetime as datetime, timezone as timezone
from typing import Any, Dict, TypeVar

T = TypeVar('T')

class EndpointConfig:
    def __init__(self, headers: Dict[str, Any], cookies: Dict[str, Any]) -> None: ...

class GAPI:
    loaded_endpoints: Dict[str, EndpointConfig]
    creds: Any
    headers: Dict[str, Any]
    cookies: Dict[str, Any]
    gen_token_lock: Any
    authentication_mode: str
    require_key: str
    key_origin: str
    api_name: str
    package_name: str
    scopes: Any
    def __init__(self) -> None: ...

class Parser: ...
