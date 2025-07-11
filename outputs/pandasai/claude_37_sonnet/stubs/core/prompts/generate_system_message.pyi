from .base import BasePrompt

class GenerateSystemMessagePrompt(BasePrompt):
    template_path: str = "generate_system_message.tmpl"