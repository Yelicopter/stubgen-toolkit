import abc
from llama_index.core.indices import VectorStoreIndex
from llama_index.core.schema import BaseNode, Document, TransformComponent
from llama_index.core.storage import StorageContext
from typing import Any

class BaseIngestComponent(abc.ABC):
    def __init__(
        self,
        storage_context: StorageContext,
        embed_model: Any,
        transformations: list[TransformComponent],
    ) -> None:
        ...

    @abc.abstractmethod
    def ingest(self, file_name: str, file_data: Any) -> Any:
        ...

    @abc.abstractmethod
    def bulk_ingest(self, files: list[Any]) -> Any:
        ...

    @abc.abstractmethod
    def delete(self, doc_id: str) -> None:
        ...