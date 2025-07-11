from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Awaitable, Callable, Dict, List, Literal, Optional, Tuple
from fastapi import APIRouter, WebSocket
from custom_types import InputMode
from llm import Completion, Llm
from prompts.types import PromptContent, Stack
from openai.types.chat import ChatCompletionMessageParam

router: APIRouter
MessageType = Literal[
    "chunk",
    "status",
    "setCode",
    "error",
    "variantComplete",
    "variantError",
    "variantCount",
]

class VariantErrorAlreadySent(Exception):
    original_error: Exception
    def __init__(self, original_error: Exception) -> None: ...

@dataclass
class PipelineContext:
    websocket: WebSocket
    ws_comm: Optional[WebSocketCommunicator] = ...
    params: Dict[str, Any] = ...
    extracted_params: Optional[ExtractedParams] = ...
    prompt_messages: List[ChatCompletionMessageParam] = ...
    image_cache: Dict[str, str] = ...
    variant_models: List[Llm] = ...
    completions: List[str] = ...
    variant_completions: Dict[int, str] = ...
    metadata: Dict[str, Any] = ...
    @property
    def send_message(self) -> Callable[[MessageType, Any, int], Awaitable[None]]: ...
    @property
    def throw_error(self) -> Callable[[str], Awaitable[None]]: ...

class Middleware(ABC):
    @abstractmethod
    async def process(self, context: PipelineContext, next_func: Callable[[], Awaitable[None]]) -> None: ...

class Pipeline:
    middlewares: List[Middleware]
    def __init__(self) -> None: ...
    def use(self, middleware: Middleware) -> Pipeline: ...
    async def execute(self, websocket: WebSocket) -> None: ...
    def _wrap_middleware(
        self, middleware: Middleware, next_func: Callable[[PipelineContext], Awaitable[None]]
    ) -> Callable[[PipelineContext], Awaitable[None]]: ...

class WebSocketCommunicator:
    websocket: WebSocket
    is_closed: bool
    def __init__(self, websocket: WebSocket) -> None: ...
    async def accept(self) -> None: ...
    async def send_message(self, type: MessageType, value: Any, variantIndex: int) -> None: ...
    async def throw_error(self, message: str) -> None: ...
    async def receive_params(self) -> Dict[str, Any]: ...
    async def close(self) -> None: ...

@dataclass
class ExtractedParams:
    stack: Stack
    input_mode: InputMode
    should_generate_images: bool
    openai_api_key: Optional[str]
    anthropic_api_key: Optional[str]
    openai_base_url: Optional[str]
    generation_type: Literal["create", "update"]
    prompt: PromptContent
    history: List[Dict[str, Any]]
    is_imported_from_code: bool

class ParameterExtractionStage:
    throw_error: Callable[[str], Awaitable[None]]
    def __init__(self, throw_error: Callable[[str], Awaitable[None]]) -> None: ...
    async def extract_and_validate(self, params: Dict[str, Any]) -> ExtractedParams: ...
    def _get_from_settings_dialog_or_env(
        self, params: Dict[str, Any], key: str, env_var: Optional[str]
    ) -> Optional[str]: ...

class ModelSelectionStage:
    throw_error: Callable[[str], Awaitable[None]]
    def __init__(self, throw_error: Callable[[str], Awaitable[None]]) -> None: ...
    async def select_models(
        self,
        generation_type: Literal["create", "update"],
        input_mode: InputMode,
        openai_api_key: Optional[str],
        anthropic_api_key: Optional[str],
        gemini_api_key: Optional[str] = ...,
    ) -> List[Llm]: ...
    def _get_variant_models(
        self,
        generation_type: Literal["create", "update"],
        input_mode: InputMode,
        num_variants: int,
        openai_api_key: Optional[str],
        anthropic_api_key: Optional[str],
        gemini_api_key: Optional[str],
    ) -> List[Llm]: ...

class PromptCreationStage:
    throw_error: Callable[[str], Awaitable[None]]
    def __init__(self, throw_error: Callable[[str], Awaitable[None]]) -> None: ...
    async def create_prompt(
        self, extracted_params: ExtractedParams
    ) -> Tuple[List[ChatCompletionMessageParam], Dict[str, str]]: ...

class MockResponseStage:
    send_message: Callable[[MessageType, Any, int], Awaitable[None]]
    def __init__(self, send_message: Callable[[MessageType, Any, int], Awaitable[None]]) -> None: ...
    async def generate_mock_response(self, input_mode: InputMode) -> List[str]: ...

class VideoGenerationStage:
    send_message: Callable[[MessageType, Any, int], Awaitable[None]]
    throw_error: Callable[[str], Awaitable[None]]
    def __init__(
        self,
        send_message: Callable[[MessageType, Any, int], Awaitable[None]],
        throw_error: Callable[[str], Awaitable[None]],
    ) -> None: ...
    async def generate_video_code(
        self, prompt_messages: List[ChatCompletionMessageParam], anthropic_api_key: Optional[str]
    ) -> List[str]: ...

class PostProcessingStage:
    def __init__(self) -> None: ...
    async def process_completions(
        self, completions: List[str], prompt_messages: List[ChatCompletionMessageParam], websocket: WebSocket
    ) -> None: ...

class ParallelGenerationStage:
    send_message: Callable[[MessageType, Any, int], Awaitable[None]]
    openai_api_key: Optional[str]
    openai_base_url: Optional[str]
    anthropic_api_key: Optional[str]
    should_generate_images: bool
    def __init__(
        self,
        send_message: Callable[[MessageType, Any, int], Awaitable[None]],
        openai_api_key: Optional[str],
        openai_base_url: Optional[str],
        anthropic_api_key: Optional[str],
        should_generate_images: bool,
    ) -> None: ...
    async def process_variants(
        self,
        variant_models: List[Llm],
        prompt_messages: List[ChatCompletionMessageParam],
        image_cache: Dict[str, str],
        params: Dict[str, Any],
    ) -> Dict[int, str]: ...
    def _create_generation_tasks(
        self,
        variant_models: List[Llm],
        prompt_messages: List[ChatCompletionMessageParam],
        params: Dict[str, Any],
    ) -> List[Awaitable[Completion]]: ...
    async def _process_chunk(self, content: str, variant_index: int) -> None: ...
    async def _stream_openai_with_error_handling(
        self, prompt_messages: List[ChatCompletionMessageParam], model_name: str, index: int
    ) -> Completion: ...
    async def _perform_image_generation(self, completion: str, image_cache: Dict[str, str]) -> str: ...
    async def _process_variant_completion(
        self,
        index: int,
        task: Awaitable[Completion],
        model: Llm,
        image_cache: Dict[str, str],
        variant_completions: Dict[int, str],
    ) -> None: ...

class WebSocketSetupMiddleware(Middleware):
    async def process(self, context: PipelineContext, next_func: Callable[[], Awaitable[None]]) -> None: ...

class ParameterExtractionMiddleware(Middleware):
    async def process(self, context: PipelineContext, next_func: Callable[[], Awaitable[None]]) -> None: ...

class StatusBroadcastMiddleware(Middleware):
    async def process(self, context: PipelineContext, next_func: Callable[[], Awaitable[None]]) -> None: ...

class PromptCreationMiddleware(Middleware):
    async def process(self, context: PipelineContext, next_func: Callable[[], Awaitable[None]]) -> None: ...

class CodeGenerationMiddleware(Middleware):
    async def process(self, context: PipelineContext, next_func: Callable[[], Awaitable[None]]) -> None: ...

class PostProcessingMiddleware(Middleware):
    async def process(self, context: PipelineContext, next_func: Callable[[], Awaitable[None]]) -> None: ...

async def stream_code(websocket: WebSocket) -> None: ...