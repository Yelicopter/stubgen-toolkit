from typing import Literal

from pydantic import BaseModel, Field

from private_gpt.components.embedding.embedding_component import EmbeddingComponent

class Embedding(BaseModel):
    index: int
    object: Literal["embedding"]
    embedding: list[float] = Field(examples=[[0.0023064255, -0.009327292]])

class EmbeddingsService:
    def __init__(self, embedding_component: EmbeddingComponent) -> None: ...
    def texts_embeddings(self, texts: list[str]) -> list[Embedding]: ...