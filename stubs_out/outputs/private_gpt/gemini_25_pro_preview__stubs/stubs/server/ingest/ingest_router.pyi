from fastapi import APIRouter as APIRouter, Request as Request, UploadFile as UploadFile
from private_gpt.server.ingest.model import IngestedDoc as IngestedDoc
from pydantic import BaseModel
from typing import Literal

ingest_router: APIRouter

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
