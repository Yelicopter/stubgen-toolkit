from enum import IntEnum
from functools import lru_cache
from itertools import filterfalse
from logging import getLogger
from operator import attrgetter
from typing import Dict, Iterable, List, NamedTuple, Optional, Pattern, Sequence, Tuple, Type, Union

from .cells import _is_single_cell_widths, cached_cell_len, cell_len, get_character_cell_size, set_cell_size
from .repr import Result, rich_repr
from .style import Style

from .console import Console, ConsoleOptions, RenderResult

class ControlType(IntEnum):
    BELL: int
    CARRIAGE_RETURN: int
    HOME: int
    CLEAR: int
    SHOW_CURSOR: int
    HIDE_CURSOR: int
    ENABLE_ALT_SCREEN: int
    DISABLE_ALT_SCREEN: int
    CURSOR_UP: int
    CURSOR_DOWN: int
    CURSOR_FORWARD: int
    CURSOR_BACKWARD: int
    CURSOR_MOVE_TO_COLUMN: int
    CURSOR_MOVE_TO: int
    ERASE_IN_LINE: int
    SET_WINDOW_TITLE: int

ControlCode = Union[
    Tuple[ControlType],
    Tuple[ControlType, Union[int, str]],
    Tuple[ControlType, int, int],
]

@rich_repr()
class Segment(NamedTuple):
    text: str
    style: Optional[Style] = ...
    control: Optional[Sequence[ControlCode]] = ...
    @property
    def cell_length(self) -> int: ...
    def __rich_repr__(self) -> Result: ...
    def __bool__(self) -> bool: ...
    @property
    def is_control(self) -> bool: ...
    @classmethod
    @lru_cache(1024 * 16)
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
    def __init__(self, segments: Iterable[Segment], new_lines: bool = ...) -> None: ...
    segments: List[Segment]
    new_lines: bool
    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult: ...

class SegmentLines:
    def __init__(self, lines: Iterable[List[Segment]], new_lines: bool = ...) -> None: ...
    lines: List[List[Segment]]
    new_lines: bool
    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult: ...