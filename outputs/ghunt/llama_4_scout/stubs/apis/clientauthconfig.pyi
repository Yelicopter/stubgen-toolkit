from ghunt.objects.base import GHuntCreds
from ghunt.errors import *
import ghunt.globals as gb
from ghunt.objects.apis import GAPI
from ghunt.parsers.clientauthconfig import CacBrand

class ClientAuthConfigHttp(GAPI):
    def __init__(self, creds: GHuntCreds, headers: dict = {}) -> None:
        ...

    async def get_brand(self, as_client: Any, project_number: str) -> tuple:
        ...