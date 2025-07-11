from fastapi import APIRouter, Depends, Request
from pydantic import BaseModel
from starlette.responses import StreamingResponse
from private_gpt.open_ai.extensions.context_filter import ContextFilter
from private_gpt.open_ai.openai_models import OpenAICompletion

completions_router = APIRouter()

class CompletionsBody(BaseModel):
    prompt: str
    system_prompt: str | None
    use_context: bool
    context_filter: ContextFilter | None
    include_sources: bool
    stream: bool

@completions_router.post("/completions", response_model=OpenAICompletion)
def prompt_completion(request: Request, body: CompletionsBody) -> StreamingResponse | OpenAICompletion:
    ...