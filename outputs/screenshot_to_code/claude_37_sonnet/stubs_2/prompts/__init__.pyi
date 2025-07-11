from typing import Union, Any, cast, List, Dict, Tuple
from openai.types.chat import ChatCompletionMessageParam, ChatCompletionContentPartParam

from custom_types import InputMode
from image_generation.core import create_alt_url_mapping
from prompts.imported_code_prompts import IMPORTED_CODE_SYSTEM_PROMPTS
from prompts.screenshot_system_prompts import SYSTEM_PROMPTS
from prompts.text_prompts import SYSTEM_PROMPTS as TEXT_SYSTEM_PROMPTS
from prompts.types import Stack, PromptContent

USER_PROMPT: str
SVG_USER_PROMPT: str

async def create_prompt(
    stack: Stack,
    input_mode: InputMode,
    generation_type: str,
    prompt: Any,
    history: List[Dict[str, Any]],
    is_imported_from_code: bool,
) -> Tuple[List[ChatCompletionMessageParam], Dict[str, str]]: ...

def create_message_from_history_item(
    item: Dict[str, Any], role: str
) -> ChatCompletionMessageParam: ...

def assemble_imported_code_prompt(
    code: str, stack: Stack
) -> List[ChatCompletionMessageParam]: ...

def assemble_prompt(
    image_data_url: str,
    stack: Stack,
) -> List[ChatCompletionMessageParam]: ...

def assemble_text_prompt(
    text_prompt: str,
    stack: Stack,
) -> List[ChatCompletionMessageParam]: ...