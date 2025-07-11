from config import ANTHROPIC_API_KEY, GEMINI_API_KEY, OPENAI_API_KEY
from llm import Llm, ANTHROPIC_MODELS, GEMINI_MODELS
from models import (
    stream_claude_response,
    stream_gemini_response,
    stream_openai_response,
)
from prompts import assemble_prompt
from prompts.types import Stack
from openai.types.chat import ChatCompletionMessageParam

async def generate_code_for_image(
    image_url: str, stack: Stack, model: Llm
) -> str:
    ...

async def generate_code_core(
    prompt_messages: list[ChatCompletionMessageParam], model: Llm
) -> str:
    ...