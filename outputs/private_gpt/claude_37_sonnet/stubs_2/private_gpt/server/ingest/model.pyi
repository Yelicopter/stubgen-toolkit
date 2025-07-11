from typing import Any, Dict, Literal, Optional

from llama_index.core.schema import Document
from pydantic import BaseModel, Field

class IngestedDoc(BaseModel):
    object: Literal["ingest.document"]
    doc_id: str = Field(examples=["c202d5e6-7b69-4869-81cc-dd574ee8ee11"])
    doc_metadata: Optional[Dict[str, Any]] = Field(
        examples=[
            {
                "page_label": "2",
                "file_name": "Sales Report Q3 2023.pdf",
            }
        ]
    )

    @staticmethod
    def curate_metadata(metadata: Dict[str, Any]) -> Dict[str, Any]: ...

    @staticmethod
    def from_document(document: Document) -> 'IngestedDoc': ...