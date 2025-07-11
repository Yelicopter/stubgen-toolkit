from ghunt import globals as gb
from ghunt.apis.vision import VisionHttp
import httpx
from base64 import b64encode
import asyncio
from typing import Any, Optional

async def detect_face(vision_api: VisionHttp, as_client: httpx.AsyncClient, image_url: str) -> Optional[Any]: ...