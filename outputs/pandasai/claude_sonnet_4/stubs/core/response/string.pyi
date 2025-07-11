from typing import Any
from .base import BaseResponse

class StringResponse(BaseResponse):
    def __init__(self, value: Any = None, last_code_executed: Optional[str] = None): ...