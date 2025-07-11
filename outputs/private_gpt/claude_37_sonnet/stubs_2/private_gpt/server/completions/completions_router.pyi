from fastapi import APIRouter, Depends, Request
from pydantic import BaseModel, ConfigDict
from starlette.responses import StreamingResponse
from typing import Optional, Union, Dict, Any

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
    system_prompt: Optional[str] = None
    use_context: bool = False
    context_filter: Optional[ContextFilter] = None
    include_sources: bool = True
    stream: bool = False

    model_config: ConfigDict = ConfigDict()

def prompt_completion(
    request: Request, body: CompletionsBody
) -> Union[OpenAICompletion, StreamingResponse]: ...