import httpx
from typing import Optional

async def check_and_login(as_client: Optional[httpx.AsyncClient], clean: bool = ...) -> None: ...
