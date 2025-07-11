import abc
import multiprocessing.pool
from pathlib import Path
from queue import Queue
from typing import Any, Literal

from llama_index.core.embeddings.utils import EmbedType
from llama_index.core.indices.base import BaseIndex
from llama_index.core.schema import BaseNode, Document, TransformComponent
from llama_index.core.storage import StorageContext

from private_gpt.settings.settings import Settings

class BaseIngestComponent(abc.ABC):
    storage_context: StorageContext
    embed_model: EmbedType
    transformations: list[TransformComponent]
    def __init__(
        self,
        storage_context: StorageContext,
        embed_model: EmbedType,
        transformations: list[TransformComponent],
        *args: Any,
        **kwargs: Any,
    ) -> None: ...
    @abc.abstractmethod
    def ingest(self, file_name: str, file_data: Path) -> list[Document]: ...
    @abc.abstractmethod
    def bulk_ingest(self, files: list[tuple[str, Path]]) -> list[Document]: ...
    @abc.abstractmethod
    def delete(self, doc_id: str) -> None: ...

class BaseIngestComponentWithIndex(BaseIngestComponent, abc.ABC):
    _index: BaseIndex
    def __init__(
        self,
        storage_context: StorageContext,
        embed_model: EmbedType,
        transformations: list[TransformComponent],
        *args: Any,
        **kwargs: Any,
    ) -> None: ...
    def _initialize_index(self) -> BaseIndex: ...
    def _save_index(self) -> None: ...
    def delete(self, doc_id: str) -> None: ...

class SimpleIngestComponent(BaseIngestComponentWithIndex):
    def __init__(
        self,
        storage_context: StorageContext,
        embed_model: EmbedType,
        transformations: list[TransformComponent],
        *args: Any,
        **kwargs: Any,
    ) -> None: ...
    def ingest(self, file_name: str, file_data: Path) -> list[Document]: ...
    def bulk_ingest(self, files: list[tuple[str, Path]]) -> list[Document]: ...
    def _save_docs(self, documents: list[Document]) -> list[Document]: ...

class BatchIngestComponent(BaseIngestComponentWithIndex):
    def __init__(
        self,
        storage_context: StorageContext,
        embed_model: EmbedType,
        transformations: list[TransformComponent],
        count_workers: int,
        *args: Any,
        **kwargs: Any,
    ) -> None: ...
    def ingest(self, file_name: str, file_data: Path) -> list[Document]: ...
    def bulk_ingest(self, files: list[tuple[str, Path]]) -> list[Document]: ...
    def _save_docs(self, documents: list[Document]) -> list[Document]: ...

class ParallelizedIngestComponent(BaseIngestComponentWithIndex):
    def __init__(
        self,
        storage_context: StorageContext,
        embed_model: EmbedType,
        transformations: list[TransformComponent],
        count_workers: int,
        *args: Any,
        **kwargs: Any,
    ) -> None: ...
    def ingest(self, file_name: str, file_data: Path) -> list[Document]: ...
    def bulk_ingest(self, files: list[tuple[str, Path]]) -> list[Document]: ...
    def _save_docs(self, documents: list[Document]) -> list[Document]: ...
    def __del__(self) -> None: ...

class PipelineIngestComponent(BaseIngestComponentWithIndex):
    NODE_FLUSH_COUNT: int
    doc_q: Queue[tuple[Literal["process", "flush", "quit"], str | None, list[Document] | None]]
    node_q: Queue[
        tuple[
            Literal["process", "flush", "quit"],
            str | None,
            list[Document] | None,
            list[BaseNode] | None,
        ]
    ]
    def __init__(
        self,
        storage_context: StorageContext,
        embed_model: EmbedType,
        transformations: list[TransformComponent],
        count_workers: int,
        *args: Any,
        **kwargs: Any,
    ) -> None: ...
    def _doc_to_node(self) -> None: ...
    def _doc_to_node_worker(self, file_name: str, documents: list[Document]) -> None: ...
    def _save_docs(
        self, files: list[str], documents: list[Document], nodes: list[BaseNode]
    ) -> None: ...
    def _write_nodes(self) -> None: ...
    def _flush(self) -> None: ...
    def ingest(self, file_name: str, file_data: Path) -> list[Document]: ...
    def bulk_ingest(self, files: list[tuple[str, Path]]) -> list[Document]: ...

def get_ingestion_component(
    storage_context: StorageContext,
    embed_model: EmbedType,
    transformations: list[TransformComponent],
    settings: Settings,
) -> BaseIngestComponent: ...