from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

from pandasai.helpers.session import Session
from pandasai.llm.base import LLM

if TYPE_CHECKING:
    from pandasai.core.prompts.base import BasePrompt

class BambooLLM(LLM):
    _session: Session
    def __init__(
        self, endpoint_url: Optional[str] = ..., api_key: Optional[str] = ...
    ) -> None: ...
    def call(self, instruction: BasePrompt, _context: Any = ...) -> str: ...
    @property
    def type(self) -> str: ...