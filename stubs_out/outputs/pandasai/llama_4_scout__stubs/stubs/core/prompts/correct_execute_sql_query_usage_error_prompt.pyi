from pandasai.core.prompts.base import BasePrompt

class CorrectExecuteSQLQueryUsageErrorPrompt(BasePrompt):
    template_path: str
    def to_json(self) -> dict: ...
