from typing import Optional, Union

from .base import BaseResponse

class NumberResponse(BaseResponse):
    def __init__(
        self, value: Optional[Union[int, float]] = ..., last_code_executed: Optional[str] = ...
    ) -> None: ...