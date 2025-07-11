from .base import BaseResponse as BaseResponse
from typing import Any, Optional

class StringResponse(BaseResponse):
    def __init__(self, value: Any = ..., last_code_executed: Optional[str] = ...) -> None: ...
