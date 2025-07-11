from typing import Literal, List, Union
from fastapi import APIRouter, Depends, Request
from pydantic import BaseModel
from private_gpt.server.embeddings.embeddings_service import (
    Embedding,
    EmbeddingsService,
)
from private_gpt.server.utils.auth import authenticated

embeddings_router: APIRouter

class EmbeddingsBody(BaseModel):
    input: Union[str, List[str]]

class EmbeddingsResponse(BaseModel):
    object: Literal["list"]
    model: Literal["private-gpt"]
    data: List[Embedding]

def embeddings_generation(request: Request, body: EmbeddingsBody) -> EmbeddingsResponse: ...