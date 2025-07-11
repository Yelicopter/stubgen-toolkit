from enum import IntEnum
from typing import (
    TYPE_CHECKING,
    Dict,
    Iterable,
    List,
    NamedTuple,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
)

from .style import Style

if TYPE_CHECKING:
    from .console import Console, ConsoleOptions, RenderResult

class ControlType(IntEnum):
    BELL = 0
    CARRIAGE_RETURN = 1
    HOME = 2
    CLEAR = 3
    SHOW_CURSOR = 4
    HIDE_CURSOR = 5
    ENABLE_ALT_SCREEN = 6
    DISABLE_ALT_SCREEN = 7
    CURSOR_UP = 8
    CURSOR_DOWN = 9
    CURSOR_FORWARD = 10
    CURSOR_BACKWARD = 11
    CURSOR_MOVE_TO_COLUMN = 12
    CURSOR_MOVE_TO = 13
    ERASE_IN_LINE = 14
    SET_WINDOW_TITLE = 15

ControlCode = Union[
    Tuple[ControlType],
    Tuple[ControlType, Union[int, str]],
    Tuple[ControlType, int, int],
]

class Segment(NamedTuple):
    text: str
    style: Optional[Style]
    control: Optional[Sequence[ControlCode]]
    @property
    def cell_length(self) -> int: ...
    def __rich_repr__(self) -> Iterable[Any]: ...
    def __bool__(self) -> bool: ...
    @property
    def is_control(self) -> bool: ...
    @classmethod
    def _split_cells(cls, segment: "Segment", cut: int) -> Tuple["Segment", "Segment"]: ...
    def split_cells(self, cut: int) -> Tuple["Segment", "Segment"]: ...
    @classmethod
    def line(cls) -> "Segment": ...
    @classmethod
    def apply_style(
        cls,
        segments: Iterable["Segment"],
        style: Optional[Style] = ...,
        post_style: Optional[Style] = ...,
    ) -> Iterable["Segment"]: ...
    @classmethod
    def filter_control(
        cls, segments: Iterable["Segment"], is_control: bool = ...
    ) -> Iterable["Segment"]: ...
    @classmethod
    def split_lines(cls, segments: Iterable["Segment"]) -> Iterable[List["Segment"]]: ...
    @classmethod
    def split_and_crop_lines(
        cls,
        segments: Iterable["Segment"],
        length: int,
        style: Optional[Style] = ...,
        pad: bool = ...,
        include_new_lines: bool = ...,
    ) -> Iterable[List["Segment"]]: ...
    @classmethod
    def adjust_line_length(
        cls,
        line: List["Segment"],
        length: int,
        style: Optional[Style] = ...,
        pad: bool = ...,
    ) -> List["Segment"]: ...
    @classmethod
    def get_line_length(cls, line: List["Segment"]) -> int: ...
    @classmethod
    def get_shape(cls, lines: List[List["Segment"]]) -> Tuple[int, int]: ...
    @classmethod
    def set_shape(
        cls,
        lines: List[List["Segment"]],
        width: int,
        height: Optional[int] = ...,
        style: Optional[Style] = ...,
        new_lines: bool = ...,
    ) -> List[List["Segment"]]: ...
    @classmethod
    def align_top(
        cls: Type["Segment"],
        lines: List[List["Segment"]],
        width: int,
        height: int,
        style: Style,
        new_lines: bool = ...,
    ) -> List[List["Segment"]]: ...
    @classmethod
    def align_bottom(
        cls: Type["Segment"],
        lines: List[List["Segment"]],
        width: int,
        height: int,
        style: Style,
        new_lines: bool = ...,
    ) -> List[List["Segment"]]: ...
    @classmethod
    def align_middle(
        cls: Type["Segment"],
        lines: List[List["Segment"]],
        width: int,
        height: int,
        style: Style,
        new_lines: bool = ...,
    ) -> List[List["Segment"]]: ...
    @classmethod
    def simplify(cls, segments: Iterable["Segment"]) -> Iterable["Segment"]: ...
    @classmethod
    def strip_links(cls, segments: Iterable["Segment"]) -> Iterable["Segment"]: ...
    @classmethod
    def strip_styles(cls, segments: Iterable["Segment"]) -> Iterable["Segment"]: ...
    @classmethod
    def remove_color(cls, segments: Iterable["Segment"]) -> Iterable["Segment"]: ...
    @classmethod
    def divide(
        cls, segments: Iterable["Segment"], cuts: Iterable[int]
    ) -> Iterable[List["Segment"]]: ...

class Segments:
    segments: List[Segment]
    new_lines: bool
    def __init__(self, segments: Iterable[Segment], new_lines: bool = ...) -> None: ...
    def __rich_console__(
        self, console: "Console", options: "ConsoleOptions"
    ) -> "RenderResult": ...

class SegmentLines:
    lines: List[List[Segment]]
    new_lines: bool
    def __init__(self, lines: Iterable[List[Segment]], new_lines: bool = ...) -> None: ...
    def __rich_console__(
        self, console: "Console", options: "ConsoleOptions"
    ) -> "RenderResult": ...