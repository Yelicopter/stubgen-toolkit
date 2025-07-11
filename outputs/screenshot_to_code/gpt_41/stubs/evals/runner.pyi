from typing import Any, Coroutine, List, Optional
from llm import Llm
from prompts.types import Stack

async def generate_code_and_time(
    image_url: str,
    stack: Stack,
    model: Llm,
    original_input_filename: str,
    attempt_idx: int,
) -> tuple[str, int, Optional[str], Optional[float], Optional[Exception]]: ...

async def run_image_evals(
    stack: Stack = ...,
    model: Llm = ...,
    n: int = ...,
    input_files: Optional[list[str]] = ...,
) -> list[str]: ...