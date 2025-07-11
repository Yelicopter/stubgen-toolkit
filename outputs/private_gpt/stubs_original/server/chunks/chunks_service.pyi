from _typeshed import Incomplete
from llama_index.core.schema import NodeWithScore as NodeWithScore, RelatedNodeInfo as RelatedNodeInfo
from private_gpt.components.embedding.embedding_component import EmbeddingComponent as EmbeddingComponent
from private_gpt.components.llm.llm_component import LLMComponent as LLMComponent
from private_gpt.components.node_store.node_store_component import NodeStoreComponent as NodeStoreComponent
from private_gpt.components.vector_store.vector_store_component import VectorStoreComponent as VectorStoreComponent
from private_gpt.open_ai.extensions.context_filter import ContextFilter as ContextFilter
from private_gpt.server.ingest.model import IngestedDoc as IngestedDoc
from pydantic import BaseModel
from typing import Literal

class Chunk(BaseModel):
    object: Literal['context.chunk']
    score: float
    document: IngestedDoc
    text: str
    previous_texts: list[str] | None
    next_texts: list[str] | None
    @classmethod
    def from_node(cls, node: NodeWithScore) -> Chunk: ...

class ChunksService:
    vector_store_component: Incomplete
    llm_component: Incomplete
    embedding_component: Incomplete
    storage_context: Incomplete
    def __init__(self, llm_component: LLMComponent, vector_store_component: VectorStoreComponent, embedding_component: EmbeddingComponent, node_store_component: NodeStoreComponent) -> None: ...
    def retrieve_relevant(self, text: str, context_filter: ContextFilter | None = ..., limit: int = ..., prev_next_chunks: int = ...) -> list[Chunk]: ...
