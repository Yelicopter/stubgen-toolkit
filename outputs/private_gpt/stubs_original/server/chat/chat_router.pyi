from _typeshed import Incomplete
from fastapi import Request as Request
from private_gpt.open_ai.extensions.context_filter import ContextFilter as ContextFilter
from private_gpt.open_ai.openai_models import OpenAICompletion as OpenAICompletion, OpenAIMessage as OpenAIMessage, to_openai_response as to_openai_response, to_openai_sse_stream as to_openai_sse_stream
from private_gpt.server.chat.chat_service import ChatService as ChatService
from private_gpt.server.utils.auth import authenticated as authenticated
from pydantic import BaseModel
from starlette.responses import StreamingResponse

chat_router: Incomplete

class ChatBody(BaseModel):
    messages: list[OpenAIMessage]
    use_context: bool
    context_filter: ContextFilter | None
    include_sources: bool
    stream: bool
    model_config: Incomplete

def chat_completion(request: Request, body: ChatBody) -> OpenAICompletion | StreamingResponse: ...
