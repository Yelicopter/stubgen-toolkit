from ghunt.helpers.utils import *
from ghunt.errors import GHuntInvalidSession as GHuntInvalidSession
from ghunt.helpers import auth as auth
from ghunt.objects.base import GHuntCreds as GHuntCreds
from pathlib import Path as Path
from typing import Any

async def check_and_login(as_client: Any, clean: bool = ...) -> None: ...
