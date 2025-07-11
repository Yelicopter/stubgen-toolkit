from fastapi import APIRouter, Depends, Request
from pydantic import BaseModel, Field
from private_gpt.open_ai.extensions.context_filter import ContextFilter
from typing import Any, Literal

chunks_router = APIRouter()

class ChunksBody(BaseModel):
    text: str
    context_filter: ContextFilter | None
    limit: int
    prev_next_chunks: int

class ChunksResponse(BaseModel):
    object: Literal["list"]
    model: Literal["private-gpt"]
    data: list[Any]

@chunks_router.post("/chunks", response_model=ChunksResponse)
def chunks_retrieval(request: Request, body: ChunksBody) -> ChunksResponse:
    ...