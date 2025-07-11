from typing import Any, Dict, Optional, Tuple
from ghunt.objects.base import GHuntCreds
from ghunt.objects.apis import GAPI
from ghunt.parsers.drive import DriveCommentList, DriveFile, DriveChildList

class DriveHttp(GAPI):
    def __init__(self, creds: GHuntCreds, headers: Optional[Dict[str, Any]] = ...) -> None: ...
    async def get_file(self, as_client: Any, file_id: str) -> Tuple[bool, DriveFile]: ...
    async def get_comments(
        self,
        as_client: Any,
        file_id: str,
        page_token: str = ...,
    ) -> Tuple[bool, str, DriveCommentList]: ...
    async def get_childs(
        self,
        as_client: Any,
        file_id: str,
        page_token: str = ...,
    ) -> Tuple[bool, str, DriveChildList]: ...