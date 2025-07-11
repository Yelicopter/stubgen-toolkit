from _typeshed import Incomplete
from fastapi import Depends as Depends, Request as Request
from private_gpt.open_ai.extensions.context_filter import ContextFilter as ContextFilter
from pydantic import BaseModel, Field as Field
from typing import Any

chunks_router: Incomplete

class ChunksBody(BaseModel):
    text: str
    context_filter: ContextFilter | None
    limit: int
    prev_next_chunks: int

class ChunksResponse(BaseModel):
    object: Literal['list']
    model: Literal['private-gpt']
    data: list[Any]

def chunks_retrieval(request: Request, body: ChunksBody) -> ChunksResponse: ...
