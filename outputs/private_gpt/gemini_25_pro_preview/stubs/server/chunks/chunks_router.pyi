from typing import Literal

from fastapi import APIRouter, Request
from pydantic import BaseModel, Field

from private_gpt.open_ai.extensions.context_filter import ContextFilter
from private_gpt.server.chunks.chunks_service import Chunk

chunks_router: APIRouter

class ChunksBody(BaseModel):
    text: str = Field(examples=["Q3 2023 sales"])
    context_filter: ContextFilter | None
    limit: int = 10
    prev_next_chunks: int = Field(default=0, examples=[2])

class ChunksResponse(BaseModel):
    object: Literal["list"]
    model: Literal["private-gpt"]
    data: list[Chunk]

def chunks_retrieval(request: Request, body: ChunksBody) -> ChunksResponse: ...