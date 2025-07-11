from ghunt.apis.peoplepa import PeoplePaHttp as PeoplePaHttp
from ghunt.apis.vision import VisionHttp as VisionHttp
from ghunt.helpers import auth as auth, gmaps as gmaps, ia as ia
from ghunt.helpers.knowledge import get_user_type_definition as get_user_type_definition
from ghunt.helpers.utils import get_httpx_client as get_httpx_client
from ghunt.objects.base import GHuntCreds as GHuntCreds
from pathlib import Path
from typing import Any

async def hunt(as_client: Any, gaia_id: str, json_file: Path = ...) -> None: ...
