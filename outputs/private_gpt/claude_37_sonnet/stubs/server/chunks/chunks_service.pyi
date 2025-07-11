from typing import TYPE_CHECKING, List, Literal, Optional

from injector import inject, singleton
from llama_index.core.indices import VectorStoreIndex
from llama_index.core.schema import NodeWithScore
from llama_index.core.storage import StorageContext
from pydantic import BaseModel, Field

from private_gpt.components.embedding.embedding_component import EmbeddingComponent
from private_gpt.components.llm.llm_component import LLMComponent
from private_gpt.components.node_store.node_store_component import NodeStoreComponent
from private_gpt.components.vector_store.vector_store_component import (
    VectorStoreComponent,
)
from private_gpt.open_ai.extensions.context_filter import ContextFilter
from private_gpt.server.ingest.model import IngestedDoc

class Chunk(BaseModel):
    object: Literal["context.chunk"]
    score: float = Field(examples=[0.023])
    document: IngestedDoc
    text: str = Field(examples=["Outbound sales increased 20%, driven by new leads."])
    previous_texts: Optional[List[str]] = Field(
        default=None,
        examples=[["SALES REPORT 2023", "Inbound didn't show major changes."]],
    )
    next_texts: Optional[List[str]] = Field(
        default=None,
        examples=[
            [
                "New leads came from Google Ads campaign.",
                "The campaign was run by the Marketing Department",
            ]
        ],
    )

    @classmethod
    def from_node(cls, node: NodeWithScore) -> 'Chunk': ...

@singleton
class ChunksService:
    @inject
    def __init__(
        self,
        llm_component: LLMComponent,
        vector_store_component: VectorStoreComponent,
        embedding_component: EmbeddingComponent,
        node_store_component: NodeStoreComponent,
    ) -> None: ...
    
    def _get_sibling_nodes_text(
        self, node_with_score: NodeWithScore, related_number: int, forward: bool = True
    ) -> List[str]: ...
    
    def retrieve_relevant(
        self,
        text: str,
        context_filter: Optional[ContextFilter] = None,
        limit: int = 10,
        prev_next_chunks: int = 0,
    ) -> List[Chunk]: ...