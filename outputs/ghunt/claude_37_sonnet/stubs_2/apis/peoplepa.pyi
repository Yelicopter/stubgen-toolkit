from ghunt.objects.base import GHuntCreds
from ghunt.errors import *
import ghunt.globals as gb
from ghunt.objects.apis import GAPI
from ghunt.parsers.people import Person
from typing import Dict, List, Optional, Tuple
import inspect
import json
import httpx

class PeoplePaHttp(GAPI):
    hostname: str
    scheme: str
    authentication_mode: str
    require_key: str
    
    def __init__(self, creds: GHuntCreds, headers: Dict[str, str] = {}) -> None: ...
    
    async def people_lookup(self, as_client: httpx.AsyncClient, email: str, params_template: str = "just_gaia_id") -> Tuple[bool, Person]: ...
    
    async def people(self, as_client: httpx.AsyncClient, gaia_id: str, params_template: str = "just_name") -> Tuple[bool, Person]: ...