from base64 import b64encode as b64encode
from ghunt.apis.vision import VisionHttp as VisionHttp
from typing import Any

async def detect_face(vision_api: VisionHttp, as_client: Any, image_url: str) -> Any: ...
