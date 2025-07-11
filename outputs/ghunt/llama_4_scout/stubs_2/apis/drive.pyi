from ghunt.objects.base import GHuntCreds
from ghunt.errors import *
import ghunt.globals as gb
from ghunt.objects.apis import GAPI
from ghunt.parsers.drive import DriveCommentList, DriveFile, DriveChildList
from typing import Any

class DriveHttp(GAPI):
    def __init__(self, creds: GHuntCreds, headers: dict = {}) -> None:
        ...

    async def get_file(self, as_client: Any, file_id: str) -> tuple:
        ...

    async def get_comments(self, as_client: Any, file_id: str, page_token: str = "") -> tuple:
        ...

    async def get_childs(self, as_client: Any, file_id: str, page_token: str = "") -> tuple:
        ...