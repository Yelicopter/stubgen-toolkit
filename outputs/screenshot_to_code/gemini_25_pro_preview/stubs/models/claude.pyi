from typing import Any, Awaitable, Callable, Dict, List, Tuple
from openai.types.chat import ChatCompletionMessageParam
from llm import Completion

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
    include_thinking: bool = ...,
    model_name: str = ...,
) -> Completion: ...