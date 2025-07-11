from fastapi import APIRouter as APIRouter, Depends as Depends, Request as Request
from private_gpt.open_ai.extensions.context_filter import ContextFilter as ContextFilter
from private_gpt.server.chunks.chunks_service import Chunk as Chunk, ChunksService as ChunksService
from private_gpt.server.utils.auth import authenticated as authenticated
from pydantic import BaseModel, Field as Field
from typing import Literal

chunks_router: APIRouter

class ChunksBody(BaseModel):
    text: str
    context_filter: ContextFilter | None
    limit: int
    prev_next_chunks: int

class ChunksResponse(BaseModel):
    object: Literal['list']
    model: Literal['private-gpt']
    data: list[Chunk]

def chunks_retrieval(request: Request, body: ChunksBody) -> ChunksResponse: ...
