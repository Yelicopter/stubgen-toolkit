from .base import BaseResponse as BaseResponse

class StringResponse(BaseResponse):
    def __init__(self, value: str = ..., last_code_executed: str = ...) -> None: ...
