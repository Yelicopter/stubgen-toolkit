from ghunt.objects.base import GHuntCreds
from ghunt.objects.apis import GAPI
from ghunt.parsers.vision import VisionFaceDetection
import httpx
from typing import Dict, Tuple

class VisionHttp(GAPI):
    def __init__(self, creds: GHuntCreds, headers: Dict[str, str] = ...) -> None: ...
    async def detect_faces(self, as_client: httpx.AsyncClient, image_url: str = ..., image_content: str = ..., params_template: str = ...) -> Tuple[bool, bool, VisionFaceDetection]: ...