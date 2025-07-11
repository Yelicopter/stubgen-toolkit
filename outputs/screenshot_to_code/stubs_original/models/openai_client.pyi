from llm import Completion as Completion
from openai.types.chat import ChatCompletionMessageParam as ChatCompletionMessageParam
from typing import Awaitable, Callable, List

async def stream_openai_response(messages: List[ChatCompletionMessageParam], api_key: str, base_url: str | None, callback: Callable[[str], Awaitable[None]], model_name: str) -> Completion: ...
