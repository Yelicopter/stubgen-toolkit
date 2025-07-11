import abc
import itertools
import logging
import multiprocessing
import multiprocessing.pool
import os
import threading
from pathlib import Path
from queue import Queue
from typing import Any, Callable

from llama_index.core.data_structs import IndexDict
from llama_index.core.embeddings.utils import EmbedType
from llama_index.core.indices import VectorStoreIndex, load_index_from_storage
from llama_index.core.indices.base import BaseIndex
from llama_index.core.ingestion import run_transformations
from llama_index.core.schema import BaseNode, Document, TransformComponent
from llama_index.core.storage import StorageContext

from private_gpt.components.ingest.ingest_helper import IngestionHelper
from private_gpt.paths import local_data_path
from private_gpt.settings.settings import Settings
from private_gpt.utils.eta import eta

class BaseIngestComponent(abc.ABC):
    storage_context: StorageContext
    embed_model: Any
    transformations: list[Any]
    def __init__(
        self,
        storage_context: StorageContext,
        embed_model: Any,
        transformations: list[Any],
        *args: Any,
        **kwargs: Any,
    ) -> None: ...
    @abc.abstractmethod
    def ingest(self, file_name: str, file_data: Any) -> list[Any]: ...
    @abc.abstractmethod
    def bulk_ingest(self, files: list[tuple[str, Any]]) -> list[Any]: ...
    @abc.abstractmethod
    def delete(self, doc_id: str) -> None: ...

class BaseIngestComponentWithIndex(BaseIngestComponent, abc.ABC):
    show_progress: bool
    _index_thread_lock: threading.Lock
    _index: Any
    def __init__(
        self,
        storage_context: StorageContext,
        embed_model: Any,
        transformations: list[Any],
        *args: Any,
        **kwargs: Any,
    ) -> None: ...
    def _initialize_index(self) -> Any: ...
    def _save_index(self) -> None: ...
    def delete(self, doc_id: str) -> None: ...
    @abc.abstractmethod
    def ingest(self, file_name: str, file_data: Any) -> list[Any]: ...
    @abc.abstractmethod
    def bulk_ingest(self, files: list[tuple[str, Any]]) -> list[Any]: ...

class SimpleIngestComponent(BaseIngestComponentWithIndex):
    def __init__(
        self,
        storage_context: StorageContext,
        embed_model: Any,
        transformations: list[Any],
        *args: Any,
        **kwargs: Any,
    ) -> None: ...
    def ingest(self, file_name: str, file_data: Any) -> list[Any]: ...
    def bulk_ingest(self, files: list[tuple[str, Any]]) -> list[Any]: ...
    def _save_docs(self, documents: list[Any]) -> list[Any]: ...

class BatchIngestComponent(BaseIngestComponentWithIndex):
    count_workers: int
    _file_to_documents_work_pool: multiprocessing.pool.Pool
    def __init__(
        self,
        storage_context: StorageContext,
        embed_model: Any,
        transformations: list[Any],
        count_workers: int,
        *args: Any,
        **kwargs: Any,
    ) -> None: ...
    def ingest(self, file_name: str, file_data: Any) -> list[Any]: ...
    def bulk_ingest(self, files: list[tuple[str, Any]]) -> list[Any]: ...
    def _save_docs(self, documents: list[Any]) -> list[Any]: ...

class ParallelizedIngestComponent(BaseIngestComponentWithIndex):
    count_workers: int
    _ingest_work_pool: multiprocessing.pool.ThreadPool
    _file_to_documents_work_pool: multiprocessing.pool.Pool
    def __init__(
        self,
        storage_context: StorageContext,
        embed_model: Any,
        transformations: list[Any],
        count_workers: int,
        *args: Any,
        **kwargs: Any,
    ) -> None: ...
    def ingest(self, file_name: str, file_data: Any) -> list[Any]: ...
    def bulk_ingest(self, files: list[tuple[str, Any]]) -> list[Any]: ...
    def _save_docs(self, documents: list[Any]) -> list[Any]: ...
    def __del__(self) -> None: ...

class PipelineIngestComponent(BaseIngestComponentWithIndex):
    NODE_FLUSH_COUNT: int
    count_workers: int
    doc_semaphore: "multiprocessing.synchronize.Semaphore"
    doc_q: Queue[Any]
    node_q: Queue[Any]
    def __init__(
        self,
        storage_context: StorageContext,
        embed_model: Any,
        transformations: list[Any],
        count_workers: int,
        *args: Any,
        **kwargs: Any,
    ) -> None: ...
    def _doc_to_node(self) -> None: ...
    def _doc_to_node_worker(self, file_name: str, documents: list[Any]) -> None: ...
    def _save_docs(
        self, files: list[Any], documents: list[Any], nodes: list[Any]
    ) -> None: ...
    def _write_nodes(self) -> None: ...
    def _flush(self) -> None: ...
    def ingest(self, file_name: str, file_data: Any) -> list[Any]: ...
    def bulk_ingest(self, files: list[tuple[str, Any]]) -> list[Any]: ...

def get_ingestion_component(
    storage_context: StorageContext,
    embed_model: Any,
    transformations: list[Any],
    settings: Any,
) -> BaseIngestComponent: ...