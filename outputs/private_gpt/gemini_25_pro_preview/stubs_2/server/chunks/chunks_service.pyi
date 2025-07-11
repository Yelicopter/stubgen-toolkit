from __future__ import annotations

from typing import TYPE_CHECKING, Literal

from llama_index.core.schema import NodeWithScore
from pydantic import BaseModel, Field

from private_gpt.components.embedding.embedding_component import EmbeddingComponent
from private_gpt.components.llm.llm_component import LLMComponent
from private_gpt.components.node_store.node_store_component import NodeStoreComponent
from private_gpt.components.vector_store.vector_store_component import (
    VectorStoreComponent,
)
from private_gpt.open_ai.extensions.context_filter import ContextFilter
from private_gpt.server.ingest.model import IngestedDoc

if TYPE_CHECKING:
    from llama_index.core.schema import RelatedNodeInfo

class Chunk(BaseModel):
    object: Literal["context.chunk"]
    score: float = Field(examples=[0.023])
    document: IngestedDoc
    text: str = Field(examples=["Outbound sales increased 20%, driven by new leads."])
    previous_texts: list[str] | None = Field(
        default=None,
        examples=[["SALES REPORT 2023", "Inbound didn't show major changes."]],
    )
    next_texts: list[str] | None = Field(
        default=None,
        examples=[
            [
                "New leads came from Google Ads campaign.",
                "The campaign was run by the Marketing Department",
            ]
        ],
    )
    @classmethod
    def from_node(cls, node: NodeWithScore) -> Chunk: ...

class ChunksService:
    def __init__(
        self,
        llm_component: LLMComponent,
        vector_store_component: VectorStoreComponent,
        embedding_component: EmbeddingComponent,
        node_store_component: NodeStoreComponent,
    ) -> None: ...
    def _get_sibling_nodes_text(
        self, node_with_score: NodeWithScore, related_number: int, forward: bool = ...
    ) -> list[str]: ...
    def retrieve_relevant(
        self,
        text: str,
        context_filter: ContextFilter | None = ...,
        limit: int = ...,
        prev_next_chunks: int = ...,
    ) -> list[Chunk]: ...