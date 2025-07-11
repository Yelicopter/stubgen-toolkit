from typing import Any, Coroutine, List, Optional, Tuple
from llm import Llm
from prompts.types import Stack

async def generate_code_and_time(
    image_url: str,
    stack: Stack,
    model: Llm,
    original_input_filename: str,
    attempt_idx: int,
) -> Tuple[str, int, Optional[str], Optional[float], Optional[Exception]]: ...

async def run_image_evals(
    stack: Optional[Stack] = None,
    model: Optional[str] = None,
    n: int = 1,
    input_files: Optional[List[str]] = None
) -> List[str]: ...