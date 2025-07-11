from pandasai.helpers.json_encoder import CustomJsonEncoder as CustomJsonEncoder
from typing import Any, Dict, Optional

class BaseResponse:
    value: Any
    type: str
    last_code_executed: Optional[str]
    error: Optional[str]
    def __init__(self, value: Any = ..., type: Optional[str] = ..., last_code_executed: Optional[str] = ..., error: Optional[str] = ...) -> None: ...
    def to_dict(self) -> Dict[str, Any]: ...
    def to_json(self) -> str: ...
