import copy
import time
from typing import Any, Awaitable, Callable, Dict, List, Tuple, cast, Optional
from anthropic import AsyncAnthropic
from openai.types.chat import ChatCompletionMessageParam
from config import IS_DEBUG_ENABLED
from debug.DebugFileWriter import DebugFileWriter
from image_processing.utils import process_image
from utils import pprint_prompt
from llm import Completion, Llm

def convert_openai_messages_to_claude(
    messages: List[ChatCompletionMessageParam],
) -> Tuple[str, List[Dict[str, Any]]]: ...

async def stream_claude_response(
    messages: List[ChatCompletionMessageParam],
    api_key: str,
    callback: Callable[[str], Awaitable[None]],
    model_name: str,
) -> Completion: ...

async def stream_claude_response_native(
    system_prompt: str,
    messages: List[Dict[str, Any]],
    api_key: str,
    callback: Callable[[str], Awaitable[None]],
    include_thinking: bool = False,
    model_name: str = "claude-3-7-sonnet-20250219",
) -> Completion: ...