from __future__ import annotations

from enum import Enum
from pathlib import Path
from typing import Any, Iterator

import gradio as gr
from fastapi import FastAPI
from pydantic import BaseModel

from private_gpt.server.chat.chat_service import ChatService, CompletionGen
from private_gpt.server.chunks.chunks_service import Chunk, ChunksService
from private_gpt.server.ingest.ingest_service import IngestService
from private_gpt.server.recipes.summarize.summarize_service import SummarizeService

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
    def __init__(
        self,
        ingest_service: IngestService,
        chat_service: ChatService,
        chunks_service: ChunksService,
        summarizeService: SummarizeService,
    ) -> None: ...
    def _chat(
        self, message: str, history: list[list[str | None]], mode: Modes, *_: Any
    ) -> Iterator[str]: ...
    @staticmethod
    def _get_default_system_prompt(mode: Modes) -> str: ...
    @staticmethod
    def _get_default_mode_explanation(mode: Modes) -> str: ...
    def _set_system_prompt(self, system_prompt_input: str) -> None: ...
    def _set_explanatation_mode(self, explanation_mode: str) -> None: ...
    def _set_current_mode(self, mode: Modes) -> list[Any]: ...
    def _list_ingested_files(self) -> list[list[str]]: ...
    def _upload_file(self, files: list[str]) -> None: ...
    def _delete_all_files(self) -> list[Any]: ...
    def _delete_selected_file(self) -> list[Any]: ...
    def _deselect_selected_file(self) -> list[Any]: ...
    def _selected_a_file(self, select_data: gr.SelectData) -> list[Any]: ...
    def _build_ui_blocks(self) -> gr.Blocks: ...
    def get_ui_blocks(self) -> gr.Blocks: ...
    def mount_in_app(self, app: FastAPI, path: str) -> None: ...