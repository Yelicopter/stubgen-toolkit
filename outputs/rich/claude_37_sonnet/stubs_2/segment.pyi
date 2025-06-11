from enum import IntEnum
from functools import lru_cache
from itertools import filterfalse
from logging import getLogger
from operator import attrgetter
from typing import Dict, Iterable, List, NamedTuple, Optional, Pattern, Sequence, Tuple, Type, Union

from .cells import cached_cell_len, cell_len, get_character_cell_size, set_cell_size
from .repr import Result, rich_repr
from .style import Style

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

@rich_repr()
class Segment(NamedTuple):
    text: str
    style: Optional[Style] = None
    control: Optional[Sequence[ControlCode]] = None
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
        style: Optional[Style] = None,
        post_style: Optional[Style] = None,
    ) -> Iterable["Segment"]: ...
    @classmethod
    def filter_control(
        cls, segments: Iterable["Segment"], is_control: bool = False
    ) -> Iterable["Segment"]: ...
    @classmethod
    def split_lines(cls, segments: Iterable["Segment"]) -> Iterable[List["Segment"]]: ...
    @classmethod
    def split_and_crop_lines(
        cls,
        segments: Iterable["Segment"],
        length: int,
        style: Optional[Style] = None,
        pad: bool = False,
        include_new_lines: bool = False,
    ) -> Iterable[List["Segment"]]: ...
    @classmethod
    def adjust_line_length(
        cls,
        line: List["Segment"],
        length: int,
        style: Optional[Style] = None,
        pad: bool = False,
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
        height: Optional[int] = None,
        style: Optional[Style] = None,
        new_lines: bool = False,
    ) -> List[List["Segment"]]: ...
    @classmethod
    def align_top(
        cls: Type["Segment"],
        lines: List[List["Segment"]],
        width: int,
        height: int,
        style: Style,
        new_lines: bool = False,
    ) -> List[List["Segment"]]: ...
    @classmethod
    def align_bottom(
        cls: Type["Segment"],
        lines: List[List["Segment"]],
        width: int,
        height: int,
        style: Style,
        new_lines: bool = False,
    ) -> List[List["Segment"]]: ...
    @classmethod
    def align_middle(
        cls: Type["Segment"],
        lines: List[List["Segment"]],
        width: int,
        height: int,
        style: Style,
        new_lines: bool = False,
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
    def __init__(self, segments: Iterable[Segment], new_lines: bool = False) -> None: ...
    segments: List[Segment]
    new_lines: bool
    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult: ...

class SegmentLines:
    def __init__(self, lines: Iterable[List[Segment]], new_lines: bool = False) -> None: ...
    lines: List[List[Segment]]
    new_lines: bool
    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult: ...