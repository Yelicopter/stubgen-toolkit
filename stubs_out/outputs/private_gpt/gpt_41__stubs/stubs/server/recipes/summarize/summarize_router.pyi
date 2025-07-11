from fastapi import APIRouter as APIRouter, Depends as Depends, Request as Request
from private_gpt.open_ai.extensions.context_filter import ContextFilter as ContextFilter
from private_gpt.open_ai.openai_models import to_openai_sse_stream as to_openai_sse_stream
from private_gpt.server.recipes.summarize.summarize_service import SummarizeService as SummarizeService
from private_gpt.server.utils.auth import authenticated as authenticated
from pydantic import BaseModel
from starlette.responses import StreamingResponse as StreamingResponse

summarize_router: APIRouter

class SummarizeBody(BaseModel):
    text: str | None
    use_context: bool
    context_filter: ContextFilter | None
    prompt: str | None
    instructions: str | None
    stream: bool

class SummarizeResponse(BaseModel):
    summary: str

def summarize(request: Request, body: SummarizeBody) -> SummarizeResponse | StreamingResponse: ...
