from typing import Any, Dict

from .base import BasePrompt

class GeneratePythonCodeWithSQLPrompt(BasePrompt):
    template_path: str = "generate_python_code_with_sql.tmpl"
    
    def to_json(self) -> Dict[str, Any]: ...