import base64
import logging
import time
from collections.abc import Iterable
from enum import Enum
from pathlib import Path
from typing import Any

import gradio as gr
from fastapi import FastAPI
from gradio.themes.utils.colors import slate
from injector import inject, singleton
from llama_index.core.llms import ChatMessage, ChatResponse, MessageRole
from llama_index.core.types import TokenGen
from pydantic import BaseModel

from private_gpt.constants import PROJECT_ROOT_PATH
from private_gpt.di import global_injector
from private_gpt.open_ai.extensions.context_filter import ContextFilter
from private_gpt.server.chat.chat_service import ChatService, CompletionGen
from private_gpt.server.chunks.chunks_service import Chunk, ChunksService
from private_gpt.server.ingest.ingest_service import IngestService
from private_gpt.server.recipes.summarize.summarize_service import SummarizeService
from private_gpt.settings.settings import settings
from private_gpt.ui.images import logo_svg

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
    def curate_sources(sources: list[Chunk]) -> list["Source"]: ...

@singleton
class PrivateGptUi:
    @inject
    def __init__(
        self,
        ingest_service: IngestService,
        chat_service: ChatService,
        chunks_service: ChunksService,
        summarizeService: SummarizeService,
    ) -> None: ...
    def _chat(
        self, message: str, history: list[list[str]], mode: str, *args: Any
    ) -> Iterable[str]: ...
    @staticmethod
    def _get_default_system_prompt(mode: Modes) -> str: ...
    @staticmethod
    def _get_default_mode_explanation(mode: Modes) -> str: ...
    def _set_system_prompt(self, system_prompt_input: str) -> None: ...
    def _set_explanatation_mode(self, explanation_mode: str) -> None: ...
    def _set_current_mode(self, mode: str) -> list[Any]: ...
    def _list_ingested_files(self) -> list[list[str]]: ...
    def _upload_file(self, files: list[str]) -> None: ...
    def _delete_all_files(self) -> list[Any]: ...
    def _delete_selected_file(self) -> list[Any]: ...
    def _deselect_selected_file(self) -> list[Any]: ...
    def _selected_a_file(self, select_data: Any) -> list[Any]: ...
    def _build_ui_blocks(self) -> gr.Blocks: ...
    def get_ui_blocks(self) -> gr.Blocks: ...
    def mount_in_app(self, app: FastAPI, path: str) -> None: ...