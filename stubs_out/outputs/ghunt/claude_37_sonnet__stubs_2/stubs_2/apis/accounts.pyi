from ghunt.errors import *
import httpx
from ghunt.objects.apis import GAPI
from ghunt.objects.base import GHuntCreds as GHuntCreds
from typing import Dict, List, Tuple

class Accounts(GAPI):
    api_name: str
    package_name: str
    scopes: List[str]
    hostname: str
    scheme: str
    authentication_mode: str
    require_key: str
    def __init__(self, creds: GHuntCreds, headers: Dict[str, str] = ...) -> None: ...
    async def OAuthLogin(self, as_client: httpx.AsyncClient) -> Tuple[bool, str]: ...
