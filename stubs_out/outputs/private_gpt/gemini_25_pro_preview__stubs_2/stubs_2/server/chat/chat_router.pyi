from fastapi import APIRouter as APIRouter, Request as Request
from private_gpt.open_ai.extensions.context_filter import ContextFilter as ContextFilter
from private_gpt.open_ai.openai_models import OpenAICompletion as OpenAICompletion, OpenAIMessage as OpenAIMessage
from pydantic import BaseModel, ConfigDict as ConfigDict
from starlette.responses import StreamingResponse as StreamingResponse
from typing import ClassVar

chat_router: APIRouter

class ChatBody(BaseModel):
    messages: list[OpenAIMessage]
    use_context: bool
    context_filter: ContextFilter | None
    include_sources: bool
    stream: bool
    model_config: ClassVar[ConfigDict]

def chat_completion(request: Request, body: ChatBody) -> OpenAICompletion | StreamingResponse: ...
