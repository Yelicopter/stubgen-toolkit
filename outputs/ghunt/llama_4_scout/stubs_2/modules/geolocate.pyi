from ghunt import globals as gb
from ghunt.helpers.utils import get_httpx_client
from ghunt.apis.geolocation import GeolocationHttp
from ghunt.helpers import auth

import httpx
from geopy.geocoders import Nominatim
from pathlib import Path
from typing import Any

async def main(as_client: Any, bssid: str, input_file: Path, json_file: Path = None) -> None:
    ...