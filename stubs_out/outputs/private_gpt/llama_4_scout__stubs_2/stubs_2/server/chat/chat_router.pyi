from _typeshed import Incomplete
from fastapi import Depends as Depends, Request as Request
from private_gpt.open_ai.extensions.context_filter import ContextFilter as ContextFilter
from private_gpt.open_ai.openai_models import OpenAICompletion
from pydantic import BaseModel
from starlette.responses import StreamingResponse as StreamingResponse
from typing import Any

chat_router: Incomplete

class ChatBody(BaseModel):
    messages: list[Any]
    use_context: bool
    context_filter: ContextFilter | None
    include_sources: bool
    stream: bool

def chat_completion(request: Request, body: ChatBody) -> StreamingResponse | OpenAICompletion: ...
