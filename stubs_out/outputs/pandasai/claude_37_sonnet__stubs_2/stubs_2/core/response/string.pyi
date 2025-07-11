from .base import BaseResponse as BaseResponse
from typing import Optional

class StringResponse(BaseResponse):
    def __init__(self, value: Optional[str] = ..., last_code_executed: Optional[str] = ...) -> None: ...
