from _typeshed import Incomplete
from pandasai.helpers.json_encoder import CustomJsonEncoder as CustomJsonEncoder
from typing import Any

class BaseResponse:
    value: Incomplete
    type: Incomplete
    last_code_executed: Incomplete
    error: Incomplete
    def __init__(self, value: Any = ..., type: str = ..., last_code_executed: str = ..., error: str = ...) -> None: ...
    def to_dict(self) -> dict: ...
    def to_json(self) -> str: ...
