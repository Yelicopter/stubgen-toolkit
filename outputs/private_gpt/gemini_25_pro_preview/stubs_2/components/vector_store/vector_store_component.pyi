from llama_index.core.indices.vector_store import VectorIndexRetriever, VectorStoreIndex
from llama_index.core.vector_stores.types import (
    BasePydanticVectorStore,
    MetadataFilters,
)

from private_gpt.open_ai.extensions.context_filter import ContextFilter
from private_gpt.settings.settings import Settings

def _doc_id_metadata_filter(
    context_filter: ContextFilter | None,
) -> MetadataFilters: ...

class VectorStoreComponent:
    settings: Settings
    vector_store: BasePydanticVectorStore
    def __init__(self, settings: Settings) -> None: ...
    def get_retriever(
        self,
        index: VectorStoreIndex,
        context_filter: ContextFilter | None = ...,
        similarity_top_k: int = ...,
    ) -> VectorIndexRetriever: ...
    def close(self) -> None: ...