from .base import BasePrompt as BasePrompt
from typing import Any, Dict

class GeneratePythonCodeWithSQLPrompt(BasePrompt):
    template_path: str
    def to_json(self) -> Dict[str, Any]: ...
