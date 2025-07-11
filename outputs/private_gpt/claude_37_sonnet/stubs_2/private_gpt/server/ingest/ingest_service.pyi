import logging
import tempfile
from pathlib import Path
from typing import TYPE_CHECKING, AnyStr, BinaryIO, List, Optional, Tuple

from injector import inject, singleton
from llama_index.core.node_parser import SentenceWindowNodeParser
from llama_index.core.storage import StorageContext

from private_gpt.components.embedding.embedding_component import EmbeddingComponent
from private_gpt.components.ingest.ingest_component import get_ingestion_component
from private_gpt.components.llm.llm_component import LLMComponent
from private_gpt.components.node_store.node_store_component import NodeStoreComponent
from private_gpt.components.vector_store.vector_store_component import (
    VectorStoreComponent,
)
from private_gpt.server.ingest.model import IngestedDoc
from private_gpt.settings.settings import settings

logger: logging.Logger

@singleton
class IngestService:
    @inject
    def __init__(
        self,
        llm_component: LLMComponent,
        vector_store_component: VectorStoreComponent,
        embedding_component: EmbeddingComponent,
        node_store_component: NodeStoreComponent,
    ) -> None: ...
    
    def _ingest_data(self, file_name: str, file_data: AnyStr) -> List[IngestedDoc]: ...
    def ingest_file(self, file_name: str, file_data: Path) -> List[IngestedDoc]: ...
    def ingest_text(self, file_name: str, text: str) -> List[IngestedDoc]: ...
    def ingest_bin_data(
        self, file_name: str, raw_file_data: BinaryIO
    ) -> List[IngestedDoc]: ...
    def bulk_ingest(self, files: List[Tuple[str, Path]]) -> List[IngestedDoc]: ...
    def list_ingested(self) -> List[IngestedDoc]: ...
    def delete(self, doc_id: str) -> None: ...