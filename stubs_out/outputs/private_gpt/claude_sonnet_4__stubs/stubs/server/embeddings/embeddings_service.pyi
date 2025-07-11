from private_gpt.components.embedding.embedding_component import EmbeddingComponent as EmbeddingComponent
from pydantic import BaseModel
from typing import List, Literal

class Embedding(BaseModel):
    index: int
    object: Literal['embedding']
    embedding: List[float]

class EmbeddingsService:
    def __init__(self, embedding_component: EmbeddingComponent) -> None: ...
    def texts_embeddings(self, texts: List[str]) -> List[Embedding]: ...
