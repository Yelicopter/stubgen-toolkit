from fastapi import APIRouter as APIRouter, Depends as Depends, Request as Request
from private_gpt.open_ai.extensions.context_filter import ContextFilter as ContextFilter
from private_gpt.open_ai.openai_models import OpenAICompletion as OpenAICompletion, OpenAIMessage as OpenAIMessage
from private_gpt.server.chat.chat_router import ChatBody as ChatBody, chat_completion as chat_completion
from private_gpt.server.utils.auth import authenticated as authenticated
from pydantic import BaseModel
from starlette.responses import StreamingResponse as StreamingResponse

completions_router: APIRouter

class CompletionsBody(BaseModel):
    prompt: str
    system_prompt: str | None
    use_context: bool
    context_filter: ContextFilter | None
    include_sources: bool
    stream: bool
    model_config: dict

def prompt_completion(request: Request, body: CompletionsBody) -> OpenAICompletion | StreamingResponse: ...
