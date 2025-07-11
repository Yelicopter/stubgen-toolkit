from typing import Literal, List
from injector import inject, singleton
from pydantic import BaseModel, Field
from private_gpt.components.embedding.embedding_component import EmbeddingComponent

class Embedding(BaseModel):
    index: int
    object: Literal["embedding"]
    embedding: List[float] = Field(examples=[[0.0023064255, -0.009327292]])

@singleton
class EmbeddingsService:
    @inject
    def __init__(self, embedding_component: EmbeddingComponent) -> None: ...
    
    def texts_embeddings(self, texts: List[str]) -> List[Embedding]: ...