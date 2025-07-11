from itertools import chain

from injector import inject, singleton
from llama_index.core import (
    Document,
    StorageContext,
    SummaryIndex,
)
from llama_index.core.base.response.schema import Response, StreamingResponse
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.response_synthesizers import ResponseMode
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

@singleton
class SummarizeService:
    @inject
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
        use_context: bool = False,
        stream: bool = False,
        text: str | None = None,
        instructions: str | None = None,
        context_filter: ContextFilter | None = None,
        prompt: str | None = None,
    ) -> str | TokenGen: ...
    def summarize(
        self,
        use_context: bool = False,
        text: str | None = None,
        instructions: str | None = None,
        context_filter: ContextFilter | None = None,
        prompt: str | None = None,
    ) -> str: ...
    def stream_summarize(
        self,
        use_context: bool = False,
        text: str | None = None,
        instructions: str | None = None,
        context_filter: ContextFilter | None = None,
        prompt: str | None = None,
    ) -> TokenGen: ...