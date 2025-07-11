from ghunt.objects.base import GHuntCreds
from ghunt.objects.apis import GAPI
import httpx
from typing import Dict, Tuple

class Accounts(GAPI):
    def __init__(self, creds: GHuntCreds, headers: Dict[str, str] = ...) -> None: ...
    async def OAuthLogin(self, as_client: httpx.AsyncClient) -> Tuple[bool, str]: ...