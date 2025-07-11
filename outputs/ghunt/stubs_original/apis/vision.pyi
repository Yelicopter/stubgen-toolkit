from ghunt.errors import *
from typing import *
import httpx
from _typeshed import Incomplete
from ghunt.objects.apis import GAPI as GAPI
from ghunt.objects.base import GHuntCreds as GHuntCreds
from ghunt.parsers.vision import VisionFaceDetection as VisionFaceDetection

class VisionHttp(GAPI):
    hostname: str
    scheme: str
    authentication_mode: Incomplete
    require_key: str
    key_origin: str
    def __init__(self, creds: GHuntCreds, headers: Dict[str, str] = ...) -> None: ...
    async def detect_faces(self, as_client: httpx.AsyncClient, image_url: str = ..., image_content: str = ..., params_template: str = ...) -> Tuple[bool, bool, VisionFaceDetection]: ...
