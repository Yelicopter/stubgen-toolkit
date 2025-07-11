from typing import Any, Dict

from .base import BasePrompt

class CorrectOutputTypeErrorPrompt(BasePrompt):
    template_path: str = "correct_output_type_error_prompt.tmpl"
    
    def to_json(self) -> Dict[str, Any]: ...