from .base import BasePrompt as BasePrompt

class GeneratePythonCodeWithSQLPrompt(BasePrompt):
    template_path: str
    def to_json(self): ...
