from typing import Literal

from fastapi import APIRouter, Depends, Request
from pydantic import BaseModel

from private_gpt.server.embeddings.embeddings_service import (
    Embedding,
    EmbeddingsService,
)
from private_gpt.server.utils.auth import authenticated

embeddings_router: APIRouter

class EmbeddingsBody(BaseModel):
    input: str | list[str]

class EmbeddingsResponse(BaseModel):
    object: Literal["list"]
    model: Literal["private-gpt"]
    data: list[Embedding]

def embeddings_generation(request: Request, body: EmbeddingsBody) -> EmbeddingsResponse: ...