import httpx
from ghunt.objects.base import DriveExtractedUser as DriveExtractedUser
from pathlib import Path
from typing import Optional

def show_user(user: DriveExtractedUser) -> None: ...
async def hunt(as_client: Optional[httpx.AsyncClient], file_id: str, json_file: Optional[Path] = ...) -> None: ...
