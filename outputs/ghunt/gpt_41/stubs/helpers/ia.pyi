from typing import Any

from ghunt.apis.vision import VisionHttp

async def detect_face(vision_api: VisionHttp, as_client: Any, image_url: str) -> Any: ...