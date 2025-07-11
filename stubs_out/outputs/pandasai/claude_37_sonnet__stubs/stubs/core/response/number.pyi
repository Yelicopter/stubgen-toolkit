from .base import BaseResponse as BaseResponse
from typing import Union

class NumberResponse(BaseResponse):
    def __init__(self, value: Union[int, float] = ..., last_code_executed: str = ...) -> None: ...
