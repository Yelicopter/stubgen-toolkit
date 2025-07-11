import base64
import time
from typing import Awaitable, Callable, Dict, List, Optional, Any
from openai.types.chat import ChatCompletionMessageParam
from google import genai
from google.genai import types
from llm import Completion, Llm

def extract_image_from_messages(
    messages: List[ChatCompletionMessageParam],
) -> Dict[str, Any]: ...

async def stream_gemini_response(
    messages: List[ChatCompletionMessageParam],
    api_key: str,
    callback: Callable[[str], Awaitable[None]],
    model_name: str,
) -> Completion: ...