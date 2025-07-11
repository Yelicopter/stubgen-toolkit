from _typeshed import Incomplete
from fastapi import Depends as Depends, HTTPException as HTTPException, Request as Request, UploadFile as UploadFile
from pydantic import BaseModel, Field as Field
from typing import Any, Literal

ingest_router: Incomplete

class IngestTextBody(BaseModel):
    file_name: str
    text: str

class IngestResponse(BaseModel):
    object: Literal['list']
    model: Literal['private-gpt']
    data: list[Any]

def ingest(request: Request, file: UploadFile) -> IngestResponse: ...
def ingest_file(request: Request, file: UploadFile) -> IngestResponse: ...
def ingest_text(request: Request, body: IngestTextBody) -> IngestResponse: ...
def list_ingested(request: Request) -> IngestResponse: ...
def delete_ingested(request: Request, doc_id: str) -> IngestResponse: ...
