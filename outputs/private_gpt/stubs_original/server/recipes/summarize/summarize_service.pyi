from _typeshed import Incomplete
from llama_index.core.storage.docstore.types import RefDocInfo as RefDocInfo
from llama_index.core.types import TokenGen as TokenGen
from private_gpt.components.embedding.embedding_component import EmbeddingComponent as EmbeddingComponent
from private_gpt.components.llm.llm_component import LLMComponent as LLMComponent
from private_gpt.components.node_store.node_store_component import NodeStoreComponent as NodeStoreComponent
from private_gpt.components.vector_store.vector_store_component import VectorStoreComponent as VectorStoreComponent
from private_gpt.open_ai.extensions.context_filter import ContextFilter as ContextFilter
from private_gpt.settings.settings import Settings as Settings

DEFAULT_SUMMARIZE_PROMPT: str

class SummarizeService:
    settings: Incomplete
    llm_component: Incomplete
    node_store_component: Incomplete
    vector_store_component: Incomplete
    embedding_component: Incomplete
    storage_context: Incomplete
    def __init__(self, settings: Settings, llm_component: LLMComponent, node_store_component: NodeStoreComponent, vector_store_component: VectorStoreComponent, embedding_component: EmbeddingComponent) -> None: ...
    def summarize(self, use_context: bool = ..., text: str | None = ..., instructions: str | None = ..., context_filter: ContextFilter | None = ..., prompt: str | None = ...) -> str: ...
    def stream_summarize(self, use_context: bool = ..., text: str | None = ..., instructions: str | None = ..., context_filter: ContextFilter | None = ..., prompt: str | None = ...) -> TokenGen: ...
