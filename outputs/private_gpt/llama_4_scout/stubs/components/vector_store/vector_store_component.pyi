from injector import inject, singleton
from llama_index.core.vector_stores.types import BasePydanticVectorStore
from private_gpt.settings.settings import Settings

@singleton
class VectorStoreComponent:
    @inject
    def __init__(self, settings: Settings) -> None:
        ...

    def get_vector_store(self) -> BasePydanticVectorStore:
        ...

    def get_retriever(self, index: Any, context_filter: Any = None, similarity_top_k: int = 2) -> Any:
        ...