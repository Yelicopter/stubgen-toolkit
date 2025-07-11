from ghunt.errors import *
from ghunt.objects.apis import GAPI
from ghunt.objects.base import GHuntCreds as GHuntCreds
from ghunt.parsers.clientauthconfig import CacBrand as CacBrand
from typing import Any

class ClientAuthConfigHttp(GAPI):
    def __init__(self, creds: GHuntCreds, headers: dict = ...) -> None: ...
    async def get_brand(self, as_client: Any, project_number: str) -> tuple: ...
