from ghunt.objects.base import GHuntCreds
from ghunt.errors import *
import ghunt.globals as gb
from ghunt.objects.apis import GAPI
from ghunt.parsers.clientauthconfig import CacBrand
from typing import Dict, List, Optional, Tuple
import inspect
import json
import httpx

class ClientAuthConfigHttp(GAPI):
    hostname: str
    scheme: str
    authentication_mode: str
    require_key: str
    
    def __init__(self, creds: GHuntCreds, headers: Dict[str, str] = {}) -> None: ...
    
    async def get_brand(self, as_client: httpx.AsyncClient, project_number: str) -> Tuple[bool, CacBrand]: ...