from typing import Literal

from fastapi import APIRouter, Request, UploadFile
from pydantic import BaseModel, Field

from private_gpt.server.ingest.model import IngestedDoc

ingest_router: APIRouter

class IngestTextBody(BaseModel):
    file_name: str = Field(examples=["Avatar: The Last Airbender"])
    text: str = Field(
        examples=[
            "Avatar is set in an Asian and Arctic-inspired world in which some "
            "people can telekinetically manipulate one of the four elements—water, "
            "earth, fire or air—through practices known as 'bending', inspired by "
            "Chinese martial arts."
        ]
    )

class IngestResponse(BaseModel):
    object: Literal["list"]
    model: Literal["private-gpt"]
    data: list[IngestedDoc]

def ingest(request: Request, file: UploadFile) -> IngestResponse: ...
def ingest_file(request: Request, file: UploadFile) -> IngestResponse: ...
def ingest_text(request: Request, body: IngestTextBody) -> IngestResponse: ...
def list_ingested(request: Request) -> IngestResponse: ...
def delete_ingested(request: Request, doc_id: str) -> None: ...