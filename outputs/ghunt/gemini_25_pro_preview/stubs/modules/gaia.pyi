import httpx
from pathlib import Path
from typing import Optional

async def hunt(as_client: Optional[httpx.AsyncClient], gaia_id: str, json_file: Optional[Path] = ...) -> None: ...