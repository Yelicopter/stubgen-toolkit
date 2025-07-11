import abc
from _typeshed import Incomplete
from collections.abc import Sequence
from llama_index.core.llms import ChatMessage
from typing import Any, Literal

logger: Incomplete

class AbstractPromptStyle(abc.ABC, metaclass=abc.ABCMeta):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def messages_to_prompt(self, messages: Sequence[ChatMessage]) -> str: ...
    def completion_to_prompt(self, prompt: str) -> str: ...

class DefaultPromptStyle(AbstractPromptStyle):
    messages_to_prompt: Incomplete
    completion_to_prompt: Incomplete
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class Llama2PromptStyle(AbstractPromptStyle):
    BOS: Incomplete
    EOS: Incomplete
    B_INST: Incomplete
    E_INST: Incomplete
    B_SYS: Incomplete
    E_SYS: Incomplete
    DEFAULT_SYSTEM_PROMPT: str

class Llama3PromptStyle(AbstractPromptStyle):
    BOS: Incomplete
    EOS: Incomplete
    B_INST: Incomplete
    E_INST: Incomplete
    EOT: str
    B_SYS: Incomplete
    E_SYS: Incomplete
    ASSISTANT_INST: str
    DEFAULT_SYSTEM_PROMPT: str

class TagPromptStyle(AbstractPromptStyle): ...
class MistralPromptStyle(AbstractPromptStyle): ...
class ChatMLPromptStyle(AbstractPromptStyle): ...

def get_prompt_style(prompt_style: Literal['default', 'llama2', 'llama3', 'tag', 'mistral', 'chatml'] | None) -> AbstractPromptStyle: ...
