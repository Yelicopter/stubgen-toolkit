from ghunt.errors import *
from typing import *
import httpx
from _typeshed import Incomplete
from ghunt.objects.apis import GAPI as GAPI
from ghunt.objects.base import GHuntCreds as GHuntCreds
from ghunt.parsers.drive import DriveChildList as DriveChildList, DriveCommentList as DriveCommentList, DriveFile as DriveFile

class DriveHttp(GAPI):
    api_name: str
    package_name: str
    scopes: Incomplete
    hostname: str
    scheme: str
    authentication_mode: str
    require_key: Incomplete
    def __init__(self, creds: GHuntCreds, headers: Dict[str, str] = ...) -> None: ...
    async def get_file(self, as_client: httpx.AsyncClient, file_id: str) -> Tuple[bool, DriveFile]: ...
    async def get_comments(self, as_client: httpx.AsyncClient, file_id: str, page_token: str = ...) -> Tuple[bool, str, DriveCommentList]: ...
    async def get_childs(self, as_client: httpx.AsyncClient, file_id: str, page_token: str = ...) -> Tuple[bool, str, DriveChildList]: ...
