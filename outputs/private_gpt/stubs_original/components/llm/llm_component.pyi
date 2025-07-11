from _typeshed import Incomplete
from collections.abc import Callable as Callable
from llama_index.core.llms import LLM as LLM
from private_gpt.components.llm.prompt_helper import get_prompt_style as get_prompt_style
from private_gpt.paths import models_cache_path as models_cache_path, models_path as models_path
from private_gpt.settings.settings import Settings as Settings

logger: Incomplete

class LLMComponent:
    llm: LLM
    def __init__(self, settings: Settings) -> None: ...
