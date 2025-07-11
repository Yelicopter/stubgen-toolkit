from fastapi import APIRouter, Depends, Request
from pydantic import BaseModel
from starlette.responses import StreamingResponse
from typing import Any

from private_gpt.open_ai.extensions.context_filter import ContextFilter
from private_gpt.open_ai.openai_models import (
    OpenAICompletion,
    OpenAIMessage,
)
from private_gpt.server.chat.chat_router import ChatBody, chat_completion
from private_gpt.server.utils.auth import authenticated

completions_router: APIRouter

class CompletionsBody(BaseModel):
    prompt: str
    system_prompt: str | None
    use_context: bool
    context_filter: ContextFilter | None
    include_sources: bool
    stream: bool

    model_config: dict[str, Any]

def prompt_completion(
    request: Request, body: CompletionsBody
) -> OpenAICompletion | StreamingResponse: ...
