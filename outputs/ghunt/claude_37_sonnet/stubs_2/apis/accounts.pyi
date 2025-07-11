from ghunt.objects.base import GHuntCreds
from ghunt.errors import *
import ghunt.globals as gb
from ghunt.objects.apis import GAPI
from typing import Dict, List, Optional, Tuple
import inspect
import httpx

class Accounts(GAPI):
    api_name: str
    package_name: str
    scopes: List[str]
    hostname: str
    scheme: str
    authentication_mode: str
    require_key: str
    
    def __init__(self, creds: GHuntCreds, headers: Dict[str, str] = {}) -> None: ...
    
    async def OAuthLogin(self, as_client: httpx.AsyncClient) -> Tuple[bool, str]: ...