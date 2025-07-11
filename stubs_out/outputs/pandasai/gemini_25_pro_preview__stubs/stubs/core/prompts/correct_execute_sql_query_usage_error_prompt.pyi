from pandasai.core.prompts.base import BasePrompt
from typing import Any, Dict

class CorrectExecuteSQLQueryUsageErrorPrompt(BasePrompt):
    template_path: str
    def to_json(self) -> Dict[str, Any]: ...
