from typing import Any, Dict, Optional, TypeVar, Generic, Awaitable
from datetime import datetime, timezone

T = TypeVar("T")

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
    def _load_api(self, creds: Any, headers: Dict[str, Any]) -> None: ...
    def _load_endpoint(
        self,
        endpoint_name: str,
        headers: Optional[Dict[str, Any]] = ...,
        ext_metadata: Optional[Dict[str, Any]] = ...,
    ) -> None: ...
    async def _check_and_gen_authorization_token(self, as_client: Any, creds: Any) -> str: ...
    async def _query(
        self,
        as_client: Any,
        verb: str,
        endpoint_name: str,
        base_url: str,
        params: Optional[Dict[str, Any]],
        data: Any,
        data_type: Any,
    ) -> Any: ...

class Parser:
    def _merge(self, obj: Any) -> None: ...