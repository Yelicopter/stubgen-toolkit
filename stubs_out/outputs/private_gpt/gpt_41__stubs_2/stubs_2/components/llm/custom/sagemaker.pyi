import io
from collections.abc import Sequence as Sequence
from llama_index.callbacks import CallbackManager as CallbackManager
from llama_index.core.base.llms.generic_utils import completion_response_to_chat_response as completion_response_to_chat_response, stream_completion_response_to_chat_response as stream_completion_response_to_chat_response
from llama_index.core.bridge.pydantic import Field as Field
from llama_index.core.llms import CompletionResponse as CompletionResponse, CustomLLM, LLMMetadata as LLMMetadata
from llama_index.llms import ChatMessage as ChatMessage, ChatResponse as ChatResponse, ChatResponseGen as ChatResponseGen, CompletionResponseGen as CompletionResponseGen
from typing import Any

class LineIterator:
    byte_iterator: Any
    buffer: io.BytesIO
    read_pos: int
    def __init__(self, stream: Any) -> None: ...
    def __iter__(self) -> LineIterator: ...
    def __next__(self) -> bytes: ...

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
    def __init__(self, endpoint_name: str = ..., temperature: float = ..., max_new_tokens: int = ..., context_window: int = ..., messages_to_prompt: Any = ..., completion_to_prompt: Any = ..., callback_manager: Any = ..., generate_kwargs: dict[str, Any] | None = ..., model_kwargs: dict[str, Any] | None = ..., verbose: bool = ...) -> None: ...
    @property
    def inference_params(self) -> dict[str, Any]: ...
    @property
    def metadata(self) -> LLMMetadata: ...
    def complete(self, prompt: str, **kwargs: Any) -> CompletionResponse: ...
    def stream_complete(self, prompt: str, **kwargs: Any) -> Any: ...
    def chat(self, messages: Any, **kwargs: Any) -> Any: ...
    def stream_chat(self, messages: Any, **kwargs: Any) -> Any: ...
