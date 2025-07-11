import sys
from typing import TYPE_CHECKING, Callable, Dict, Iterable, List, Union

if sys.version_info >= (3, 8):
    from typing import Final
else:
    from typing_extensions import Final  # pragma: no cover

from .segment import ControlCode, ControlType, Segment

if TYPE_CHECKING:
    from .console import Console, ConsoleOptions, RenderResult

class Control:
    def __init__(self, *codes: Union[ControlType, Tuple[ControlType, int]]) -> None:
        ...

    @classmethod
    def bell(cls) -> "Control":
        ...

    @classmethod
    def home(cls) -> "Control":
        ...

    @classmethod
    def move(cls, x: int = 0, y: int = 0) -> "Control":
        ...

    @classmethod
    def move_to_column(cls, x: int, y: int = 0) -> "Control":
        ...

    @classmethod
    def move_to(cls, x: int, y: int) -> "Control":
        ...

    @classmethod
    def clear(cls) -> "Control":
        ...

    @classmethod
    def show_cursor(cls, show: bool) -> "Control":
        ...

    @classmethod
    def alt_screen(cls, enable: bool) -> "Control":
        ...

    @classmethod
    def title(cls, title: str) -> "Control":
        ...

    def __str__(self) -> str:
        ...

    def __rich_console__(self, console: "Console", options: "ConsoleOptions") -> "RenderResult":
        ...

def strip_control_codes(text: str) -> str:
    ...

def escape_control_codes(text: str) -> str:
    ...