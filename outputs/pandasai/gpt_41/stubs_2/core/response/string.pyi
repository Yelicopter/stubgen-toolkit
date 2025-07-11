from typing import Any
from .base import BaseResponse

class StringResponse(BaseResponse):
    def __init__(self, value: str, **kwargs: Any) -> None:
        ...
    @property
    def value(self) -> str:
        ...
    def __str__(self) -> str:
        ...