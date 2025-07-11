from fastapi import APIRouter, Depends, Request
from llama_index.core.llms import ChatMessage, MessageRole
from pydantic import BaseModel
from starlette.responses import StreamingResponse
from typing import Optional, List, Union
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
    messages: List[OpenAIMessage]
    use_context: bool = False
    context_filter: Optional[ContextFilter] = None
    include_sources: bool = True
    stream: bool = False

def chat_completion(
    request: Request, body: ChatBody
) -> Union[OpenAICompletion, StreamingResponse]: ...