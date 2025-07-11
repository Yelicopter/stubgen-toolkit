import gradio as gr
from enum import Enum
from fastapi import FastAPI as FastAPI
from pathlib import Path
from private_gpt.server.chat.chat_service import ChatService as ChatService, CompletionGen as CompletionGen
from private_gpt.server.chunks.chunks_service import Chunk as Chunk, ChunksService as ChunksService
from private_gpt.server.ingest.ingest_service import IngestService as IngestService
from private_gpt.server.recipes.summarize.summarize_service import SummarizeService as SummarizeService
from pydantic import BaseModel

AVATAR_BOT: Path
UI_TAB_TITLE: str
SOURCES_SEPARATOR: str

class Modes(str, Enum):
    RAG_MODE: str
    SEARCH_MODE: str
    BASIC_CHAT_MODE: str
    SUMMARIZE_MODE: str

MODES: list[Modes]

class Source(BaseModel):
    file: str
    page: str
    text: str
    class Config:
        frozen: bool
    @staticmethod
    def curate_sources(sources: list[Chunk]) -> list[Source]: ...

class PrivateGptUi:
    def __init__(self, ingest_service: IngestService, chat_service: ChatService, chunks_service: ChunksService, summarizeService: SummarizeService) -> None: ...
    def get_ui_blocks(self) -> gr.Blocks: ...
    def mount_in_app(self, app: FastAPI, path: str) -> None: ...
