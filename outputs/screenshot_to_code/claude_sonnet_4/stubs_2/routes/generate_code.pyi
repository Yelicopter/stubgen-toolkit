from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import Callable, Awaitable, Any, Dict, List, Literal, Optional
from fastapi import APIRouter, WebSocket
from custom_types import InputMode
from llm import Llm, Completion
from openai.types.chat import ChatCompletionMessageParam
from prompts.types import Stack, PromptContent

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
    ws_comm: Optional["WebSocketCommunicator"] = None
    params: Dict[str, Any] = field(default_factory=dict)
    extracted_params: Optional["ExtractedParams"] = None
    prompt_messages: List[ChatCompletionMessageParam] = field(default_factory=list)
    image_cache: Dict[str, str] = field(default_factory=dict)
    variant_models: List[Llm] = field(default_factory=list)
    completions: List[str] = field(default_factory=list)
    variant_completions: Dict[int, str] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)

    @property
    def send_message(self) -> Callable[[MessageType, str, int], Awaitable[None]]: ...
    @property
    def throw_error(self) -> Callable[[str], Awaitable[None]]: ...

class Middleware(ABC):
    @abstractmethod
    async def process(
        self, context: PipelineContext, next_func: Callable[[], Awaitable[None]]
    ) -> None: ...

class Pipeline:
    middlewares: List[Middleware]
    
    def __init__(self) -> None: ...
    def use(self, middleware: Middleware) -> "Pipeline": ...
    async def execute(self, websocket: WebSocket) -> None: ...

class WebSocketCommunicator:
    websocket: WebSocket
    is_closed: bool
    
    def __init__(self, websocket: WebSocket) -> None: ...
    async def accept(self) -> None: ...
    async def send_message(self, type: MessageType, value: str, variantIndex: int) -> None: ...
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
    def __init__(self, throw_error: Callable[[str], Awaitable[None]]) -> None: ...
    async def extract_and_validate(self, params: Dict[str, Any]) -> ExtractedParams: ...

class ModelSelectionStage:
    def __init__(self, throw_error: Callable[[str], Awaitable[None]]) -> None: ...
    async def select_models(
        self,
        generation_type: Literal["create", "update"],
        input_mode: InputMode,
        openai_api_key: Optional[str],
        anthropic_api_key: Optional[str],
        gemini_api_key: Optional[str] = None,
    ) -> List[Llm]: ...

class PromptCreationStage:
    def __init__(self, throw_error: Callable[[str], Awaitable[None]]) -> None: ...
    async def create_prompt(
        self, extracted_params: ExtractedParams,
    ) -> tuple[List[ChatCompletionMessageParam], Dict[str, str]]: ...

class MockResponseStage:
    def __init__(self, send_message: Callable[[MessageType, str, int], Awaitable[None]]) -> None: ...
    async def generate_mock_response(self, input_mode: InputMode) -> List[str]: ...

class VideoGenerationStage:
    def __init__(
        self,
        send_message: Callable[[MessageType, str, int], Awaitable[None]],
        throw_error: Callable[[str], Awaitable[None]],
    ) -> None: ...
    async def generate_video_code(
        self,
        prompt_messages: List[ChatCompletionMessageParam],
        anthropic_api_key: Optional[str],
    ) -> List[str]: ...

class PostProcessingStage:
    def __init__(self) -> None: ...
    async def process_completions(
        self,
        completions: List[str],
        prompt_messages: List[ChatCompletionMessageParam],
        websocket: WebSocket,
    ) -> None: ...

class ParallelGenerationStage:
    def __init__(
        self,
        send_message: Callable[[MessageType, str, int], Awaitable[None]],
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

class WebSocketSetupMiddleware(Middleware):
    async def process(
        self, context: PipelineContext, next_func: Callable[[], Awaitable[None]]
    ) -> None: ...

class ParameterExtractionMiddleware(Middleware):
    async def process(
        self, context: PipelineContext, next_func: Callable[[], Awaitable[None]]
    ) -> None: ...

class StatusBroadcastMiddleware(Middleware):
    async def process(
        self, context: PipelineContext, next_func: Callable[[], Awaitable[None]]
    ) -> None: ...

class PromptCreationMiddleware(Middleware):
    async def process(
        self, context: PipelineContext, next_func: Callable[[], Awaitable[None]]
    ) -> None: ...

class CodeGenerationMiddleware(Middleware):
    async def process(
        self, context: PipelineContext, next_func: Callable[[], Awaitable[None]]
    ) -> None: ...

class PostProcessingMiddleware(Middleware):
    async def process(
        self, context: PipelineContext, next_func: Callable[[], Awaitable[None]]
    ) -> None: ...

async def stream_code(websocket: WebSocket) -> None: ...