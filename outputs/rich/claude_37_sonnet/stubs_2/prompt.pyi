from typing import Any, Generic, List, Optional, TextIO, TypeVar, Union, overload

from . import get_console
from .console import Console
from .text import Text, TextType

PromptType = TypeVar("PromptType")
DefaultType = TypeVar("DefaultType")

class PromptError(Exception): ...

class InvalidResponse(PromptError):
    def __init__(self, message: TextType) -> None: ...
    message: TextType
    def __rich__(self) -> TextType: ...

class PromptBase(Generic[PromptType]):
    response_type: type
    validate_error_message: str
    illegal_choice_message: str
    prompt_suffix: str
    choices: Optional[List[str]]
    def __init__(
        self,
        prompt: TextType = ...,
        *,
        console: Optional[Console] = ...,
        password: bool = ...,
        choices: Optional[List[str]] = ...,
        case_sensitive: bool = ...,
        show_default: bool = ...,
        show_choices: bool = ...,
    ) -> None: ...
    console: Console
    prompt: Text
    password: bool
    case_sensitive: bool
    show_default: bool
    show_choices: bool
    @classmethod
    @overload
    def ask(
        cls,
        prompt: TextType = ...,
        *,
        console: Optional[Console] = ...,
        password: bool = ...,
        choices: Optional[List[str]] = ...,
        case_sensitive: bool = ...,
        show_default: bool = ...,
        show_choices: bool = ...,
        default: DefaultType,
        stream: Optional[TextIO] = ...,
    ) -> Union[DefaultType, PromptType]: ...
    @classmethod
    @overload
    def ask(
        cls,
        prompt: TextType = ...,
        *,
        console: Optional[Console] = ...,
        password: bool = ...,
        choices: Optional[List[str]] = ...,
        case_sensitive: bool = ...,
        show_default: bool = ...,
        show_choices: bool = ...,
        stream: Optional[TextIO] = ...,
    ) -> PromptType: ...
    def render_default(self, default: DefaultType) -> Text: ...
    def make_prompt(self, default: DefaultType) -> Text: ...
    @classmethod
    def get_input(
        cls,
        console: Console,
        prompt: TextType,
        password: bool,
        stream: Optional[TextIO] = ...,
    ) -> str: ...
    def check_choice(self, value: str) -> bool: ...
    def process_response(self, value: str) -> PromptType: ...
    def on_validate_error(self, value: str, error: InvalidResponse) -> None: ...
    def pre_prompt(self) -> None: ...
    @overload
    def __call__(self, *, stream: Optional[TextIO] = ...) -> PromptType: ...
    @overload
    def __call__(
        self, *, default: DefaultType, stream: Optional[TextIO] = ...
    ) -> Union[PromptType, DefaultType]: ...

class Prompt(PromptBase[str]):
    response_type: type

class IntPrompt(PromptBase[int]):
    response_type: type
    validate_error_message: str

class FloatPrompt(PromptBase[float]):
    response_type: type
    validate_error_message: str

class Confirm(PromptBase[bool]):
    response_type: type
    validate_error_message: str
    choices: List[str]
    def render_default(self, default: DefaultType) -> Text: ...
    def process_response(self, value: str) -> bool: ...