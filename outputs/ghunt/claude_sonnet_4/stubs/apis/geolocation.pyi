from ghunt.objects.base import GHuntCreds
from ghunt.errors import *
import ghunt.globals as gb
from ghunt.objects.apis import GAPI
from ghunt.parsers.geolocate import GeolocationResponse
import httpx
from typing import *
import inspect
import json

class GeolocationHttp(GAPI):
    def __init__(self, creds: GHuntCreds, headers: Dict[str, str] = {}) -> None: ...
    async def geolocate(self, as_client: httpx.AsyncClient, bssid: str, body: Dict) -> Tuple[bool, GeolocationResponse]: ...