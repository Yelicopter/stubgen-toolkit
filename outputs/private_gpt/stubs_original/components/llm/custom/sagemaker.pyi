from _typeshed import Incomplete
from collections.abc import Sequence
from llama_index.callbacks import CallbackManager as CallbackManager
from llama_index.core.llms import CompletionResponse, CustomLLM, LLMMetadata
from llama_index.llms import ChatMessage as ChatMessage, ChatResponse as ChatResponse, ChatResponseGen as ChatResponseGen, CompletionResponseGen as CompletionResponseGen
from typing import Any

logger: Incomplete

class LineIterator:
    byte_iterator: Incomplete
    buffer: Incomplete
    read_pos: int
    def __init__(self, stream: Any) -> None: ...
    def __iter__(self) -> Any: ...
    def __next__(self) -> Any: ...

class SagemakerLLM(CustomLLM):
    endpoint_name: str
    temperature: float
    max_new_tokens: int
    context_window: int
    messages_to_prompt: Any
    completion_to_prompt: Any
    generate_kwargs: dict[str, Any]
    model_kwargs: dict[str, Any]
    verbose: bool
    def __init__(self, endpoint_name: str | None = ..., temperature: float = ..., max_new_tokens: int = ..., context_window: int = ..., messages_to_prompt: Any = ..., completion_to_prompt: Any = ..., callback_manager: CallbackManager | None = ..., generate_kwargs: dict[str, Any] | None = ..., model_kwargs: dict[str, Any] | None = ..., verbose: bool = ...) -> None: ...
    @property
    def inference_params(self): ...
    @property
    def metadata(self) -> LLMMetadata: ...
    def complete(self, prompt: str, **kwargs: Any) -> CompletionResponse: ...
    def stream_complete(self, prompt: str, **kwargs: Any) -> CompletionResponseGen: ...
    def chat(self, messages: Sequence[ChatMessage], **kwargs: Any) -> ChatResponse: ...
    def stream_chat(self, messages: Sequence[ChatMessage], **kwargs: Any) -> ChatResponseGen: ...
