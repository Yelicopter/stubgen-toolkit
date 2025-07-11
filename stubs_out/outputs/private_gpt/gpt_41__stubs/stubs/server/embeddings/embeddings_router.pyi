from fastapi import APIRouter as APIRouter, Depends as Depends, Request as Request
from private_gpt.server.embeddings.embeddings_service import Embedding as Embedding, EmbeddingsService as EmbeddingsService
from private_gpt.server.utils.auth import authenticated as authenticated
from pydantic import BaseModel
from typing import Literal

embeddings_router: APIRouter

class EmbeddingsBody(BaseModel):
    input: str | list[str]

class EmbeddingsResponse(BaseModel):
    object: Literal['list']
    model: Literal['private-gpt']
    data: list[Embedding]

def embeddings_generation(request: Request, body: EmbeddingsBody) -> EmbeddingsResponse: ...
