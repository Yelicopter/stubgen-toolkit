from google import genai as genai
from google.genai import types as types
from llm import Completion as Completion, Llm as Llm
from openai.types.chat import ChatCompletionMessageParam as ChatCompletionMessageParam
from typing import Any, Awaitable, Callable, Dict, List

def extract_image_from_messages(messages: List[ChatCompletionMessageParam]) -> Dict[str, Any]: ...
async def stream_gemini_response(messages: List[ChatCompletionMessageParam], api_key: str, callback: Callable[[str], Awaitable[None]], model_name: str) -> Completion: ...
