from ghunt import globals as gb
from ghunt.objects.base import GHuntCreds
from ghunt.apis.peoplepa import PeoplePaHttp
from ghunt.apis.vision import VisionHttp
from ghunt.helpers import gmaps, auth, ia
from ghunt.helpers.knowledge import get_user_type_definition
from ghunt.helpers.utils import get_httpx_client
import httpx
from typing import *
from pathlib import Path

async def hunt(as_client: httpx.AsyncClient, gaia_id: str, json_file: Path = None) -> None: ...