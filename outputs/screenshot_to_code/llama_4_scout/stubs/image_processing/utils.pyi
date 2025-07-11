import base64
import io
import time
from PIL import Image

CLAUDE_IMAGE_MAX_SIZE = 5 * 1024 * 1024
CLAUDE_MAX_IMAGE_DIMENSION = 7990

def process_image(image_data_url: str) -> tuple[str, str]:
    ...