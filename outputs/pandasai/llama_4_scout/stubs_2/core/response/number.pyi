from typing import Any

from .base import BaseResponse

class NumberResponse(BaseResponse):
    def __init__(self, value: Any = None, last_code_executed: str = None) -> None:
        ...