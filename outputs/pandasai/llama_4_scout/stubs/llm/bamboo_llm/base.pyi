from __future__ import annotations

from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from pandasai.core.prompts.base import BasePrompt

from pandasai.helpers.session import Session
from pandasai.llm.base import LLM


class BambooLLM(LLM):
    _session: Session

    def __init__(
        self, endpoint_url: str | None = None, api_key: str | None = None
    ) -> None:
        ...

    def call(self, instruction: "BasePrompt", _context: None = None) -> str:
        ...


    @property
    def type(self) -> str:
        ...