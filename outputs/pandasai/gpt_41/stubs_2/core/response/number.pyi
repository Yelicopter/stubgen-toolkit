from typing import Any
from .base import BaseResponse

class NumberResponse(BaseResponse):
    def __init__(self, value: float, **kwargs: Any) -> None:
        ...
    @property
    def value(self) -> float:
        ...
    def __str__(self) -> str:
        ...