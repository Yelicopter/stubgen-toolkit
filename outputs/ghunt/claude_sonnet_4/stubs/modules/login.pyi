from typing import *
import httpx
from pathlib import Path
from ghunt import globals as gb
from ghunt.helpers.utils import *
from ghunt.helpers import auth
from ghunt.objects.base import GHuntCreds
from ghunt.errors import GHuntInvalidSession

async def check_and_login(as_client: Optional[httpx.AsyncClient], clean: bool = False) -> None: ...