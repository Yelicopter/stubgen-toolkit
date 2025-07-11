from typing import Optional

from pandasai.agent.state import AgentState
from pandasai.core.prompts.base import BasePrompt

from .base import LLM

class FakeLLM(LLM):
    _output: str
    _type: str
    called: bool
    last_prompt: Optional[str]
    def __init__(self, output: Optional[str] = ..., type: str = ...) -> None: ...
    def call(self, instruction: BasePrompt, context: Optional[AgentState] = ...) -> str: ...
    @property
    def type(self) -> str: ...