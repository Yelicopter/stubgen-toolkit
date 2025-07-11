from typing import Any, Dict

from .base import BasePrompt

class CorrectOutputTypeErrorPrompt(BasePrompt):
    template_path: str
    def to_json(self) -> Dict[str, Any]: ...