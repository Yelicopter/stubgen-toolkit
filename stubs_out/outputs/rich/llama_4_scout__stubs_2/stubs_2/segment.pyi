from .cells import cached_cell_len as cached_cell_len, cell_len as cell_len, get_character_cell_size as get_character_cell_size, set_cell_size as set_cell_size
from .console import Console as Console, ConsoleOptions as ConsoleOptions, RenderResult as RenderResult
from .repr import Result as Result, rich_repr as rich_repr
from .style import Style as Style
from _typeshed import Incomplete
from enum import IntEnum
from itertools import filterfalse as filterfalse
from operator import attrgetter as attrgetter
from typing import Iterable, List, NamedTuple, Optional, Tuple, Union

log: Incomplete

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
ControlCode = Union[Tuple[ControlType], Tuple[ControlType, Union[int, str]], Tuple[ControlType, int, int]]

class Segment(NamedTuple):
    text: str
    style: Optional[Style]
    control: Optional[Tuple[ControlType]]
    @property
    def cell_length(self) -> int: ...
    def __rich_repr__(self) -> Result: ...
    def __bool__(self) -> bool: ...
    def split_cells(self, cut: int) -> Tuple['Segment', 'Segment']: ...
    @classmethod
    def line(cls) -> Segment: ...
    @classmethod
    def apply_style(cls, segments: Iterable['Segment'], style: Optional[Style] = ..., post_style: Optional[Style] = ...) -> Iterable['Segment']: ...
    @classmethod
    def filter_control(cls, segments: Iterable['Segment'], is_control: bool = ...) -> Iterable['Segment']: ...
    @classmethod
    def split_lines(cls, segments: Iterable['Segment']) -> Iterable[List['Segment']]: ...
    @classmethod
    def split_and_crop_lines(cls, segments: Iterable['Segment'], length: int, style: Optional[Style] = ..., pad: bool = ..., include_new_lines: bool = ...) -> Iterable[List['Segment']]: ...
    @classmethod
    def adjust_line_length(cls, line: List['Segment'], length: int, style: Optional[Style] = ..., pad: bool = ...) -> List['Segment']: ...
    @classmethod
    def get_line_length(cls, line: List['Segment']) -> int: ...
    @classmethod
    def get_shape(cls, lines: List[List['Segment']]) -> Tuple[int, int]: ...
    @classmethod
    def set_shape(cls, lines: List[List['Segment']], width: int, height: Optional[int] = ..., style: Optional[Style] = ..., new_lines: bool = ...) -> List[List['Segment']]: ...
    @classmethod
    def align_top(cls, lines: List[List['Segment']], width: int, height: Optional[int], style: Style, new_lines: bool = ...) -> List[List['Segment']]: ...
    @classmethod
    def align_bottom(cls, lines: List[List['Segment']], width: int, height: Optional[int], style: Style, new_lines: bool = ...) -> List[List['Segment']]: ...
    @classmethod
    def align_middle(cls, lines: List[List['Segment']], width: int, height: Optional[int], style: Style, new_lines: bool = ...) -> List[List['Segment']]: ...
    @classmethod
    def simplify(cls, segments: Iterable['Segment']) -> Iterable['Segment']: ...
    @classmethod
    def strip_links(cls, segments: Iterable['Segment']) -> Iterable['Segment']: ...
    @classmethod
    def strip_styles(cls, segments: Iterable['Segment']) -> Iterable['Segment']: ...
    @classmethod
    def remove_color(cls, segments: Iterable['Segment']) -> Iterable['Segment']: ...
    @classmethod
    def divide(cls, segments: Iterable['Segment'], cuts: Iterable[int]) -> Iterable[Iterable[List['Segment']]]: ...
