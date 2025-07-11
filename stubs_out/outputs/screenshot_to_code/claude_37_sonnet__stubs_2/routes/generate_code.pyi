import abc
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from codegen.utils import extract_html_content as extract_html_content
from config import ANTHROPIC_API_KEY as ANTHROPIC_API_KEY, GEMINI_API_KEY as GEMINI_API_KEY, IS_PROD as IS_PROD, NUM_VARIANTS as NUM_VARIANTS, OPENAI_API_KEY as OPENAI_API_KEY, OPENAI_BASE_URL as OPENAI_BASE_URL, REPLICATE_API_KEY as REPLICATE_API_KEY, SHOULD_MOCK_AI_RESPONSE as SHOULD_MOCK_AI_RESPONSE
from custom_types import InputMode as InputMode
from fastapi import APIRouter as APIRouter, WebSocket as WebSocket
from fs_logging.core import write_logs as write_logs
from image_generation.core import generate_images as generate_images
from llm import ANTHROPIC_MODELS as ANTHROPIC_MODELS, Completion as Completion, GEMINI_MODELS as GEMINI_MODELS, Llm, OPENAI_MODELS as OPENAI_MODELS
from mock_llm import mock_completion as mock_completion
from models.claude import stream_claude_response as stream_claude_response, stream_claude_response_native as stream_claude_response_native
from models.gemini import stream_gemini_response as stream_gemini_response
from models.openai_client import stream_openai_response as stream_openai_response
from openai.types.chat import ChatCompletionMessageParam as ChatCompletionMessageParam
from prompts import create_prompt as create_prompt
from prompts.claude_prompts import VIDEO_PROMPT as VIDEO_PROMPT
from prompts.types import PromptContent as PromptContent, Stack as Stack
from typing import Any, Awaitable, Callable, Dict, List, Literal, Optional, Tuple
from utils import print_prompt_summary as print_prompt_summary
from ws.constants import APP_ERROR_WEB_SOCKET_CODE as APP_ERROR_WEB_SOCKET_CODE

MessageType: Incomplete
router: APIRouter

class VariantErrorAlreadySent(Exception):
    original_error: Exception
    def __init__(self, original_error: Exception) -> None: ...

class PipelineContext:
    websocket: WebSocket
    ws_comm: Optional[Any]
    params: Dict[str, Any]
    extracted_params: Optional[Any]
    prompt_messages: List[ChatCompletionMessageParam]
    image_cache: Dict[str, str]
    variant_models: List[Llm]
    completions: List[str]
    variant_completions: Dict[int, str]
    metadata: Dict[str, Any]
    @property
    def send_message(self) -> Callable[[MessageType, Any, int], Awaitable[None]]: ...
    @property
    def throw_error(self) -> Callable[[str], Awaitable[None]]: ...
    def __init__(self, websocket, ws_comm, params, extracted_params, prompt_messages, image_cache, variant_models, completions, variant_completions, metadata) -> None: ...

class Middleware(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    async def process(self, context: PipelineContext, next_func: Callable[[], Awaitable[None]]) -> None: ...

class Pipeline:
    middlewares: List[Middleware]
    def __init__(self) -> None: ...
    def use(self, middleware: Middleware) -> Pipeline: ...
    async def execute(self, websocket: WebSocket) -> None: ...

class WebSocketCommunicator:
    websocket: WebSocket
    is_closed: bool
    def __init__(self, websocket: WebSocket) -> None: ...
    async def accept(self) -> None: ...
    async def send_message(self, type: MessageType, value: Any, variantIndex: int) -> None: ...
    async def throw_error(self, message: str) -> None: ...
    async def receive_params(self) -> Dict[str, Any]: ...
    async def close(self) -> None: ...

class ExtractedParams:
    stack: Stack
    input_mode: InputMode
    should_generate_images: bool
    openai_api_key: Optional[str]
    anthropic_api_key: Optional[str]
    openai_base_url: Optional[str]
    generation_type: Literal['create', 'update']
    prompt: PromptContent
    history: List[Dict[str, Any]]
    is_imported_from_code: bool
    def __init__(self, stack, input_mode, should_generate_images, openai_api_key, anthropic_api_key, openai_base_url, generation_type, prompt, history, is_imported_from_code) -> None: ...

class ParameterExtractionStage:
    throw_error: Callable[[str], Awaitable[None]]
    def __init__(self, throw_error: Callable[[str], Awaitable[None]]) -> None: ...
    async def extract_and_validate(self, params: Dict[str, Any]) -> ExtractedParams: ...

class ModelSelectionStage:
    throw_error: Callable[[str], Awaitable[None]]
    def __init__(self, throw_error: Callable[[str], Awaitable[None]]) -> None: ...
    async def select_models(self, generation_type: Literal['create', 'update'], input_mode: InputMode, openai_api_key: Optional[str], anthropic_api_key: Optional[str], gemini_api_key: Optional[str] = ...) -> List[Llm]: ...

class PromptCreationStage:
    throw_error: Callable[[str], Awaitable[None]]
    def __init__(self, throw_error: Callable[[str], Awaitable[None]]) -> None: ...
    async def create_prompt(self, extracted_params: ExtractedParams) -> Tuple[List[ChatCompletionMessageParam], Dict[str, str]]: ...

class MockResponseStage:
    send_message: Callable[[MessageType, Any, int], Awaitable[None]]
    def __init__(self, send_message: Callable[[MessageType, Any, int], Awaitable[None]]) -> None: ...
    async def generate_mock_response(self, input_mode: InputMode) -> List[str]: ...

class VideoGenerationStage:
    send_message: Callable[[MessageType, Any, int], Awaitable[None]]
    throw_error: Callable[[str], Awaitable[None]]
    def __init__(self, send_message: Callable[[MessageType, Any, int], Awaitable[None]], throw_error: Callable[[str], Awaitable[None]]) -> None: ...
    async def generate_video_code(self, prompt_messages: List[ChatCompletionMessageParam], anthropic_api_key: Optional[str]) -> List[str]: ...

class PostProcessingStage:
    def __init__(self) -> None: ...
    async def process_completions(self, completions: List[str], prompt_messages: List[ChatCompletionMessageParam], websocket: WebSocket) -> None: ...

class ParallelGenerationStage:
    send_message: Callable[[MessageType, Any, int], Awaitable[None]]
    openai_api_key: Optional[str]
    openai_base_url: Optional[str]
    anthropic_api_key: Optional[str]
    should_generate_images: bool
    def __init__(self, send_message: Callable[[MessageType, Any, int], Awaitable[None]], openai_api_key: Optional[str], openai_base_url: Optional[str], anthropic_api_key: Optional[str], should_generate_images: bool) -> None: ...
    async def process_variants(self, variant_models: List[Llm], prompt_messages: List[ChatCompletionMessageParam], image_cache: Dict[str, str], params: Dict[str, Any]) -> Dict[int, str]: ...

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
