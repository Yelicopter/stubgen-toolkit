import httpx
from pathlib import Path
from typing import Optional

async def main(as_client: Optional[httpx.AsyncClient], bssid: Optional[str], input_file: Optional[Path], json_file: Optional[Path] = ...) -> None: ...