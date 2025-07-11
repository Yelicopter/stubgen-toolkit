from llm import Llm
from openai.types.chat import ChatCompletionMessageParam as ChatCompletionMessageParam
from prompts.types import Stack as Stack
from typing import List

async def generate_code_for_image(image_url: str, stack: Stack, model: Llm) -> str: ...
async def generate_code_core(prompt_messages: List[ChatCompletionMessageParam], model: Llm) -> str: ...
