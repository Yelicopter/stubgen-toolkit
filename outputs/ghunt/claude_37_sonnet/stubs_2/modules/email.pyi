from ghunt import globals as gb
from ghunt.helpers.utils import get_httpx_client
from ghunt.objects.base import GHuntCreds
from ghunt.apis.peoplepa import PeoplePaHttp
from ghunt.apis.vision import VisionHttp
from ghunt.helpers import gmaps, playgames, auth, calendar as gcalendar, ia
from ghunt.helpers.knowledge import get_user_type_definition
import httpx
from typing import Optional
from pathlib import Path

async def hunt(as_client: httpx.AsyncClient, email_address: str, json_file: Optional[Path] = None) -> None: ...
