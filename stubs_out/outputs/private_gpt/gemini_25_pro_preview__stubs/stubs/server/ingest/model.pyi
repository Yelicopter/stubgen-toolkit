from llama_index.core.schema import Document as Document
from pydantic import BaseModel
from typing import Any, Literal

class IngestedDoc(BaseModel):
    object: Literal['ingest.document']
    doc_id: str
    doc_metadata: dict[str, Any] | None
    @staticmethod
    def curate_metadata(metadata: dict[str, Any]) -> dict[str, Any]: ...
    @staticmethod
    def from_document(document: Document) -> IngestedDoc: ...
