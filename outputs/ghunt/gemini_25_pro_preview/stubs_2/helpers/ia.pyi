from ghunt.apis.vision import VisionHttp
from ghunt.parsers.vision import VisionFaceDetection
import httpx
from typing import Optional

async def detect_face(vision_api: VisionHttp, as_client: httpx.AsyncClient, image_url: str) -> Optional[VisionFaceDetection]: ...