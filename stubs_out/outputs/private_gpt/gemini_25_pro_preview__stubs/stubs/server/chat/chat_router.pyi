from fastapi import APIRouter as APIRouter, Request as Request
from private_gpt.open_ai.extensions.context_filter import ContextFilter as ContextFilter
from private_gpt.open_ai.openai_models import OpenAICompletion as OpenAICompletion, OpenAIMessage as OpenAIMessage
from pydantic import BaseModel
from starlette.responses import StreamingResponse as StreamingResponse

chat_router: APIRouter

class ChatBody(BaseModel):
    messages: list[OpenAIMessage]
    use_context: bool
    context_filter: ContextFilter | None
    include_sources: bool
    stream: bool
    model_config: dict

def chat_completion(request: Request, body: ChatBody) -> OpenAICompletion | StreamingResponse: ...
