import abc
from collections.abc import Sequence
from typing import Any, Callable, Literal

from llama_index.core.llms import ChatMessage

class AbstractPromptStyle(abc.ABC):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @abc.abstractmethod
    def _messages_to_prompt(self, messages: Sequence[ChatMessage]) -> str: ...
    @abc.abstractmethod
    def _completion_to_prompt(self, completion: str) -> str: ...
    def messages_to_prompt(self, messages: Sequence[ChatMessage]) -> str: ...
    def completion_to_prompt(self, prompt: str) -> str: ...

class DefaultPromptStyle(AbstractPromptStyle):
    messages_to_prompt: Callable[[Sequence[ChatMessage]], str] | None
    completion_to_prompt: Callable[[str], str] | None
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def _messages_to_prompt(self, messages: Sequence[ChatMessage]) -> str: ...
    def _completion_to_prompt(self, completion: str) -> str: ...

class Llama2PromptStyle(AbstractPromptStyle):
    BOS: str
    EOS: str
    B_INST: str
    E_INST: str
    B_SYS: str
    E_SYS: str
    DEFAULT_SYSTEM_PROMPT: str
    def _messages_to_prompt(self, messages: Sequence[ChatMessage]) -> str: ...
    def _completion_to_prompt(self, completion: str) -> str: ...

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
    def _messages_to_prompt(self, messages: Sequence[ChatMessage]) -> str: ...
    def _completion_to_prompt(self, completion: str) -> str: ...

class TagPromptStyle(AbstractPromptStyle):
    def _messages_to_prompt(self, messages: Sequence[ChatMessage]) -> str: ...
    def _completion_to_prompt(self, completion: str) -> str: ...

class MistralPromptStyle(AbstractPromptStyle):
    def _messages_to_prompt(self, messages: Sequence[ChatMessage]) -> str: ...
    def _completion_to_prompt(self, completion: str) -> str: ...

class ChatMLPromptStyle(AbstractPromptStyle):
    def _messages_to_prompt(self, messages: Sequence[ChatMessage]) -> str: ...
    def _completion_to_prompt(self, completion: str) -> str: ...

def get_prompt_style(
    prompt_style: Literal[
        "default", "llama2", "llama3", "tag", "mistral", "chatml"
    ]
    | None
) -> AbstractPromptStyle: ...