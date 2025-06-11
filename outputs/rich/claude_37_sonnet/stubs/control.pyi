import sys
import time
from typing import TYPE_CHECKING, Callable, Dict, Iterable, List, Union

if sys.version_info >= (3, 8):
    from typing import Final
else:
    from typing_extensions import Final  # pragma: no cover

from .segment import ControlCode, ControlType, Segment

if TYPE_CHECKING:
    from .console import Console, ConsoleOptions, RenderResult

STRIP_CONTROL_CODES: Final
_CONTROL_STRIP_TRANSLATE: Final

CONTROL_ESCAPE: Final

CONTROL_CODES_FORMAT: Dict[int, Callable[..., str]]

class Control:
    segment: Segment

    def __init__(self, *codes: Union[ControlType, ControlCode]) -> None: ...

    @classmethod
    def bell(cls) -> "Control": ...

    @classmethod
    def home(cls) -> "Control": ...

    @classmethod
    def move(cls, x: int = 0, y: int = 0) -> "Control": ...

    @classmethod
    def move_to_column(cls, x: int, y: int = 0) -> "Control": ...

    @classmethod
    def move_to(cls, x: int, y: int) -> "Control": ...

    @classmethod
    def clear(cls) -> "Control": ...

    @classmethod
    def show_cursor(cls, show: bool) -> "Control": ...

    @classmethod
    def alt_screen(cls, enable: bool) -> "Control": ...

    @classmethod
    def title(cls, title: str) -> "Control": ...

    def __str__(self) -> str: ...

    def __rich_console__(
        self, console: "Console", options: "ConsoleOptions"
    ) -> "RenderResult": ...

def strip_control_codes(
    text: str, _translate_table: Dict[int, None] = _CONTROL_STRIP_TRANSLATE
) -> str: ...

def escape_control_codes(
    text: str,
    _translate_table: Dict[int, str] = CONTROL_ESCAPE,
) -> str: ...