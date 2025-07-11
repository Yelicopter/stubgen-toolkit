from typing import Any, Optional, Union

from .base import BaseResponse

class NumberResponse(BaseResponse):
    def __init__(self, value: Optional[Union[int, float]] = None, last_code_executed: Optional[str] = None) -> None: ...