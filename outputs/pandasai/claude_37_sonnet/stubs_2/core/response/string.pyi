from typing import Any, Optional

from .base import BaseResponse

class StringResponse(BaseResponse):
    def __init__(self, value: Optional[str] = None, last_code_executed: Optional[str] = None) -> None: ...