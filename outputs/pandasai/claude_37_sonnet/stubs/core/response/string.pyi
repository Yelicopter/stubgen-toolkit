from typing import Any, Optional

from .base import BaseResponse

class StringResponse(BaseResponse):
    def __init__(self, value: str = None, last_code_executed: str = None) -> None: ...