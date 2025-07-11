from ghunt.helpers.utils import *
from typing import *
import httpx
from ghunt.apis.clientauthconfig import ClientAuthConfigHttp as ClientAuthConfigHttp
from ghunt.apis.drive import DriveHttp as DriveHttp
from ghunt.helpers import auth as auth
from ghunt.helpers.drive import get_comments_from_file as get_comments_from_file, get_users_from_file as get_users_from_file
from ghunt.objects.base import DriveExtractedUser as DriveExtractedUser, GHuntCreds as GHuntCreds

def show_user(user: DriveExtractedUser): ...
async def hunt(as_client: httpx.AsyncClient, file_id: str, json_file: bool = ...): ...
