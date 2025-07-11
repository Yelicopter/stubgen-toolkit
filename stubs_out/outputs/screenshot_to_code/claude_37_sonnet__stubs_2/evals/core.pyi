from config import ANTHROPIC_API_KEY as ANTHROPIC_API_KEY, GEMINI_API_KEY as GEMINI_API_KEY, OPENAI_API_KEY as OPENAI_API_KEY
from llm import Llm
from openai.types.chat import ChatCompletionMessageParam as ChatCompletionMessageParam
from prompts.types import Stack as Stack
from typing import List

async def generate_code_for_image(image_url: str, stack: Stack, model: Llm) -> str: ...
async def generate_code_core(prompt_messages: List[ChatCompletionMessageParam], model: Llm) -> str: ...
