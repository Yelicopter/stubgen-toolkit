from ghunt.objects.base import GHuntCreds
from ghunt.errors import *
import ghunt.globals as gb
from ghunt.objects.apis import GAPI
from ghunt.parsers.people import Person
from typing import Any

class PeoplePaHttp(GAPI):
    def __init__(self, creds: GHuntCreds, headers: dict = {}) -> None:
        ...

    async def people_lookup(self, as_client: Any, email: str, params_template: str = "just_gaia_id") -> tuple:
        ...

    async def people(self, as_client: Any, gaia_id: str, params_template: str = "just_name") -> tuple:
        ...