from llm import Completion as Completion
from openai.types.chat import ChatCompletionMessageParam as ChatCompletionMessageParam
from typing import Awaitable, Callable, List, Optional

async def stream_openai_response(messages: List[ChatCompletionMessageParam], api_key: str, base_url: Optional[str], callback: Callable[[str], Awaitable[None]], model_name: str) -> Completion: ...
