from ghunt.errors import *
import httpx
from ghunt.objects.apis import GAPI
from ghunt.objects.base import GHuntCreds as GHuntCreds
from ghunt.parsers.clientauthconfig import CacBrand as CacBrand
from typing import Dict, Tuple

class ClientAuthConfigHttp(GAPI):
    hostname: str
    scheme: str
    authentication_mode: str
    require_key: str
    def __init__(self, creds: GHuntCreds, headers: Dict[str, str] = ...) -> None: ...
    async def get_brand(self, as_client: httpx.AsyncClient, project_number: str) -> Tuple[bool, CacBrand]: ...
