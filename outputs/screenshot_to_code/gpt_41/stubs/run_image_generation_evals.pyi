import asyncio
from typing import List

EVALS: List[str]
OUTPUT_DIR: str

async def generate_and_save_images(
    prompts: List[str],
    model: str,
    api_key: str,
) -> None: ...

async def main() -> None: ...