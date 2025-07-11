from typing import *
from ghunt.helpers.utils import *
import httpx
from ghunt.errors import GHuntInvalidSession as GHuntInvalidSession
from ghunt.helpers import auth as auth
from ghunt.objects.base import GHuntCreds as GHuntCreds

async def check_and_login(as_client: httpx.AsyncClient, clean: bool = ...) -> None: ...
