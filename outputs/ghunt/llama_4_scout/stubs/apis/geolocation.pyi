from ghunt.objects.base import GHuntCreds
from ghunt.errors import *
import ghunt.globals as gb
from ghunt.objects.apis import GAPI
from ghunt.parsers.geolocate import GeolocationResponse

class GeolocationHttp(GAPI):
    def __init__(self, creds: GHuntCreds, headers: dict = {}) -> None:
        ...

    async def geolocate(self, as_client: Any, bssid: str, body: Any) -> tuple:
        ...