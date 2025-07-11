from injector import inject, singleton
from llama_index.core.llms import LLM, MockLLM
from private_gpt.settings.settings import Settings

@singleton
class LLMComponent:
    @inject
    def __init__(self, settings: Settings) -> None:
        ...

    def get_llm(self) -> LLM:
        ...