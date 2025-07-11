import asyncio
import httpx
from typing import Dict, Any

async def call_replicate(input: Dict[str, Any], api_token: str) -> str: ...