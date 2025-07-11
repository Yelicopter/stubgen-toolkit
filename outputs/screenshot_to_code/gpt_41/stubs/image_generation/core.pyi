from typing import Any, Dict, List, Optional

async def process_tasks(
    prompts: List[str],
    api_key: str,
    base_url: Optional[str],
    model: str,
) -> List[Optional[str]]: ...

async def generate_image_dalle(
    prompt: str, api_key: str, base_url: Optional[str]
) -> Optional[str]: ...

async def generate_image_replicate(prompt: str, api_key: str) -> Optional[str]: ...

def extract_dimensions(url: str) -> tuple[int, int]: ...

def create_alt_url_mapping(code: str) -> Dict[str, str]: ...

async def generate_images(
    code: str,
    api_key: str,
    base_url: Optional[str],
    image_cache: Dict[str, str],
    model: str = ...,
) -> str: ...