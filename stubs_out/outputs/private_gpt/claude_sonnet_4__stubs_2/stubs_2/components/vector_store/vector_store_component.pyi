import logging
from llama_index.core.indices.vector_store import VectorIndexRetriever as VectorIndexRetriever, VectorStoreIndex as VectorStoreIndex
from llama_index.core.vector_stores.types import BasePydanticVectorStore as BasePydanticVectorStore, FilterCondition as FilterCondition, MetadataFilter as MetadataFilter, MetadataFilters as MetadataFilters
from private_gpt.open_ai.extensions.context_filter import ContextFilter as ContextFilter
from private_gpt.paths import local_data_path as local_data_path
from private_gpt.settings.settings import Settings as Settings
from typing import Optional

logger: logging.Logger

class VectorStoreComponent:
    settings: Settings
    vector_store: BasePydanticVectorStore
    def __init__(self, settings: Settings) -> None: ...
    def get_retriever(self, index: VectorStoreIndex, context_filter: Optional[ContextFilter] = ..., similarity_top_k: int = ...) -> VectorIndexRetriever: ...
    def close(self) -> None: ...
