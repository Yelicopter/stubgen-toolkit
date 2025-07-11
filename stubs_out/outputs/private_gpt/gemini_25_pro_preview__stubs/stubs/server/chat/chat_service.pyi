from llama_index.core.chat_engine.types import BaseChatEngine as BaseChatEngine
from llama_index.core.llms import ChatMessage as ChatMessage
from llama_index.core.postprocessor.types import BaseNodePostprocessor as BaseNodePostprocessor
from llama_index.core.types import TokenGen as TokenGen
from private_gpt.components.embedding.embedding_component import EmbeddingComponent as EmbeddingComponent
from private_gpt.components.llm.llm_component import LLMComponent as LLMComponent
from private_gpt.components.node_store.node_store_component import NodeStoreComponent as NodeStoreComponent
from private_gpt.components.vector_store.vector_store_component import VectorStoreComponent as VectorStoreComponent
from private_gpt.open_ai.extensions.context_filter import ContextFilter as ContextFilter
from private_gpt.server.chunks.chunks_service import Chunk as Chunk
from private_gpt.settings.settings import Settings as Settings
from pydantic import BaseModel

class Completion(BaseModel):
    response: str
    sources: list[Chunk] | None

class CompletionGen(BaseModel):
    response: TokenGen
    sources: list[Chunk] | None

class ChatEngineInput:
    system_message: ChatMessage | None
    last_message: ChatMessage | None
    chat_history: list[ChatMessage] | None
    @classmethod
    def from_messages(cls, messages: list[ChatMessage]) -> ChatEngineInput: ...
    def __init__(self, system_message, last_message, chat_history) -> None: ...

class ChatService:
    settings: Settings
    def __init__(self, settings: Settings, llm_component: LLMComponent, vector_store_component: VectorStoreComponent, embedding_component: EmbeddingComponent, node_store_component: NodeStoreComponent) -> None: ...
    def stream_chat(self, messages: list[ChatMessage], use_context: bool = ..., context_filter: ContextFilter | None = ...) -> CompletionGen: ...
    def chat(self, messages: list[ChatMessage], use_context: bool = ..., context_filter: ContextFilter | None = ...) -> Completion: ...
