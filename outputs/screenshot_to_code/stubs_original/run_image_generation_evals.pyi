from _typeshed import Incomplete
from typing import List, Literal, Optional

EVALS: Incomplete
OPENAI_API_KEY: Optional[str]
REPLICATE_API_TOKEN: Optional[str]
OUTPUT_DIR: str

async def generate_and_save_images(prompts: List[str], model: Literal['dalle3', 'flux'], api_key: Optional[str]) -> None: ...
async def main() -> None: ...
