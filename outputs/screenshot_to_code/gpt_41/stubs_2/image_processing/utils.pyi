from typing import Tuple

CLAUDE_IMAGE_MAX_SIZE: int
CLAUDE_MAX_IMAGE_DIMENSION: int

def process_image(image_data_url: str) -> Tuple[str, str]: ...