from .base import BaseResponse as BaseResponse
from typing import Any

class ChartResponse(BaseResponse):
    def __init__(self, value: Any, **kwargs: Any) -> None: ...
    @property
    def value(self) -> Any: ...
