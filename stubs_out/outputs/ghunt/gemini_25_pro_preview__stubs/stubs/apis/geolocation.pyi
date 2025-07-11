import httpx
from ghunt.objects.apis import GAPI
from ghunt.objects.base import GHuntCreds as GHuntCreds
from ghunt.parsers.geolocate import GeolocationResponse as GeolocationResponse
from typing import Any, Dict, Optional, Tuple

class GeolocationHttp(GAPI):
    def __init__(self, creds: GHuntCreds, headers: Dict[str, str] = ...) -> None: ...
    async def geolocate(self, as_client: httpx.AsyncClient, bssid: Optional[str], body: Optional[Dict[str, Any]]) -> Tuple[bool, GeolocationResponse]: ...
