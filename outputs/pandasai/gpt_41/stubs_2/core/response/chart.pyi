from typing import Any
from .base import BaseResponse

class ChartResponse(BaseResponse):
    def __init__(self, value: Any, **kwargs: Any) -> None:
        ...
    @property
    def value(self) -> Any:
        ...
    def __str__(self) -> str:
        ...