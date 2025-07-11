from .base import BasePrompt


class CorrectOutputTypeErrorPrompt(BasePrompt):
    template_path = "correct_output_type_error_prompt.tmpl"

    def to_json(self) -> dict:
        ...