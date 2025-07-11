from _typeshed import Incomplete
from fastapi import Request as Request, UploadFile
from private_gpt.server.ingest.ingest_service import IngestService as IngestService
from private_gpt.server.ingest.model import IngestedDoc as IngestedDoc
from private_gpt.server.utils.auth import authenticated as authenticated
from pydantic import BaseModel
from typing import Literal

ingest_router: Incomplete

class IngestTextBody(BaseModel):
    file_name: str
    text: str

class IngestResponse(BaseModel):
    object: Literal['list']
    model: Literal['private-gpt']
    data: list[IngestedDoc]

def ingest(request: Request, file: UploadFile) -> IngestResponse: ...
def ingest_file(request: Request, file: UploadFile) -> IngestResponse: ...
def ingest_text(request: Request, body: IngestTextBody) -> IngestResponse: ...
def list_ingested(request: Request) -> IngestResponse: ...
def delete_ingested(request: Request, doc_id: str) -> None: ...
