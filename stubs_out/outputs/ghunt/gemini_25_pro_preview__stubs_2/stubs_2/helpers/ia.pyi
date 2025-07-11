import httpx
from ghunt.apis.vision import VisionHttp as VisionHttp
from ghunt.parsers.vision import VisionFaceDetection as VisionFaceDetection
from typing import Optional

async def detect_face(vision_api: VisionHttp, as_client: httpx.AsyncClient, image_url: str) -> Optional[VisionFaceDetection]: ...
