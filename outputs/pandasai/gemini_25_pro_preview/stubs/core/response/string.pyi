from typing import Optional

from .base import BaseResponse

class StringResponse(BaseResponse):
    def __init__(self, value: Optional[str] = ..., last_code_executed: Optional[str] = ...) -> None: ...