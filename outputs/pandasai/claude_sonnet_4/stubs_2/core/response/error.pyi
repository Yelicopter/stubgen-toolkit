from typing import Optional
from .base import BaseResponse

class ErrorResponse(BaseResponse):
    def __init__(
        self,
        value: str = "Unfortunately, I was not able to get your answer. Please try again.",
        last_code_executed: Optional[str] = None,
        error: Optional[str] = None,
    ): ...