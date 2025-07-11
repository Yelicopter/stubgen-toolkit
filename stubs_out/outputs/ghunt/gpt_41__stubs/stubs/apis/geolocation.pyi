from ghunt.objects.apis import GAPI
from ghunt.objects.base import GHuntCreds as GHuntCreds
from ghunt.parsers.geolocate import GeolocationResponse as GeolocationResponse
from typing import Any, Dict, Optional, Tuple

class GeolocationHttp(GAPI):
    def __init__(self, creds: GHuntCreds, headers: Optional[Dict[str, Any]] = ...) -> None: ...
    async def geolocate(self, as_client: Any, bssid: Optional[str], body: Any) -> Tuple[bool, GeolocationResponse]: ...
