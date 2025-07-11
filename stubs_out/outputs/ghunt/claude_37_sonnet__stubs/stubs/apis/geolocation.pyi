from ghunt.errors import *
from typing import *
import httpx
from ghunt.objects.apis import GAPI
from ghunt.objects.base import GHuntCreds as GHuntCreds
from ghunt.parsers.geolocate import GeolocationResponse as GeolocationResponse

class GeolocationHttp(GAPI):
    hostname: str
    scheme: str
    authentication_mode: Optional[str]
    require_key: Optional[str]
    def __init__(self, creds: GHuntCreds, headers: Dict[str, str] = ...) -> None: ...
    async def geolocate(self, as_client: httpx.AsyncClient, bssid: str, body: dict) -> Tuple[bool, GeolocationResponse]: ...
