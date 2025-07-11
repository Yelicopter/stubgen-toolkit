from typing import Any

from pandasai.agent.state import AgentState
from pandasai.core.prompts.base import BasePrompt

class CodeGenerator:
    _context: AgentState
    _code_cleaner: Any
    _code_validator: Any
    def __init__(self, context: AgentState) -> None: ...
    def generate_code(self, prompt: BasePrompt) -> str: ...
    def validate_and_clean_code(self, code: str) -> str: ...