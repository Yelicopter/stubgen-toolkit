import time
from typing import Awaitable, Callable, List, Optional
from openai import AsyncOpenAI
from openai.types.chat import ChatCompletionMessageParam, ChatCompletionChunk
from llm import Completion

async def stream_openai_response(
    messages: List[ChatCompletionMessageParam],
    api_key: str,
    base_url: Optional[str],
    callback: Callable[[str], Awaitable[None]],
    model_name: str,
) -> Completion: ...