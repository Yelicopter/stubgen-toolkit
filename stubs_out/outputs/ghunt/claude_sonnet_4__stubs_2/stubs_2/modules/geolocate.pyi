import httpx
from ghunt.apis.geolocation import GeolocationHttp as GeolocationHttp
from ghunt.helpers import auth as auth
from ghunt.helpers.utils import get_httpx_client as get_httpx_client
from pathlib import Path
from typing import Optional

async def main(as_client: Optional[httpx.AsyncClient], bssid: str, input_file: Optional[Path], json_file: Optional[Path] = ...) -> None: ...
