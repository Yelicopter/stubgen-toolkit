from ghunt.objects.base import GHuntCreds
from ghunt.errors import *
import ghunt.globals as gb
from ghunt.objects.apis import GAPI
from ghunt.parsers.drive import DriveCommentList, DriveFile, DriveChildList
from ghunt.knowledge import drive as drive_knowledge
import httpx
from typing import *
import inspect
import json

class DriveHttp(GAPI):
    def __init__(self, creds: GHuntCreds, headers: Dict[str, str] = {}) -> None: ...
    async def get_file(self, as_client: httpx.AsyncClient, file_id: str) -> Tuple[bool, DriveFile]: ...
    async def get_comments(self, as_client: httpx.AsyncClient, file_id: str, page_token: str = "") -> Tuple[bool, str, DriveCommentList]: ...
    async def get_childs(self, as_client: httpx.AsyncClient, file_id: str, page_token: str = "") -> Tuple[bool, str, DriveChildList]: ...