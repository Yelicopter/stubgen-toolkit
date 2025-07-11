import httpx
from ghunt.apis.vision import VisionHttp as VisionHttp

async def detect_face(vision_api: VisionHttp, as_client: httpx.AsyncClient, image_url: str) -> None: ...
