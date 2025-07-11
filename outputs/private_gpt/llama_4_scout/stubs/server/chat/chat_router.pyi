from fastapi import APIRouter, Depends, Request
from pydantic import BaseModel
from starlette.responses import StreamingResponse
from private_gpt.open_ai.extensions.context_filter import ContextFilter
from private_gpt.open_ai.openai_models import OpenAICompletion, to_openai_response, to_openai_sse_stream

chat_router = APIRouter()

class ChatBody(BaseModel):
    messages: list[Any]
    use_context: bool
    context_filter: ContextFilter | None
    include_sources: bool
    stream: bool

@chat_router.post("/chat/completions", response_model=None, responses={200: {"model": OpenAICompletion}})
def chat_completion(request: Request, body: ChatBody) -> StreamingResponse | OpenAICompletion:
    ...