from typing import Awaitable, Callable, Dict, List
from openai.types.chat import ChatCompletionMessageParam
from llm import Completion

def extract_image_from_messages(messages: List[ChatCompletionMessageParam]) -> Dict[str, str]: ...
async def stream_gemini_response(
    messages: List[ChatCompletionMessageParam],
    api_key: str,
    callback: Callable[[str], Awaitable[None]],
    model_name: str,
) -> Completion: ...