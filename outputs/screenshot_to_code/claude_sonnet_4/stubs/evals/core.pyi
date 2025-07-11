from typing import List
from llm import Llm
from prompts.types import Stack
from openai.types.chat import ChatCompletionMessageParam

async def generate_code_for_image(image_url: str, stack: Stack, model: Llm) -> str: ...
async def generate_code_core(prompt_messages: List[ChatCompletionMessageParam], model: Llm) -> str: ...