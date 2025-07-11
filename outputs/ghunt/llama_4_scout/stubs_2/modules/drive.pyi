from ghunt.helpers.utils import *
from ghunt.objects.base import DriveExtractedUser, GHuntCreds
from ghunt.apis.drive import DriveHttp
from ghunt.apis.clientauthconfig import ClientAuthConfigHttp
from ghunt import globals as gb
from ghunt.helpers import auth
from ghunt.helpers.drive import get_comments_from_file, get_users_from_file
from ghunt.knowledge import drive as drive_knownledge

import httpx
import inflection
import humanize

import inspect
from typing import Any
from pathlib import Path

async def hunt(as_client: Any, file_id: str, json_file: Path = None) -> None:
    ...