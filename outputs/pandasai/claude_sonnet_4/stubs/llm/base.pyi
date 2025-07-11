from __future__ import annotations
import ast
import re
from abc import abstractmethod
from typing import TYPE_CHECKING, Any, Optional
from pandasai.core.prompts.base import BasePrompt
from pandasai.core.prompts.generate_system_message import GenerateSystemMessagePrompt
from pandasai.helpers.memory import Memory
from ..exceptions import (
    APIKeyNotFoundError,
    MethodNotImplementedError,
    NoCodeFoundError,
)

if TYPE_CHECKING:
    from pandasai.agent.state import AgentState

class LLM:
    last_prompt: Optional[str] = None
    
    def __init__(self, api_key: Optional[str] = None, **kwargs: Any) -> None: ...
    def is_pandasai_llm(self) -> bool: ...
    
    @property
    def type(self) -> str: ...
    
    def _polish_code(self, code: str) -> str: ...
    def _is_python_code(self, string: str) -> bool: ...
    def _extract_code(self, response: str, separator: str = "") -> str: ...
    def prepend_system_prompt(self, prompt: BasePrompt, memory: Memory) -> str: ...
    def get_system_prompt(self, memory: Memory) -> str: ...
    def get_messages(self, memory: Memory) -> str: ...
    
    @abstractmethod
    def call(self, instruction: BasePrompt, context: Optional[AgentState] = None) -> str: ...
    
    def generate_code(self, instruction: BasePrompt, context: AgentState) -> str: ...