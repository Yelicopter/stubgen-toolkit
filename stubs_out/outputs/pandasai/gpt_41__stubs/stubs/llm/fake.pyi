from .base import LLM as LLM
from typing import Any, Optional

class FakeLLM(LLM):
    called: bool
    last_prompt: Optional[str]
    def __init__(self, output: Optional[str] = ..., type: str = ...) -> None: ...
    def call(self, instruction: Any, context: Any = ...) -> str: ...
    @property
    def type(self) -> str: ...
