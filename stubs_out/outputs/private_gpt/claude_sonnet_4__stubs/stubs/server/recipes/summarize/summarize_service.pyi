from itertools import chain as chain
from llama_index.core import Document as Document, StorageContext as StorageContext, SummaryIndex as SummaryIndex
from llama_index.core.base.response.schema import Response as Response, StreamingResponse as StreamingResponse
from llama_index.core.node_parser import SentenceSplitter as SentenceSplitter
from llama_index.core.response_synthesizers import ResponseMode as ResponseMode
from llama_index.core.storage.docstore.types import RefDocInfo as RefDocInfo
from llama_index.core.types import TokenGen as TokenGen
from private_gpt.components.embedding.embedding_component import EmbeddingComponent as EmbeddingComponent
from private_gpt.components.llm.llm_component import LLMComponent as LLMComponent
from private_gpt.components.node_store.node_store_component import NodeStoreComponent as NodeStoreComponent
from private_gpt.components.vector_store.vector_store_component import VectorStoreComponent as VectorStoreComponent
from private_gpt.open_ai.extensions.context_filter import ContextFilter as ContextFilter
from private_gpt.settings.settings import Settings as Settings
from typing import Optional

DEFAULT_SUMMARIZE_PROMPT: str

class SummarizeService:
    def __init__(self, settings: Settings, llm_component: LLMComponent, node_store_component: NodeStoreComponent, vector_store_component: VectorStoreComponent, embedding_component: EmbeddingComponent) -> None: ...
    def summarize(self, use_context: bool = ..., text: Optional[str] = ..., instructions: Optional[str] = ..., context_filter: Optional[ContextFilter] = ..., prompt: Optional[str] = ...) -> str: ...
    def stream_summarize(self, use_context: bool = ..., text: Optional[str] = ..., instructions: Optional[str] = ..., context_filter: Optional[ContextFilter] = ..., prompt: Optional[str] = ...) -> TokenGen: ...
