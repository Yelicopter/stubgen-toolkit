from .base import BasePrompt

class CorrectOutputTypeErrorPrompt(BasePrompt):
    template_path: str
    
    def to_json(self) -> dict: ...