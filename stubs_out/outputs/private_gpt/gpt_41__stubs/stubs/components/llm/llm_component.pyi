from collections.abc import Callable as Callable
from llama_index.core.llms import LLM as LLM, MockLLM as MockLLM
from llama_index.core.utils import set_global_tokenizer as set_global_tokenizer
from private_gpt.components.llm.prompt_helper import get_prompt_style as get_prompt_style
from private_gpt.paths import models_cache_path as models_cache_path, models_path as models_path
from private_gpt.settings.settings import Settings as Settings
from transformers import AutoTokenizer as AutoTokenizer

class LLMComponent:
    llm: LLM
    def __init__(self, settings: Settings) -> None: ...
