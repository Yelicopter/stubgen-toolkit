from ghunt.errors import *
from typing import *
import httpx
from ghunt.objects.apis import GAPI
from ghunt.objects.base import GHuntCreds as GHuntCreds

class Accounts(GAPI):
    api_name: str
    package_name: str
    scopes: List[str]
    hostname: str
    scheme: str
    authentication_mode: str
    require_key: Optional[str]
    def __init__(self, creds: GHuntCreds, headers: Dict[str, str] = ...) -> None: ...
    async def OAuthLogin(self, as_client: httpx.AsyncClient) -> Tuple[bool, str]: ...
