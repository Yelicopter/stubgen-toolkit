import httpx
from typing import Any

async def is_email_registered(as_client: Any, email: str) -> bool:
    ...