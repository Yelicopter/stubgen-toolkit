from typing import Any

class BaseResponse:
    value: Any
    type: str
    last_code_executed: Any
    error: Any

    def __init__(
        self,
        value: Any = ...,
        type: Any = ...,
        last_code_executed: Any = ...,
        error: Any = ...,
    ) -> None: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def to_dict(self) -> dict: ...
    def to_json(self) -> str: ...