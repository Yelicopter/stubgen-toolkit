from ghunt.errors import *
from ghunt.objects.apis import GAPI
from ghunt.objects.base import GHuntCreds as GHuntCreds
from ghunt.parsers.geolocate import GeolocationResponse as GeolocationResponse
from typing import Any

class GeolocationHttp(GAPI):
    def __init__(self, creds: GHuntCreds, headers: dict = ...) -> None: ...
    async def geolocate(self, as_client: Any, bssid: str, body: Any) -> tuple: ...
