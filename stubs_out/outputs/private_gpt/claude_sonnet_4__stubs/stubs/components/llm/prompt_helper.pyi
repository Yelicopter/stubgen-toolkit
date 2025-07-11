import abc
import logging
from collections.abc import Sequence
from llama_index.core.llms import ChatMessage as ChatMessage, MessageRole as MessageRole
from typing import Any, Literal, Optional, Union

logger: logging.Logger

class AbstractPromptStyle(abc.ABC, metaclass=abc.ABCMeta):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def messages_to_prompt(self, messages: Sequence[ChatMessage]) -> str: ...
    def completion_to_prompt(self, prompt: str) -> str: ...

class DefaultPromptStyle(AbstractPromptStyle):
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

def get_prompt_style(prompt_style: Optional[Union[Literal['default'], Literal['llama2'], Literal['llama3'], Literal['tag'], Literal['mistral'], Literal['chatml']]]) -> AbstractPromptStyle: ...
