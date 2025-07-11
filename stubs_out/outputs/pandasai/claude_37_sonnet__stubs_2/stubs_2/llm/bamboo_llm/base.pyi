from _typeshed import Incomplete
from pandasai.core.prompts.base import BasePrompt as BasePrompt
from pandasai.helpers.session import Session as Session
from pandasai.llm.base import LLM
from typing import Optional

class BambooLLM(LLM):
    def __init__(self, endpoint_url: Optional[str] = ..., api_key: Optional[str] = ...) -> None: ...
    def call(self, instruction: BasePrompt, _context: Incomplete | None = ...) -> str: ...
    @property
    def type(self) -> str: ...
