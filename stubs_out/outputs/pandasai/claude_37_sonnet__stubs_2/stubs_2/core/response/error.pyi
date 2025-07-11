from .base import BaseResponse as BaseResponse
from typing import Optional

class ErrorResponse(BaseResponse):
    def __init__(self, value: str = ..., last_code_executed: Optional[str] = ..., error: Optional[str] = ...) -> None: ...
