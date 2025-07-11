from fastapi import APIRouter as APIRouter, Request as Request
from private_gpt.open_ai.extensions.context_filter import ContextFilter as ContextFilter
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
