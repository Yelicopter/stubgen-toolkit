from pathlib import Path
from typing import AnyStr, BinaryIO

from private_gpt.components.embedding.embedding_component import EmbeddingComponent
from private_gpt.components.llm.llm_component import LLMComponent
from private_gpt.components.node_store.node_store_component import NodeStoreComponent
from private_gpt.components.vector_store.vector_store_component import (
    VectorStoreComponent,
)
from private_gpt.server.ingest.model import IngestedDoc

class IngestService:
    def __init__(
        self,
        llm_component: LLMComponent,
        vector_store_component: VectorStoreComponent,
        embedding_component: EmbeddingComponent,
        node_store_component: NodeStoreComponent,
    ) -> None: ...
    def _ingest_data(self, file_name: str, file_data: AnyStr) -> list[IngestedDoc]: ...
    def ingest_file(self, file_name: str, file_data: Path) -> list[IngestedDoc]: ...
    def ingest_text(self, file_name: str, text: str) -> list[IngestedDoc]: ...
    def ingest_bin_data(
        self, file_name: str, raw_file_data: BinaryIO
    ) -> list[IngestedDoc]: ...
    def bulk_ingest(self, files: list[tuple[str, Path]]) -> list[IngestedDoc]: ...
    def list_ingested(self) -> list[IngestedDoc]: ...
    def delete(self, doc_id: str) -> None: ...