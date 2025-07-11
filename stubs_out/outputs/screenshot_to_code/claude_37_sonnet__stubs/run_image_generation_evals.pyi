from dotenv import load_dotenv as load_dotenv
from image_generation.core import process_tasks as process_tasks
from typing import List, Literal, Optional

EVALS: List[str]
OUTPUT_DIR: str

async def generate_and_save_images(prompts: List[str], model: Literal['dalle3', 'flux'], api_key: Optional[str]) -> None: ...
async def main() -> None: ...
