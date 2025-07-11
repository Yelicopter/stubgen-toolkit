from typing import Any, Generic, List, Optional, TextIO, TypeVar, Union, overload

from . import get_console
from .console import Console
from .text import Text, TextType

PromptType = TypeVar("PromptType")
DefaultType = TypeVar("DefaultType")


class PromptError(Exception):
    """Exception base class for prompt related errors."""


class InvalidResponse(PromptError):
    """Exception to indicate a response was invalid. Raise this within process_response() to indicate an error
    and provide an error message.

    Args:
        message (Union[str, Text]): Error message.
    """

    def __init__(self, message: Union[str, Text]) -> None:
        self.message = message

    def __rich__(self) -> Text:
        return self.message


class PromptBase(Generic[PromptType]):
    """Ask the user for input until a valid response is received. This is the base class, see one of
    the concrete classes for examples.

    Args:
        prompt (TextType, optional): Prompt text. Defaults to "".
        console (Console, optional): A Console instance or None to use global console. Defaults to None.
        password (bool, optional): Enable password input. Defaults to False.
        choices (List[str], optional): A list of valid choices. Defaults to None.
        case_sensitive (bool, optional): Matching of choices should be case-sensitive. Defaults to True.
        show_default (bool, optional): Show default in prompt. Defaults to True.
        show_choices (bool, optional): Show choices in prompt. Defaults to True.
    """

    response_type: type = str

    validate_error_message = "[prompt.invalid]Please enter a valid value"
    illegal_choice_message = (
        "[prompt.invalid.choice]Please select one of the available options"
    )
    prompt_suffix = ": "

    choices: Optional[List[str]] = None

    def __init__(
        self,
        prompt: TextType = "",
        *,
        console: Optional[Console] = None,
        password: bool = False,
        choices: Optional[List[str]] = None,
        case_sensitive: bool = True,
        show_default: bool = True,
        show_choices: bool = True,
    ) -> None:
        ...

    @classmethod
    @overload
    def ask(
        cls,
        prompt: TextType = "",
        *,
        console: Optional[Console] = None,
        password: bool = False,
        choices: Optional[List[str]] = None,
        case_sensitive: bool = True,
        show_default: bool = True,
        show_choices: bool = True,
        default: DefaultType,
        stream: Optional[TextIO] = None,
    ) -> DefaultType:
        ...

    @classmethod
    @overload
    def ask(
        cls,
        prompt: TextType = "",
        *,
        console: Optional[Console] = None,
        password: bool = False,
        choices: Optional[List[str]] = None,
        case_sensitive: bool = True,
        show_default: bool = True,
        show_choices: bool = True,
        stream: Optional[TextIO] = None,
    ) -> str:
        ...

    @classmethod
    def ask(
        cls,
        prompt: TextType = "",
        *,
        console: Optional[Console] = None,
        password: bool = False,
        choices: Optional[List[str]] = None,
        case_sensitive: bool = True,
        show_default: bool = True,
        show_choices: bool = True,
        default: Any = ...,
        stream: Optional[TextIO] = None,
    ) -> PromptType:
        ...

    def render_default(self, default: DefaultType) -> Text:
        ...

    def make_prompt(self, default: DefaultType) -> Text:
        ...

    @classmethod
    def get_input(
        cls,
        console: Console,
        prompt: TextType,
        password: bool,
        stream: Optional[TextIO] = None,
    ) -> str:
        ...

    def check_choice(self, value: str) -> bool:
        ...

    def process_response(self, value: str) -> PromptType:
        ...

    def on_validate_error(self, value: str, error: InvalidResponse) -> None:
        ...

    def pre_prompt(self) -> None:
        ...

    @overload
    def __call__(self, *, stream: Optional[TextIO] = None) -> PromptType:
        ...

    @overload
    def __call__(self, *, default: DefaultType, stream: Optional[TextIO] = None) -> DefaultType:
        ...

    def __call__(self, *, default: Any = ..., stream: Optional[TextIO] = None) -> PromptType:
        ...

class Prompt(PromptBase[str]):
    """A prompt that returns a str.

    Example:
        >>> name = Prompt.ask("Enter your name")


    """

    response_type = str


class IntPrompt(PromptBase[int]):
    """A prompt that returns an integer.

    Example:
        >>> burrito_count = IntPrompt.ask("How many burritos do you want to order")

    """

    response_type = int
    validate_error_message = "[prompt.invalid]Please enter a valid integer number"


class FloatPrompt(PromptBase[float]):
    """A prompt that returns a float.

    Example:
        >>> temperature = FloatPrompt.ask("Enter desired temperature")

    """

    response_type = float
    validate_error_message = "[prompt.invalid]Please enter a number"


class Confirm(PromptBase[bool]):
    """A yes / no confirmation prompt.

    Example:
        >>> if Confirm.ask("Continue"):
                run_job()

    """

    response_type = bool
    validate_error_message = "[prompt.invalid]Please enter Y or N"
    choices: List[str] = ["y", "n"]

    def render_default(self, default: bool) -> Text:
        ...

    def process_response(self, value: str) -> bool:
        ...