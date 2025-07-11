import abc
import itertools
import logging
import multiprocessing
import multiprocessing.pool
import os
import threading
from pathlib import Path
from queue import Queue
from typing import Any, Dict, List, Optional, Tuple, Type

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

logger: logging.Logger

class BaseIngestComponent(abc.ABC):
    def __init__(
        self,
        storage_context: StorageContext,
        embed_model: EmbedType,
        transformations: List[TransformComponent],
        *args: Any,
        **kwargs: Any,
    ) -> None: ...
    
    @abc.abstractmethod
    def ingest(self, file_name: str, file_data: Path) -> List[Document]: ...
    
    @abc.abstractmethod
    def bulk_ingest(self, files: List[Tuple[str, Path]]) -> List[Document]: ...
    
    @abc.abstractmethod
    def delete(self, doc_id: str) -> None: ...

class BaseIngestComponentWithIndex(BaseIngestComponent, abc.ABC):
    def __init__(
        self,
        storage_context: StorageContext,
        embed_model: EmbedType,
        transformations: List[TransformComponent],
        *args: Any,
        **kwargs: Any,
    ) -> None: ...
    
    def _initialize_index(self) -> BaseIndex | VectorStoreIndex: ...
    def _save_index(self) -> None: ...
    def delete(self, doc_id: str) -> None: ...

class SimpleIngestComponent(BaseIngestComponentWithIndex):
    def __init__(
        self,
        storage_context: StorageContext,
        embed_model: EmbedType,
        transformations: List[TransformComponent],
        *args: Any,
        **kwargs: Any,
    ) -> None: ...
    
    def ingest(self, file_name: str, file_data: Path) -> List[Document]: ...
    def bulk_ingest(self, files: List[Tuple[str, Path]]) -> List[Document]: ...
    def _save_docs(self, documents: List[Document]) -> List[Document]: ...

class BatchIngestComponent(BaseIngestComponentWithIndex):
    def __init__(
        self,
        storage_context: StorageContext,
        embed_model: EmbedType,
        transformations: List[TransformComponent],
        count_workers: int,
        *args: Any,
        **kwargs: Any,
    ) -> None: ...
    
    def ingest(self, file_name: str, file_data: Path) -> List[Document]: ...
    def bulk_ingest(self, files: List[Tuple[str, Path]]) -> List[Document]: ...
    def _save_docs(self, documents: List[Document]) -> List[Document]: ...

class ParallelizedIngestComponent(BaseIngestComponentWithIndex):
    def __init__(
        self,
        storage_context: StorageContext,
        embed_model: EmbedType,
        transformations: List[TransformComponent],
        count_workers: int,
        *args: Any,
        **kwargs: Any,
    ) -> None: ...
    
    def ingest(self, file_name: str, file_data: Path) -> List[Document]: ...
    def bulk_ingest(self, files: List[Tuple[str, Path]]) -> List[Document]: ...
    def _save_docs(self, documents: List[Document]) -> List[Document]: ...
    def __del__(self) -> None: ...

class PipelineIngestComponent(BaseIngestComponentWithIndex):
    NODE_FLUSH_COUNT: int = 5000
    
    def __init__(
        self,
        storage_context: StorageContext,
        embed_model: EmbedType,
        transformations: List[TransformComponent],
        count_workers: int,
        *args: Any,
        **kwargs: Any,
    ) -> None: ...
    
    def _doc_to_node(self) -> None: ...
    def _doc_to_node_worker(self, file_name: str, documents: List[Document]) -> None: ...
    def _save_docs(
        self, files: List[str], documents: List[Document], nodes: List[BaseNode]
    ) -> None: ...
    def _write_nodes(self) -> None: ...
    def _flush(self) -> None: ...
    def ingest(self, file_name: str, file_data: Path) -> List[Document]: ...
    def bulk_ingest(self, files: List[Tuple[str, Path]]) -> List[Document]: ...

def get_ingestion_component(
    storage_context: StorageContext,
    embed_model: EmbedType,
    transformations: List[TransformComponent],
    settings: Settings,
) -> BaseIngestComponent: ...