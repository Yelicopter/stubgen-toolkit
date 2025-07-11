from custom_types import InputMode as InputMode
from llm import Completion as Completion
from typing import Awaitable, Callable

STREAM_CHUNK_SIZE: int

async def mock_completion(process_chunk: Callable[[str, int], Awaitable[None]], input_mode: InputMode) -> Completion: ...

APPLE_MOCK_CODE: str
NYTIMES_MOCK_CODE: str
NO_IMAGES_NYTIMES_MOCK_CODE: str
MORTGAGE_CALCULATOR_VIDEO_PROMPT_MOCK: str
GOOGLE_FORM_VIDEO_PROMPT_MOCK: str
TALLY_FORM_VIDEO_PROMPT_MOCK: str
