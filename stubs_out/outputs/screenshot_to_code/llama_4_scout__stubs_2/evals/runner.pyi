from .config import EVALS_DIR as EVALS_DIR
from .core import generate_code_for_image as generate_code_for_image
from .utils import image_to_data_url as image_to_data_url
from datetime import datetime as datetime
from llm import Llm
from prompts.types import Stack as Stack
from typing import List, Optional, Tuple

async def generate_code_and_time(image_url: str, stack: Stack, model: Llm, original_input_filename: str, attempt_idx: int) -> Tuple[str, int, Optional[str], Optional[float], Optional[Exception]]: ...
async def run_image_evals(stack: Optional[Stack] = ..., model: Optional[Llm] = ..., n: int = ..., input_files: Optional[List[str]] = ...) -> List[str]: ...
