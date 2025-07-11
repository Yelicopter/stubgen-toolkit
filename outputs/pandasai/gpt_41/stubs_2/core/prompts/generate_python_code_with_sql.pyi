from .base import BasePrompt

class GeneratePythonCodeWithSQLPrompt(BasePrompt):
    template_path: str
    def to_json(self) -> dict: ...