from .base import BaseResponse as BaseResponse
from typing import Any

class NumberResponse(BaseResponse):
    def __init__(self, value: float, **kwargs: Any) -> None: ...
    @property
    def value(self) -> float: ...
