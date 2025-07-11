from anthropic import AsyncAnthropic as AsyncAnthropic
from config import IS_DEBUG_ENABLED as IS_DEBUG_ENABLED
from debug.DebugFileWriter import DebugFileWriter as DebugFileWriter
from image_processing.utils import process_image as process_image
from llm import Completion as Completion, Llm as Llm
from openai.types.chat import ChatCompletionMessageParam as ChatCompletionMessageParam
from typing import Any, Awaitable, Callable, Dict, List, Tuple
from utils import pprint_prompt as pprint_prompt

def convert_openai_messages_to_claude(messages: List[ChatCompletionMessageParam]) -> Tuple[str, List[Dict[str, Any]]]: ...
async def stream_claude_response(messages: List[ChatCompletionMessageParam], api_key: str, callback: Callable[[str], Awaitable[None]], model_name: str) -> Completion: ...
async def stream_claude_response_native(system_prompt: str, messages: List[Dict[str, Any]], api_key: str, callback: Callable[[str], Awaitable[None]], include_thinking: bool = ..., model_name: str = ...) -> Completion: ...
