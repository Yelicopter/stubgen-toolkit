from ghunt.objects.base import GHuntCreds
from ghunt.errors import *
import ghunt.globals as gb
from ghunt.objects.apis import GAPI
import httpx
from typing import *
import inspect

class Accounts(GAPI):
    def __init__(self, creds: GHuntCreds, headers: Dict[str, str] = {}) -> None: ...
    async def OAuthLogin(self, as_client: httpx.AsyncClient) -> Tuple[bool, str]: ...