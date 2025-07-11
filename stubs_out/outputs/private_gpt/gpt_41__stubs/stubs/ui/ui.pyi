import gradio as gr
from enum import Enum
from fastapi import FastAPI as FastAPI
from gradio.themes.utils.colors import slate as slate
from llama_index.core.llms import ChatMessage as ChatMessage, ChatResponse as ChatResponse, MessageRole as MessageRole
from llama_index.core.types import TokenGen as TokenGen
from pathlib import Path
from private_gpt.constants import PROJECT_ROOT_PATH as PROJECT_ROOT_PATH
from private_gpt.di import global_injector as global_injector
from private_gpt.open_ai.extensions.context_filter import ContextFilter as ContextFilter
from private_gpt.server.chat.chat_service import ChatService as ChatService, CompletionGen as CompletionGen
from private_gpt.server.chunks.chunks_service import Chunk as Chunk, ChunksService as ChunksService
from private_gpt.server.ingest.ingest_service import IngestService as IngestService
from private_gpt.server.recipes.summarize.summarize_service import SummarizeService as SummarizeService
from private_gpt.settings.settings import settings as settings
from private_gpt.ui.images import logo_svg as logo_svg
from pydantic import BaseModel

THIS_DIRECTORY_RELATIVE: Path
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
    def curate_sources(sources: list[Chunk]) -> list['Source']: ...

class PrivateGptUi:
    def __init__(self, ingest_service: IngestService, chat_service: ChatService, chunks_service: ChunksService, summarizeService: SummarizeService) -> None: ...
    def get_ui_blocks(self) -> gr.Blocks: ...
    def mount_in_app(self, app: FastAPI, path: str) -> None: ...
