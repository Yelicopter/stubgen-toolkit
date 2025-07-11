from fastapi import APIRouter, Depends, Request
from pydantic import BaseModel
from typing import Any, Literal

embeddings_router = APIRouter()

class EmbeddingsBody(BaseModel):
    input: str | list[str]

class EmbeddingsResponse(BaseModel):
    object: Literal["list"]
    model: Literal["private-gpt"]
    data: list[Any]

@embeddings_router.post("/embeddings", response_model=EmbeddingsResponse)
def embeddings_generation(request: Request, body: EmbeddingsBody) -> EmbeddingsResponse:
    ...