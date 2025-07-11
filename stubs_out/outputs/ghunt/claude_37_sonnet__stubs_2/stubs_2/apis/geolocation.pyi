from ghunt.errors import *
import httpx
from ghunt.objects.apis import GAPI
from ghunt.objects.base import GHuntCreds as GHuntCreds
from ghunt.parsers.geolocate import GeolocationResponse as GeolocationResponse
from typing import Dict, Tuple

class GeolocationHttp(GAPI):
    hostname: str
    scheme: str
    authentication_mode: str
    require_key: str
    def __init__(self, creds: GHuntCreds, headers: Dict[str, str] = ...) -> None: ...
    async def geolocate(self, as_client: httpx.AsyncClient, bssid: str, body: dict) -> Tuple[bool, GeolocationResponse]: ...
