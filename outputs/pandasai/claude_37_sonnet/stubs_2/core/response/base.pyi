import json
from typing import Any, Dict, Optional

from pandasai.helpers.json_encoder import CustomJsonEncoder

class BaseResponse:
    value: Any
    type: str
    last_code_executed: Optional[str]
    error: Optional[str]
    
    def __init__(
        self,
        value: Any = None,
        type: Optional[str] = None,
        last_code_executed: Optional[str] = None,
        error: Optional[str] = None,
    ) -> None: ...
    
    def __str__(self) -> str: ...
    
    def __repr__(self) -> str: ...
    
    def to_dict(self) -> Dict[str, Any]: ...
    
    def to_json(self) -> str: ...