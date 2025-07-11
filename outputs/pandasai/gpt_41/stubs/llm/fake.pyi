from typing import Optional, Any
from .base import LLM

class FakeLLM(LLM):
    _output: str
    _type: str
    called: bool
    last_prompt: Optional[str]

    def __init__(self, output: Optional[str] = ..., type: str = ...): ...
    def call(self, instruction: Any, context: Any = ...) -> str: ...
    @property
    def type(self) -> str: ...