from .base import BaseResponse as BaseResponse
from typing import Any

class ErrorResponse(BaseResponse):
    def __init__(self, value: str = ..., last_code_executed: Any = ..., error: Any = ...) -> None: ...
