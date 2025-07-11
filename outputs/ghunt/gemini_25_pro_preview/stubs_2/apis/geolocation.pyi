from ghunt.objects.base import GHuntCreds
from ghunt.objects.apis import GAPI
from ghunt.parsers.geolocate import GeolocationResponse
import httpx
from typing import Dict, Tuple, Optional, Any

class GeolocationHttp(GAPI):
    def __init__(self, creds: GHuntCreds, headers: Dict[str, str] = ...) -> None: ...
    async def geolocate(self, as_client: httpx.AsyncClient, bssid: Optional[str], body: Optional[Dict[str, Any]]) -> Tuple[bool, GeolocationResponse]: ...