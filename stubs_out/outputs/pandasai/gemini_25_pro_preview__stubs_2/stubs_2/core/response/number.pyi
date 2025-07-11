from .base import BaseResponse as BaseResponse
from typing import Optional, Union

class NumberResponse(BaseResponse):
    def __init__(self, value: Optional[Union[int, float]] = ..., last_code_executed: Optional[str] = ...) -> None: ...
