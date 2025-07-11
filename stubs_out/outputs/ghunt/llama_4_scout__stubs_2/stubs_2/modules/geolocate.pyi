from geopy.geocoders import Nominatim as Nominatim
from ghunt.apis.geolocation import GeolocationHttp as GeolocationHttp
from ghunt.helpers import auth as auth
from ghunt.helpers.utils import get_httpx_client as get_httpx_client
from pathlib import Path
from typing import Any

async def main(as_client: Any, bssid: str, input_file: Path, json_file: Path = ...) -> None: ...
