from llama_index.core.chat_engine import ContextChatEngine as ContextChatEngine, SimpleChatEngine as SimpleChatEngine
from llama_index.core.chat_engine.types import BaseChatEngine as BaseChatEngine
from llama_index.core.indices import VectorStoreIndex as VectorStoreIndex
from llama_index.core.indices.postprocessor import MetadataReplacementPostProcessor as MetadataReplacementPostProcessor
from llama_index.core.llms import ChatMessage as ChatMessage, MessageRole as MessageRole
from llama_index.core.postprocessor import SentenceTransformerRerank as SentenceTransformerRerank, SimilarityPostprocessor as SimilarityPostprocessor
from llama_index.core.storage import StorageContext as StorageContext
from llama_index.core.types import TokenGen as TokenGen
from private_gpt.components.embedding.embedding_component import EmbeddingComponent as EmbeddingComponent
from private_gpt.components.llm.llm_component import LLMComponent as LLMComponent
from private_gpt.components.node_store.node_store_component import NodeStoreComponent as NodeStoreComponent
from private_gpt.components.vector_store.vector_store_component import VectorStoreComponent as VectorStoreComponent
from private_gpt.open_ai.extensions.context_filter import ContextFilter as ContextFilter
from private_gpt.server.chunks.chunks_service import Chunk as Chunk
from private_gpt.settings.settings import Settings as Settings
from pydantic import BaseModel
from typing import List, Optional

class Completion(BaseModel):
    response: str
    sources: Optional[List[Chunk]]

class CompletionGen(BaseModel):
    response: TokenGen
    sources: Optional[List[Chunk]]

class ChatEngineInput:
    system_message: Optional[ChatMessage]
    last_message: Optional[ChatMessage]
    chat_history: Optional[List[ChatMessage]]
    @classmethod
    def from_messages(cls, messages: List[ChatMessage]) -> ChatEngineInput: ...
    def __init__(self, system_message, last_message, chat_history) -> None: ...

class ChatService:
    settings: Settings
    def __init__(self, settings: Settings, llm_component: LLMComponent, vector_store_component: VectorStoreComponent, embedding_component: EmbeddingComponent, node_store_component: NodeStoreComponent) -> None: ...
    def stream_chat(self, messages: List[ChatMessage], use_context: bool = ..., context_filter: Optional[ContextFilter] = ...) -> CompletionGen: ...
    def chat(self, messages: List[ChatMessage], use_context: bool = ..., context_filter: Optional[ContextFilter] = ...) -> Completion: ...
