from config import ANTHROPIC_API_KEY as ANTHROPIC_API_KEY, GEMINI_API_KEY as GEMINI_API_KEY, OPENAI_API_KEY as OPENAI_API_KEY
from llm import ANTHROPIC_MODELS as ANTHROPIC_MODELS, GEMINI_MODELS as GEMINI_MODELS, Llm
from models import stream_claude_response as stream_claude_response, stream_gemini_response as stream_gemini_response, stream_openai_response as stream_openai_response
from openai.types.chat import ChatCompletionMessageParam as ChatCompletionMessageParam
from prompts import assemble_prompt as assemble_prompt
from prompts.types import Stack as Stack

async def generate_code_for_image(image_url: str, stack: Stack, model: Llm) -> str: ...
async def generate_code_core(prompt_messages: list[ChatCompletionMessageParam], model: Llm) -> str: ...
