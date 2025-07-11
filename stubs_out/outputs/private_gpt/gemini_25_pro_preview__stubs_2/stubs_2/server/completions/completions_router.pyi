from fastapi import APIRouter as APIRouter, Request as Request
from private_gpt.open_ai.extensions.context_filter import ContextFilter as ContextFilter
from private_gpt.open_ai.openai_models import OpenAICompletion as OpenAICompletion
from pydantic import BaseModel, ConfigDict as ConfigDict
from starlette.responses import StreamingResponse as StreamingResponse
from typing import ClassVar

completions_router: APIRouter

class CompletionsBody(BaseModel):
    prompt: str
    system_prompt: str | None
    use_context: bool
    context_filter: ContextFilter | None
    include_sources: bool
    stream: bool
    model_config: ClassVar[ConfigDict]

def prompt_completion(request: Request, body: CompletionsBody) -> OpenAICompletion | StreamingResponse: ...
