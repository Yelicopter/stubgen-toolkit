from typing import Any, Awaitable
from prompts.types import Stack

async def generate_code_for_image(
    image_url: str, stack: Stack, model: Any
) -> Any: ...

async def generate_code_core(
    prompt_messages: Any, model: Any
) -> Any: ...