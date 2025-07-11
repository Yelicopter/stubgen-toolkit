from fastapi import APIRouter, Request
from pydantic import BaseModel
from starlette.responses import StreamingResponse

from private_gpt.open_ai.extensions.context_filter import ContextFilter

summarize_router: APIRouter

class SummarizeBody(BaseModel):
    text: str | None
    use_context: bool = False
    context_filter: ContextFilter | None
    prompt: str | None
    instructions: str | None
    stream: bool = False

class SummarizeResponse(BaseModel):
    summary: str

def summarize(
    request: Request, body: SummarizeBody
) -> SummarizeResponse | StreamingResponse: ...