from dataclasses import dataclass
from typing import List, Optional, TYPE_CHECKING

from injector import inject, singleton
from llama_index.core.chat_engine import ContextChatEngine, SimpleChatEngine
from llama_index.core.chat_engine.types import (
    BaseChatEngine,
)
from llama_index.core.indices import VectorStoreIndex
from llama_index.core.indices.postprocessor import MetadataReplacementPostProcessor
from llama_index.core.llms import ChatMessage, MessageRole
from llama_index.core.postprocessor import (
    SentenceTransformerRerank,
    SimilarityPostprocessor,
)
from llama_index.core.storage import StorageContext
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

class Completion(BaseModel):
    response: str
    sources: Optional[List[Chunk]] = None

class CompletionGen(BaseModel):
    response: TokenGen
    sources: Optional[List[Chunk]] = None

@dataclass
class ChatEngineInput:
    system_message: Optional[ChatMessage] = None
    last_message: Optional[ChatMessage] = None
    chat_history: Optional[List[ChatMessage]] = None

    @classmethod
    def from_messages(cls, messages: List[ChatMessage]) -> 'ChatEngineInput': ...

@singleton
class ChatService:
    settings: Settings

    @inject
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
        system_prompt: Optional[str] = None,
        use_context: bool = False,
        context_filter: Optional[ContextFilter] = None,
    ) -> BaseChatEngine: ...
    
    def stream_chat(
        self,
        messages: List[ChatMessage],
        use_context: bool = False,
        context_filter: Optional[ContextFilter] = None,
    ) -> CompletionGen: ...
    
    def chat(
        self,
        messages: List[ChatMessage],
        use_context: bool = False,
        context_filter: Optional[ContextFilter] = None,
    ) -> Completion: ...