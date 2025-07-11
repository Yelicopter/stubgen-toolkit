from ghunt.objects.base import GHuntCreds
from ghunt.errors import *
import ghunt.globals as gb
from ghunt.objects.apis import GAPI
from ghunt.parsers.geolocate import GeolocationResponse
from typing import *
import inspect
import json
import httpx

class GeolocationHttp(GAPI):
    hostname: str
    scheme: str
    authentication_mode: Optional[str]
    require_key: Optional[str]
    
    def __init__(self, creds: GHuntCreds, headers: Dict[str, str] = {}) -> None: ...
    
    async def geolocate(self, as_client: httpx.AsyncClient, bssid: str, body: dict) -> Tuple[bool, GeolocationResponse]: ...