from typing import Any, ClassVar

from fastapi import APIRouter, Request
from pydantic import BaseModel, ConfigDict
from starlette.responses import StreamingResponse

from private_gpt.open_ai.extensions.context_filter import ContextFilter
from private_gpt.open_ai.openai_models import OpenAICompletion

completions_router: APIRouter

class CompletionsBody(BaseModel):
    prompt: str
    system_prompt: str | None
    use_context: bool = False
    context_filter: ContextFilter | None
    include_sources: bool = True
    stream: bool = False
    model_config: ClassVar[ConfigDict] = ...

def prompt_completion(
    request: Request, body: CompletionsBody
) -> OpenAICompletion | StreamingResponse: ...