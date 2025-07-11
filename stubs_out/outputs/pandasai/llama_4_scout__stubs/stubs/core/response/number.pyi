from .base import BaseResponse as BaseResponse
from typing import Any

class NumberResponse(BaseResponse):
    def __init__(self, value: Any = ..., last_code_executed: str = ...) -> None: ...
