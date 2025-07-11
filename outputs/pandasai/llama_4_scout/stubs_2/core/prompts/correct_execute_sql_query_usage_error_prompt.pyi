from pandasai.core.prompts.base import BasePrompt


class CorrectExecuteSQLQueryUsageErrorPrompt(BasePrompt):
    template_path = "correct_execute_sql_query_usage_error_prompt.tmpl"

    def to_json(self) -> dict:
        ...