from . import get_console as get_console
from .console import Console as Console
from .text import Text as Text, TextType as TextType
from _typeshed import Incomplete
from typing import Generic, List, Optional, TextIO, TypeVar, Union, overload

PromptType = TypeVar('PromptType')
DefaultType = TypeVar('DefaultType')

class PromptError(Exception): ...

class InvalidResponse(PromptError):
    message: Incomplete
    def __init__(self, message: Union[str, Text]) -> None: ...
    def __rich__(self) -> Text: ...

class PromptBase(Generic[PromptType]):
    response_type: type
    validate_error_message: str
    illegal_choice_message: str
    prompt_suffix: str
    choices: Optional[List[str]]
    def __init__(self, prompt: TextType = ..., *, console: Optional[Console] = ..., password: bool = ..., choices: Optional[List[str]] = ..., case_sensitive: bool = ..., show_default: bool = ..., show_choices: bool = ...) -> None: ...
    @classmethod
    @overload
    def ask(cls, prompt: TextType = ..., *, console: Optional[Console] = ..., password: bool = ..., choices: Optional[List[str]] = ..., case_sensitive: bool = ..., show_default: bool = ..., show_choices: bool = ..., default: DefaultType, stream: Optional[TextIO] = ...) -> DefaultType: ...
    @classmethod
    @overload
    def ask(cls, prompt: TextType = ..., *, console: Optional[Console] = ..., password: bool = ..., choices: Optional[List[str]] = ..., case_sensitive: bool = ..., show_default: bool = ..., show_choices: bool = ..., stream: Optional[TextIO] = ...) -> str: ...
    def render_default(self, default: DefaultType) -> Text: ...
    def make_prompt(self, default: DefaultType) -> Text: ...
    @classmethod
    def get_input(cls, console: Console, prompt: TextType, password: bool, stream: Optional[TextIO] = ...) -> str: ...
    def check_choice(self, value: str) -> bool: ...
    def process_response(self, value: str) -> PromptType: ...
    def on_validate_error(self, value: str, error: InvalidResponse) -> None: ...
    def pre_prompt(self) -> None: ...
    @overload
    def __call__(self, *, stream: Optional[TextIO] = ...) -> PromptType: ...
    @overload
    def __call__(self, *, default: DefaultType, stream: Optional[TextIO] = ...) -> DefaultType: ...

class Prompt(PromptBase[str]):
    response_type = str

class IntPrompt(PromptBase[int]):
    response_type = int
    validate_error_message: str

class FloatPrompt(PromptBase[float]):
    response_type = float
    validate_error_message: str

class Confirm(PromptBase[bool]):
    response_type = bool
    validate_error_message: str
    choices: List[str]
    def render_default(self, default: bool) -> Text: ...
    def process_response(self, value: str) -> bool: ...
