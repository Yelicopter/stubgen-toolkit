from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from llama_index.core.chat_engine.types import BaseChatEngine
from llama_index.core.llms import ChatMessage
from llama_index.core.types import TokenGen
from pydantic import BaseModel

from private_gpt.components.embedding.embedding_component import EmbeddingComponent
from private_gpt.components.llm.llm_component import LLMComponent
from private_gpt.components.node_store.node_store_component import NodeStoreComponent
from private_gpt.components.vector_store.vector_store_component import (
    VectorStoreComponent,
)
from private_gpt.open_ai.extensions.context_filter import ContextFilter
from private_gpt.server.chunks.chunks_service import Chunk
from private_gpt.settings.settings import Settings

if TYPE_CHECKING:
    from llama_index.core.postprocessor.types import BaseNodePostprocessor

class Completion(BaseModel):
    response: str
    sources: list[Chunk] | None

class CompletionGen(BaseModel):
    response: TokenGen
    sources: list[Chunk] | None

@dataclass
class ChatEngineInput:
    system_message: ChatMessage | None
    last_message: ChatMessage | None
    chat_history: list[ChatMessage] | None
    @classmethod
    def from_messages(cls, messages: list[ChatMessage]) -> ChatEngineInput: ...

class ChatService:
    settings: Settings
    def __init__(
        self,
        settings: Settings,
        llm_component: LLMComponent,
        vector_store_component: VectorStoreComponent,
        embedding_component: EmbeddingComponent,
        node_store_component: NodeStoreComponent,
    ) -> None: ...
    def _chat_engine(
        self,
        system_prompt: str | None = ...,
        use_context: bool = ...,
        context_filter: ContextFilter | None = ...,
    ) -> BaseChatEngine: ...
    def stream_chat(
        self,
        messages: list[ChatMessage],
        use_context: bool = ...,
        context_filter: ContextFilter | None = ...,
    ) -> CompletionGen: ...
    def chat(
        self,
        messages: list[ChatMessage],
        use_context: bool = ...,
        context_filter: ContextFilter | None = ...,
    ) -> Completion: ...