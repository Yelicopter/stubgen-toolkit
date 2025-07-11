import asyncio
import httpx

async def call_replicate(
    input: dict[str, Any], api_token: str
) -> str:
    ...