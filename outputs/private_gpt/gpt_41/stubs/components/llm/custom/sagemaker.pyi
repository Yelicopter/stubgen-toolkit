from __future__ import annotations
import io
import json
import logging
from typing import TYPE_CHECKING, Any

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

class LineIterator:
    byte_iterator: Any
    buffer: io.BytesIO
    read_pos: int
    def __init__(self, stream: Any) -> None: ...
    def __iter__(self) -> "LineIterator": ...
    def __next__(self) -> bytes: ...

class SagemakerLLM(CustomLLM):
    endpoint_name: str
    temperature: float
    max_new_tokens: int
    context_window: int
    messages_to_prompt: Any
    completion_to_prompt: Any
    generate_kwargs: dict
    model_kwargs: dict
    verbose: bool
    _boto_client: Any

    def __init__(
        self,
        endpoint_name: str = "",
        temperature: float = 0.1,
        max_new_tokens: int = 512,
        context_window: int = 2048,
        messages_to_prompt: Any = None,
        completion_to_prompt: Any = None,
        callback_manager: Any = None,
        generate_kwargs: dict | None = None,
        model_kwargs: dict | None = None,
        verbose: bool = True,
    ) -> None: ...
    @property
    def inference_params(self) -> dict: ...
    @property
    def metadata(self) -> LLMMetadata: ...
    @llm_completion_callback()
    def complete(self, prompt: str, **kwargs: Any) -> CompletionResponse: ...
    @llm_completion_callback()
    def stream_complete(self, prompt: str, **kwargs: Any) -> Any: ...
    @llm_chat_callback()
    def chat(self, messages: Any, **kwargs: Any) -> Any: ...
    @llm_chat_callback()
    def stream_chat(self, messages: Any, **kwargs: Any) -> Any: ...