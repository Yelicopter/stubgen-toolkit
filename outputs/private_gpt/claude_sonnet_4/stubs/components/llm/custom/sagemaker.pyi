from __future__ import annotations
import io
import json
import logging
from typing import TYPE_CHECKING, Any, Iterator, Optional
import boto3
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
    from llama_index.callbacks import CallbackManager
    from llama_index.llms import (
        ChatMessage,
        ChatResponse,
        ChatResponseGen,
        CompletionResponseGen,
    )

logger: logging.Logger

class LineIterator:
    byte_iterator: Iterator[Any]
    buffer: io.BytesIO
    read_pos: int
    
    def __init__(self, stream: Any) -> None: ...
    def __iter__(self) -> LineIterator: ...
    def __next__(self) -> bytes: ...

class SagemakerLLM(CustomLLM):
    endpoint_name: str = Field(description="")
    temperature: float = Field(description="The temperature to use for sampling.")
    max_new_tokens: int = Field(description="The maximum number of tokens to generate.")
    context_window: int = Field(
        description="The maximum number of context tokens for the model."
    )
    messages_to_prompt: Any = Field(
        description="The function to convert messages to a prompt.", exclude=True
    )
    completion_to_prompt: Any = Field(
        description="The function to convert a completion to a prompt.", exclude=True
    )
    generate_kwargs: Dict[str, Any] = Field(
        default_factory=dict, description="Kwargs used for generation."
    )
    model_kwargs: Dict[str, Any] = Field(
        default_factory=dict, description="Kwargs used for model initialization."
    )
    verbose: bool = Field(description="Whether to print verbose output.")
    _boto_client: Any = ...
    
    def __init__(
        self,
        endpoint_name: str = "",
        temperature: float = 0.1,
        max_new_tokens: int = 512,
        context_window: int = 2048,
        messages_to_prompt: Optional[Any] = None,
        completion_to_prompt: Optional[Any] = None,
        callback_manager: Optional[CallbackManager] = None,
        generate_kwargs: Optional[Dict[str, Any]] = None,
        model_kwargs: Optional[Dict[str, Any]] = None,
        verbose: bool = True,
    ) -> None: ...
    
    @property
    def inference_params(self) -> Dict[str, Any]: ...
    
    @property
    def metadata(self) -> LLMMetadata: ...
    
    @llm_completion_callback()
    def complete(self, prompt: str, **kwargs: Any) -> CompletionResponse: ...
    
    @llm_completion_callback()
    def stream_complete(self, prompt: str, **kwargs: Any) -> CompletionResponseGen: ...
    
    @llm_chat_callback()
    def chat(self, messages: Sequence[ChatMessage], **kwargs: Any) -> ChatResponse: ...
    
    @llm_chat_callback()
    def stream_chat(
        self, messages: Sequence[ChatMessage], **kwargs: Any
    ) -> ChatResponseGen: ...