import base64
import io
from typing import Any

from PIL import Image

from .base import BaseResponse

class ChartResponse(BaseResponse):
    def __init__(self, value: Any, last_code_executed: str) -> None:
        ...

    def _get_image(self) -> Image:
        ...

    def save(self, path: str) -> None:
        ...

    def show(self) -> None:
        ...

    def __str__(self) -> str:
        ...

    def get_base64_image(self) -> str:
        ...