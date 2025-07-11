from ghunt import globals as gb
from ghunt.apis.vision import VisionHttp

import httpx

from base64 import b64encode
import asyncio
from typing import Any

async def detect_face(vision_api: VisionHttp, as_client: Any, image_url: str) -> Any:
    ...