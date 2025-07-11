from .base import LLM as LLM
from pandasai.agent.state import AgentState as AgentState
from pandasai.core.prompts.base import BasePrompt as BasePrompt
from typing import Optional

class FakeLLM(LLM):
    def __init__(self, output: Optional[str] = ..., type: str = ...) -> None: ...
    def call(self, instruction: BasePrompt, context: Optional[AgentState] = ...) -> str: ...
    @property
    def type(self) -> str: ...
