import asyncio
import os
from typing import List, Optional, Literal
from dotenv import load_dotenv
import aiohttp
from image_generation.core import process_tasks

EVALS: List[str]
OUTPUT_DIR: str

async def generate_and_save_images(
    prompts: List[str],
    model: Literal["dalle3", "flux"],
    api_key: Optional[str],
) -> None: ...

async def main() -> None: ...