from llama_index.core.schema import Document as Document
from pydantic import BaseModel
from typing import Any, Dict, Literal, Optional

class IngestedDoc(BaseModel):
    object: Literal['ingest.document']
    doc_id: str
    doc_metadata: Optional[Dict[str, Any]]
    @staticmethod
    def curate_metadata(metadata: Dict[str, Any]) -> Dict[str, Any]: ...
    @staticmethod
    def from_document(document: Document) -> IngestedDoc: ...
