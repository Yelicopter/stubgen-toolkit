from ghunt import globals as gb
from ghunt.helpers.utils import get_httpx_client
from ghunt.apis.geolocation import GeolocationHttp
from ghunt.helpers import auth
import httpx
from geopy.geocoders import Nominatim
from typing import *
from pathlib import Path
import json

async def main(as_client: Optional[httpx.AsyncClient], bssid: str, input_file: Optional[Path], json_file: Optional[Path] = None) -> None: ...