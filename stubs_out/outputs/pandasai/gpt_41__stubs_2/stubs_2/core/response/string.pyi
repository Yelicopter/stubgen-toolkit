from .base import BaseResponse as BaseResponse
from typing import Any

class StringResponse(BaseResponse):
    def __init__(self, value: str, **kwargs: Any) -> None: ...
    @property
    def value(self) -> str: ...
