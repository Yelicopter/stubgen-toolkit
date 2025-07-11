from llama_index.core.llms import LLM as LLM
from private_gpt.settings.settings import Settings as Settings

class LLMComponent:
    llm: LLM
    def __init__(self, settings: Settings) -> None: ...
