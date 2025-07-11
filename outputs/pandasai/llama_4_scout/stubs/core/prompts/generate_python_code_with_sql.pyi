from .base import BasePrompt


class GeneratePythonCodeWithSQLPrompt(BasePrompt):
    template_path = "generate_python_code_with_sql.tmpl"

    def to_json(self) -> dict:
        ...