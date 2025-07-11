from .base import BaseResponse as BaseResponse

class ErrorResponse(BaseResponse):
    def __init__(self, value: str = ..., last_code_executed: str = ..., error: str = ...) -> None: ...
