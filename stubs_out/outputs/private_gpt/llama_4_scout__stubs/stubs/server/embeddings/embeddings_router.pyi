from _typeshed import Incomplete
from fastapi import Depends as Depends, Request as Request
from pydantic import BaseModel
from typing import Any

embeddings_router: Incomplete

class EmbeddingsBody(BaseModel):
    input: str | list[str]

class EmbeddingsResponse(BaseModel):
    object: Literal['list']
    model: Literal['private-gpt']
    data: list[Any]

def embeddings_generation(request: Request, body: EmbeddingsBody) -> EmbeddingsResponse: ...
