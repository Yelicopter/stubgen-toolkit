from .base import BaseResponse

class ErrorResponse(BaseResponse):
    def __init__(
        self,
        value: str = ...,
        last_code_executed: Any = ...,
        error: Any = ...,
    ): ...