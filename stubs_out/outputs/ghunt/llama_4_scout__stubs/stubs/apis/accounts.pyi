from ghunt.errors import *
from ghunt.objects.apis import GAPI
from ghunt.objects.base import GHuntCreds as GHuntCreds
from httpx import Client as Client
from typing import Any

class Accounts(GAPI):
    def __init__(self, creds: GHuntCreds, headers: dict = ...) -> None: ...
    async def OAuthLogin(self, as_client: Any) -> tuple: ...
