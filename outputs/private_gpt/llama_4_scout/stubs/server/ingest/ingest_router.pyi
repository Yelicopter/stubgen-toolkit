from fastapi import APIRouter, Depends, HTTPException, Request, UploadFile
from pydantic import BaseModel, Field

ingest_router = APIRouter()

class IngestTextBody(BaseModel):
    file_name: str
    text: str

class IngestResponse(BaseModel):
    object: Literal["list"]
    model: Literal["private-gpt"]
    data: list[Any]

@ingest_router.post("/ingest", response_model=IngestResponse, deprecated=True)
def ingest(request: Request, file: UploadFile) -> IngestResponse:
    ...

@ingest_router.post("/ingest/file", response_model=IngestResponse)
def ingest_file(request: Request, file: UploadFile) -> IngestResponse:
    ...

@ingest_router.post("/ingest/text", response_model=IngestResponse)
def ingest_text(request: Request, body: IngestTextBody) -> IngestResponse:
    ...

@ingest_router.get("/ingest/list", response_model=IngestResponse)
def list_ingested(request: Request) -> IngestResponse:
    ...

@ingest_router.delete("/ingest/{doc_id}", response_model=IngestResponse)
def delete_ingested(request: Request, doc_id: str) -> IngestResponse:
    ...