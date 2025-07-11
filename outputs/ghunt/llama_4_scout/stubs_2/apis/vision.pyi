from ghunt.objects.base import GHuntCreds
from ghunt.errors import *
import ghunt.globals as gb
from ghunt.objects.apis import GAPI
from ghunt.parsers.vision import VisionFaceDetection
from typing import Any

class VisionHttp(GAPI):
    def __init__(self, creds: GHuntCreds, headers: dict = {}) -> None:
        ...

    async def detect_faces(self, as_client: Any, image_url: str = "", image_content: str = "", params_template: str = "default") -> tuple:
        ...