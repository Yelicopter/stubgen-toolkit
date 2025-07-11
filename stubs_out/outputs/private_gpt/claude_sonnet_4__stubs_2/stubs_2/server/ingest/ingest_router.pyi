from fastapi import APIRouter as APIRouter, Depends as Depends, HTTPException as HTTPException, Request as Request, UploadFile as UploadFile
from private_gpt.server.ingest.ingest_service import IngestService as IngestService
from private_gpt.server.ingest.model import IngestedDoc as IngestedDoc
from private_gpt.server.utils.auth import authenticated as authenticated
from pydantic import BaseModel
from typing import List, Literal

ingest_router: APIRouter

class IngestTextBody(BaseModel):
    file_name: str
    text: str

class IngestResponse(BaseModel):
    object: Literal['list']
    model: Literal['private-gpt']
    data: List[IngestedDoc]

def ingest(request: Request, file: UploadFile) -> IngestResponse: ...
def ingest_file(request: Request, file: UploadFile) -> IngestResponse: ...
def ingest_text(request: Request, body: IngestTextBody) -> IngestResponse: ...
def list_ingested(request: Request) -> IngestResponse: ...
def delete_ingested(request: Request, doc_id: str) -> None: ...
