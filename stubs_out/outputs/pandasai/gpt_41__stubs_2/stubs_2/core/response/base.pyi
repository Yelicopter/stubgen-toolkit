from typing import Any

class BaseResponse:
    value: Any
    type: str
    last_code_executed: Any
    error: Any
    def __init__(self, value: Any = ..., type: Any = ..., last_code_executed: Any = ..., error: Any = ...) -> None: ...
    def to_dict(self) -> dict: ...
    def to_json(self) -> str: ...
