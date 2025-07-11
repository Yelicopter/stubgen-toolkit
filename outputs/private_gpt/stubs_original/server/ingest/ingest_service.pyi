from _typeshed import Incomplete
from llama_index.core.storage.docstore.types import RefDocInfo as RefDocInfo
from pathlib import Path
from private_gpt.components.embedding.embedding_component import EmbeddingComponent as EmbeddingComponent
from private_gpt.components.ingest.ingest_component import get_ingestion_component as get_ingestion_component
from private_gpt.components.llm.llm_component import LLMComponent as LLMComponent
from private_gpt.components.node_store.node_store_component import NodeStoreComponent as NodeStoreComponent
from private_gpt.components.vector_store.vector_store_component import VectorStoreComponent as VectorStoreComponent
from private_gpt.server.ingest.model import IngestedDoc as IngestedDoc
from private_gpt.settings.settings import settings as settings
from typing import BinaryIO

logger: Incomplete

class IngestService:
    llm_service: Incomplete
    storage_context: Incomplete
    ingest_component: Incomplete
    def __init__(self, llm_component: LLMComponent, vector_store_component: VectorStoreComponent, embedding_component: EmbeddingComponent, node_store_component: NodeStoreComponent) -> None: ...
    def ingest_file(self, file_name: str, file_data: Path) -> list[IngestedDoc]: ...
    def ingest_text(self, file_name: str, text: str) -> list[IngestedDoc]: ...
    def ingest_bin_data(self, file_name: str, raw_file_data: BinaryIO) -> list[IngestedDoc]: ...
    def bulk_ingest(self, files: list[tuple[str, Path]]) -> list[IngestedDoc]: ...
    def list_ingested(self) -> list[IngestedDoc]: ...
    def delete(self, doc_id: str) -> None: ...
