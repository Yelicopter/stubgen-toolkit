from typing import Any, Coroutine, List, Optional, Tuple
import asyncio
import os
from datetime import datetime
import time
from llm import Llm
from prompts.types import Stack
from .core import generate_code_for_image
from .utils import image_to_data_url
from .config import EVALS_DIR

async def generate_code_and_time(
    image_url: str,
    stack: Stack,
    model: Llm,
    original_input_filename: str,
    attempt_idx: int,
) -> Tuple[str, int, Optional[str], Optional[float], Optional[Exception]]:
    ...

async def run_image_evals(
    stack: Optional[Stack] = None,
    model: Optional[Llm] = None,
    n: int = 1,
    input_files: Optional[List[str]] = None,
) -> List[str]:
    ...