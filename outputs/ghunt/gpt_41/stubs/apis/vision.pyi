from typing import Any, Dict, Optional, Tuple
from ghunt.objects.base import GHuntCreds
from ghunt.objects.apis import GAPI
from ghunt.parsers.vision import VisionFaceDetection

class VisionHttp(GAPI):
    def __init__(self, creds: GHuntCreds, headers: Optional[Dict[str, Any]] = ...) -> None: ...
    async def detect_faces(
        self,
        as_client: Any,
        image_url: str = ...,
        image_content: str = ...,
        params_template: str = ...,
    ) -> Tuple[bool, bool, VisionFaceDetection]: ...