import abc
from collections.abc import Sequence
from llama_index.core.llms import ChatMessage as ChatMessage
from typing import Any, Callable, Literal

class AbstractPromptStyle(abc.ABC, metaclass=abc.ABCMeta):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def messages_to_prompt(self, messages: Sequence[ChatMessage]) -> str: ...
    def completion_to_prompt(self, prompt: str) -> str: ...

class DefaultPromptStyle(AbstractPromptStyle):
    messages_to_prompt: Callable[[Sequence[ChatMessage]], str] | None
    completion_to_prompt: Callable[[str], str] | None
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class Llama2PromptStyle(AbstractPromptStyle):
    BOS: str
    EOS: str
    B_INST: str
    E_INST: str
    B_SYS: str
    E_SYS: str
    DEFAULT_SYSTEM_PROMPT: str

class Llama3PromptStyle(AbstractPromptStyle):
    BOS: str
    EOS: str
    B_INST: str
    E_INST: str
    EOT: str
    B_SYS: str
    E_SYS: str
    ASSISTANT_INST: str
    DEFAULT_SYSTEM_PROMPT: str

class TagPromptStyle(AbstractPromptStyle): ...
class MistralPromptStyle(AbstractPromptStyle): ...
class ChatMLPromptStyle(AbstractPromptStyle): ...

def get_prompt_style(prompt_style: Literal['default', 'llama2', 'llama3', 'tag', 'mistral', 'chatml'] | None) -> AbstractPromptStyle: ...
