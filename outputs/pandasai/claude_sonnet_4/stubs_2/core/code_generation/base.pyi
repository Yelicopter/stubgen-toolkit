import traceback
from pandasai.agent.state import AgentState
from pandasai.core.prompts.base import BasePrompt
from .code_cleaning import CodeCleaner
from .code_validation import CodeRequirementValidator

class CodeGenerator:
    def __init__(self, context: AgentState): ...
    def generate_code(self, prompt: BasePrompt) -> str: ...
    def validate_and_clean_code(self, code: str) -> str: ...