import httpx
import asyncio
from ghunt.objects.base import GHuntCreds, SmartObj
from typing import Dict, Optional, Any

class EndpointConfig(SmartObj):
    headers: Dict[str, str]
    cookies: Dict[str, str]
    def __init__(self, headers: Dict[str, str], cookies: Dict[str, str]) -> None: ...

class GAPI(SmartObj):
    loaded_endpoints: Dict[str, EndpointConfig]
    creds: Optional[GHuntCreds]
    headers: Dict[str, str]
    cookies: Dict[str, str]
    gen_token_lock: Optional[asyncio.Semaphore]
    authentication_mode: str
    require_key: str
    key_origin: str
    def __init__(self) -> None: ...
    def _load_api(self, creds: GHuntCreds, headers: Dict[str, str]) -> None: ...
    def _load_endpoint(self, endpoint_name: str, headers: Dict[str, str] = ..., ext_metadata: Dict[str, Dict[str, str]] = ...) -> None: ...
    async def _check_and_gen_authorization_token(self, as_client: httpx.AsyncClient, creds: GHuntCreds) -> str: ...
    async def _query(self, as_client: httpx.AsyncClient, verb: str, endpoint_name: str, base_url: str, params: Optional[Dict[str, Any]], data: Optional[Any], data_type: Optional[str]) -> httpx.Response: ...

class Parser(SmartObj):
    def _merge(self, obj: Any) -> None: ...