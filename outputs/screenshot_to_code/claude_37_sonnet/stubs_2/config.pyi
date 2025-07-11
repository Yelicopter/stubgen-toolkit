from typing import Optional, Union, Literal, Any
import os

NUM_VARIANTS: int

OPENAI_API_KEY: Optional[str]
ANTHROPIC_API_KEY: Optional[str]
GEMINI_API_KEY: Optional[str]
OPENAI_BASE_URL: Optional[str]

REPLICATE_API_KEY: Optional[str]

SHOULD_MOCK_AI_RESPONSE: bool
IS_DEBUG_ENABLED: bool
DEBUG_DIR: str

IS_PROD: Union[bool, str, Any]