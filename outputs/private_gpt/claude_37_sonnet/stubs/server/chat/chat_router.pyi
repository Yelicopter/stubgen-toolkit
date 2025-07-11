from fastapi import APIRouter, Depends, Request
from llama_index.core.llms import ChatMessage, MessageRole
from pydantic import BaseModel, Field
from starlette.responses import StreamingResponse
from typing import List, Optional

from private_gpt.open_ai.extensions.context_filter import ContextFilter
from private_gpt.open_ai.openai_models import (
    OpenAICompletion,
    OpenAIMessage,
    to_openai_response,
    to_openai_sse_stream,
)
from private_gpt.server.chat.chat_service import ChatService
from private_gpt.server.utils.auth import authenticated

chat_router: APIRouter

class ChatBody(BaseModel):
    messages: list[OpenAIMessage]
    use_context: bool = False
    context_filter: Optional[ContextFilter] = None
    include_sources: bool = True
    stream: bool = False

    model_config: dict

def chat_completion(
    request: Request, body: ChatBody
) -> OpenAICompletion | StreamingResponse: ...