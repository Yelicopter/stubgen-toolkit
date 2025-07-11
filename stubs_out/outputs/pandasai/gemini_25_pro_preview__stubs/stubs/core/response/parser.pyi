from .base import BaseResponse as BaseResponse
from typing import Any, Dict, Optional

class ResponseParser:
    def parse(self, result: Dict[str, Any], last_code_executed: Optional[str] = ...) -> BaseResponse: ...
