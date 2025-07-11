import logging
import typing
from typing import Optional
from injector import inject, singleton
from llama_index.core.indices.vector_store import VectorIndexRetriever, VectorStoreIndex
from llama_index.core.vector_stores.types import (
    BasePydanticVectorStore,
    FilterCondition,
    MetadataFilter,
    MetadataFilters,
)
from private_gpt.open_ai.extensions.context_filter import ContextFilter
from private_gpt.paths import local_data_path
from private_gpt.settings.settings import Settings

logger: logging.Logger

def _doc_id_metadata_filter(
    context_filter: Optional[ContextFilter],
) -> MetadataFilters: ...

@singleton
class VectorStoreComponent:
    settings: Settings
    vector_store: BasePydanticVectorStore
    
    @inject
    def __init__(self, settings: Settings) -> None: ...
    
    def get_retriever(
        self,
        index: VectorStoreIndex,
        context_filter: Optional[ContextFilter] = None,
        similarity_top_k: int = 2,
    ) -> VectorIndexRetriever: ...
    
    def close(self) -> None: ...