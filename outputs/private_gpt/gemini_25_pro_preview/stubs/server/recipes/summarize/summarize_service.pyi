from llama_index.core.storage.docstore.types import RefDocInfo
from llama_index.core.types import TokenGen

from private_gpt.components.embedding.embedding_component import EmbeddingComponent
from private_gpt.components.llm.llm_component import LLMComponent
from private_gpt.components.node_store.node_store_component import NodeStoreComponent
from private_gpt.components.vector_store.vector_store_component import (
    VectorStoreComponent,
)
from private_gpt.open_ai.extensions.context_filter import ContextFilter
from private_gpt.settings.settings import Settings

DEFAULT_SUMMARIZE_PROMPT: str

class SummarizeService:
    def __init__(
        self,
        settings: Settings,
        llm_component: LLMComponent,
        node_store_component: NodeStoreComponent,
        vector_store_component: VectorStoreComponent,
        embedding_component: EmbeddingComponent,
    ) -> None: ...
    @staticmethod
    def _filter_ref_docs(
        ref_docs: dict[str, RefDocInfo], context_filter: ContextFilter | None
    ) -> list[RefDocInfo]: ...
    def _summarize(
        self,
        use_context: bool = ...,
        stream: bool = ...,
        text: str | None = ...,
        instructions: str | None = ...,
        context_filter: ContextFilter | None = ...,
        prompt: str | None = ...,
    ) -> str | TokenGen: ...
    def summarize(
        self,
        use_context: bool = ...,
        text: str | None = ...,
        instructions: str | None = ...,
        context_filter: ContextFilter | None = ...,
        prompt: str | None = ...,
    ) -> str: ...
    def stream_summarize(
        self,
        use_context: bool = ...,
        text: str | None = ...,
        instructions: str | None = ...,
        context_filter: ContextFilter | None = ...,
        prompt: str | None = ...,
    ) -> TokenGen: ...