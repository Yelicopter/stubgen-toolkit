from _typeshed import Incomplete
from enum import Enum
from typing import TypedDict

class Llm(Enum):
    GPT_4_VISION: str
    GPT_4_TURBO_2024_04_09: str
    GPT_4O_2024_05_13: str
    GPT_4O_2024_08_06: str
    GPT_4O_2024_11_20: str
    GPT_4_1_2025_04_14: str
    GPT_4_1_MINI_2025_04_14: str
    GPT_4_1_NANO_2025_04_14: str
    CLAUDE_3_SONNET: str
    CLAUDE_3_OPUS: str
    CLAUDE_3_HAIKU: str
    CLAUDE_3_5_SONNET_2024_06_20: str
    CLAUDE_3_5_SONNET_2024_10_22: str
    CLAUDE_3_7_SONNET_2025_02_19: str
    CLAUDE_4_SONNET_2025_05_14: str
    CLAUDE_4_OPUS_2025_05_14: str
    GEMINI_2_0_FLASH_EXP: str
    GEMINI_2_0_FLASH: str
    GEMINI_2_0_PRO_EXP: str
    GEMINI_2_5_FLASH_PREVIEW_05_20: str
    O1_2024_12_17: str
    O4_MINI_2025_04_16: str
    O3_2025_04_16: str

class Completion(TypedDict): ...

MODEL_PROVIDER: Incomplete
OPENAI_MODELS: Incomplete
ANTHROPIC_MODELS: Incomplete
GEMINI_MODELS: Incomplete
