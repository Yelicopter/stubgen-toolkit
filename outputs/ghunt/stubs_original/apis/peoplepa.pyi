from ghunt.errors import *
from typing import *
import httpx
from ghunt.objects.apis import GAPI as GAPI
from ghunt.objects.base import GHuntCreds as GHuntCreds
from ghunt.parsers.people import Person as Person

class PeoplePaHttp(GAPI):
    hostname: str
    scheme: str
    authentication_mode: str
    require_key: str
    def __init__(self, creds: GHuntCreds, headers: Dict[str, str] = ...) -> None: ...
    async def people_lookup(self, as_client: httpx.AsyncClient, email: str, params_template: str = ...) -> Tuple[bool, Person]: ...
    async def people(self, as_client: httpx.AsyncClient, gaia_id: str, params_template: str = ...) -> Tuple[bool, Person]: ...
