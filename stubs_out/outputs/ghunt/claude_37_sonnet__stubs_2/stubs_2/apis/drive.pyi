from ghunt.errors import *
import httpx
from ghunt.objects.apis import GAPI
from ghunt.objects.base import GHuntCreds as GHuntCreds
from ghunt.parsers.drive import DriveChildList as DriveChildList, DriveCommentList as DriveCommentList, DriveFile as DriveFile
from typing import Dict, List, Tuple

class DriveHttp(GAPI):
    api_name: str
    package_name: str
    scopes: List[str]
    hostname: str
    scheme: str
    authentication_mode: str
    require_key: str
    def __init__(self, creds: GHuntCreds, headers: Dict[str, str] = ...) -> None: ...
    async def get_file(self, as_client: httpx.AsyncClient, file_id: str) -> Tuple[bool, DriveFile]: ...
    async def get_comments(self, as_client: httpx.AsyncClient, file_id: str, page_token: str = ...) -> Tuple[bool, str, DriveCommentList]: ...
    async def get_childs(self, as_client: httpx.AsyncClient, file_id: str, page_token: str = ...) -> Tuple[bool, str, DriveChildList]: ...
