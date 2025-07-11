from ghunt import globals as gb
from ghunt.helpers.utils import get_httpx_client
from ghunt.apis.geolocation import GeolocationHttp
from ghunt.helpers import auth
import httpx
from typing import Any, Optional
from pathlib import Path
import json

async def main(as_client: httpx.AsyncClient, bssid: str, input_file: Path, json_file: Optional[Path] = None) -> None: ...