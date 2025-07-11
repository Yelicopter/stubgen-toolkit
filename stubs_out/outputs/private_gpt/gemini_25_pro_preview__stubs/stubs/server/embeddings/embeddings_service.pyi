from private_gpt.components.embedding.embedding_component import EmbeddingComponent as EmbeddingComponent
from pydantic import BaseModel
from typing import Literal

class Embedding(BaseModel):
    index: int
    object: Literal['embedding']
    embedding: list[float]

class EmbeddingsService:
    def __init__(self, embedding_component: EmbeddingComponent) -> None: ...
    def texts_embeddings(self, texts: list[str]) -> list[Embedding]: ...
