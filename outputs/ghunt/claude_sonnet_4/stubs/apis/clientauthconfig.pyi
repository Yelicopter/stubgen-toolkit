from ghunt.objects.base import GHuntCreds
from ghunt.errors import *
import ghunt.globals as gb
from ghunt.objects.apis import GAPI
from ghunt.parsers.clientauthconfig import CacBrand
import httpx
from typing import *
import inspect
import json

class ClientAuthConfigHttp(GAPI):
    def __init__(self, creds: GHuntCreds, headers: Dict[str, str] = {}) -> None: ...
    async def get_brand(self, as_client: httpx.AsyncClient, project_number: str) -> Tuple[bool, CacBrand]: ...