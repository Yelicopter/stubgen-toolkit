from __future__ import annotations

from typing import TYPE_CHECKING, Any, Callable, Iterator, Self

from llama_index.core.base.llms.generic_utils import (
    completion_response_to_chat_response,
    stream_completion_response_to_chat_response,
)
from llama_index.core.bridge.pydantic import Field
from llama_index.core.llms import (
    CompletionResponse,
    CustomLLM,
    LLMMetadata,
)
from llama_index.core.llms.callbacks import (
    llm_chat_callback,
    llm_completion_callback,
)

if TYPE_CHECKING:
    from collections.abc import Sequence

    from llama_index.core.callbacks import CallbackManager
    from llama_index.core.llms import (
        ChatMessage,
        ChatResponse,
        ChatResponseGen,
        CompletionResponseGen,
    )

class LineIterator:
    def __init__(self, stream: Any) -> None: ...
    def __iter__(self) -> Self: ...
    def __next__(self) -> bytes: ...

class SagemakerLLM(CustomLLM):
    endpoint_name: str = Field(description="")
    temperature: float = Field(description="The temperature to use for sampling.")
    max_new_tokens: int = Field(description="The maximum number of tokens to generate.")
    context_window: int = Field(
        description="The maximum number of context tokens for the model."
    )
    messages_to_prompt: Callable[[Sequence[ChatMessage]], str] = Field(
        description="The function to convert messages to a prompt.", exclude=True
    )
    completion_to_prompt: Callable[[str], str] = Field(
        description="The function to convert a completion to a prompt.", exclude=True
    )
    generate_kwargs: dict[str, Any] = Field(
        default_factory=dict, description="Kwargs used for generation."
    )
    model_kwargs: dict[str, Any] = Field(
        default_factory=dict, description="Kwargs used for model initialization."
    )
    verbose: bool = Field(description="Whether to print verbose output.")
    _boto_client: Any
    def __init__(
        self,
        endpoint_name: str = ...,
        temperature: float = ...,
        max_new_tokens: int = ...,
        context_window: int = ...,
        messages_to_prompt: Callable[[Sequence[ChatMessage]], str] | None = ...,
        completion_to_prompt: Callable[[str], str] | None = ...,
        callback_manager: CallbackManager | None = ...,
        generate_kwargs: dict[str, Any] | None = ...,
        model_kwargs: dict[str, Any] | None = ...,
        verbose: bool = ...,
    ) -> None: ...
    @property
    def inference_params(self) -> dict[str, Any]: ...
    @property
    def metadata(self) -> LLMMetadata: ...
    @llm_completion_callback()
    def complete(self, prompt: str, **kwargs: Any) -> CompletionResponse: ...
    @llm_completion_callback()
    def stream_complete(
        self, prompt: str, **kwargs: Any
    ) -> CompletionResponseGen: ...
    @llm_chat_callback()
    def chat(self, messages: Sequence[ChatMessage], **kwargs: Any) -> ChatResponse: ...
    @llm_chat_callback()
    def stream_chat(
        self, messages: Sequence[ChatMessage], **kwargs: Any
    ) -> ChatResponseGen: ...