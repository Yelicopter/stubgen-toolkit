from ghunt.errors import *
from ghunt.objects.apis import GAPI
from ghunt.objects.base import GHuntCreds as GHuntCreds
from ghunt.parsers.people import Person as Person
from typing import Any

class PeoplePaHttp(GAPI):
    def __init__(self, creds: GHuntCreds, headers: dict = ...) -> None: ...
    async def people_lookup(self, as_client: Any, email: str, params_template: str = ...) -> tuple: ...
    async def people(self, as_client: Any, gaia_id: str, params_template: str = ...) -> tuple: ...
