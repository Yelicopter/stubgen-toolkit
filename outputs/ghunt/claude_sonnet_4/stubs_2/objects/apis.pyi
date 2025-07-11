from ghunt.errors import GHuntCorruptedHeadersError
from ghunt.helpers.knowledge import get_origin_of_key, get_api_key
from ghunt.objects.base import GHuntCreds, SmartObj
from ghunt.helpers.utils import *
from ghunt.errors import *
from ghunt.helpers.auth import *
import httpx
from datetime import datetime, timezone
from typing import *
import asyncio

class EndpointConfig(SmartObj):
    def __init__(self, headers: Dict[str, str], cookies: str) -> None: ...
    headers: Dict[str, str]
    cookies: str

class GAPI(SmartObj):
    def __init__(self) -> None: ...
    loaded_endpoints: Dict[str, EndpointConfig]
    creds: Optional[GHuntCreds]
    headers: Dict[str, str]
    cookies: Dict[str, str]
    gen_token_lock: Optional[asyncio.Semaphore]
    authentication_mode: str
    require_key: str
    key_origin: str
    
    def _load_api(self, creds: GHuntCreds, headers: Dict[str, str]) -> None: ...
    def _load_endpoint(self, endpoint_name: str,
                        headers: Dict[str, str] = {}, ext_metadata: Dict[str, Dict[str, str]] = {}) -> None: ...
    async def _check_and_gen_authorization_token(self, as_client: httpx.AsyncClient, creds: GHuntCreds) -> str: ...
    async def _query(self, as_client: httpx.AsyncClient, verb: str, endpoint_name: str, base_url: str, params: Optional[Dict[str, Any]], data: Any, data_type: str) -> httpx.Response: ...

class Parser(SmartObj):
    def _merge(self, obj: Any) -> None: ...