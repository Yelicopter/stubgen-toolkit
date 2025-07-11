from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Iterable, List, NamedTuple, Optional, Sequence, Tuple, Union

from rich.align import VerticalAlignMethod
from rich.console import Console, ConsoleOptions, JustifyMethod, OverflowMethod, RenderResult, RenderableType
from rich.jupyter import JupyterMixin
from rich.measure import Measurement
from rich.padding import PaddingDimensions
from rich.style import Style, StyleType
from rich.text import Text, TextType

class Box:
    def __init__(self) -> None: ...

@dataclass
class Column:
    header: RenderableType
    footer: RenderableType
    header_style: StyleType
    footer_style: StyleType
    style: StyleType
    justify: JustifyMethod
    vertical: VerticalAlignMethod
    overflow: OverflowMethod
    width: Optional[int]
    min_width: Optional[int]
    max_width: Optional[int]
    ratio: Optional[int]
    no_wrap: bool
    highlight: bool
    _index: int
    _cells: List[RenderableType]
    def copy(self) -> Column: ...
    @property
    def cells(self) -> Iterable[RenderableType]: ...
    @property
    def flexible(self) -> bool: ...

@dataclass
class Row:
    style: Optional[StyleType]
    end_section: bool

class _Cell(NamedTuple):
    style: StyleType
    renderable: RenderableType
    vertical: VerticalAlignMethod

class Table(JupyterMixin):
    columns: List[Column]
    rows: List[Row]
    title: Optional[TextType]
    caption: Optional[TextType]
    width: Optional[int]
    min_width: Optional[int]
    box: Optional[Box]
    safe_box: Optional[bool]
    _padding: Tuple[int, int, int, int]
    pad_edge: bool
    _expand: bool
    show_header: bool
    show_footer: bool
    show_edge: bool
    show_lines: bool
    leading: int
    collapse_padding: bool
    style: StyleType
    header_style: StyleType
    footer_style: StyleType
    border_style: Optional[StyleType]
    title_style: Optional[StyleType]
    caption_style: Optional[StyleType]
    title_justify: JustifyMethod
    caption_justify: JustifyMethod
    highlight: bool
    row_styles: List[StyleType]
    def __init__(self, *headers: Union[Column, str], title: Optional[TextType] = None, caption: Optional[TextType] = None, width: Optional[int] = None, min_width: Optional[int] = None, box: Optional[Box] = ..., safe_box: Optional[bool] = None, padding: PaddingDimensions = (0, 1), collapse_padding: bool = False, pad_edge: bool = True, expand: bool = False, show_header: bool = True, show_footer: bool = False, show_edge: bool = True, show_lines: bool = False, leading: int = 0, style: StyleType = "none", row_styles: Optional[Iterable[StyleType]] = None, header_style: Optional[StyleType] = "table.header", footer_style: Optional[StyleType] = "table.footer", border_style: Optional[StyleType] = None, title_style: Optional[StyleType] = None, caption_style: Optional[StyleType] = None, title_justify: JustifyMethod = "center", caption_justify: JustifyMethod = "center", highlight: bool = False) -> None: ...
    @classmethod
    def grid(cls, *headers: Union[Column, str], padding: PaddingDimensions = 0, collapse_padding: bool = True, pad_edge: bool = False, expand: bool = False) -> Table: ...
    @property
    def expand(self) -> bool: ...
    @expand.setter
    def expand(self, expand: bool) -> None: ...
    @property
    def _extra_width(self) -> int: ...
    @property
    def row_count(self) -> int: ...
    def get_row_style(self, console: Console, index: int) -> Style: ...
    def __rich_measure__(self, console: Console, options: ConsoleOptions) -> Measurement: ...
    @property
    def padding(self) -> Tuple[int, int, int, int]: ...
    @padding.setter
    def padding(self, padding: PaddingDimensions) -> None: ...
    def add_column(self, header: RenderableType = "", footer: RenderableType = "", *, header_style: Optional[StyleType] = None, highlight: Optional[bool] = None, footer_style: Optional[StyleType] = None, style: Optional[StyleType] = None, justify: JustifyMethod = "left", vertical: VerticalAlignMethod = "top", overflow: OverflowMethod = "ellipsis", width: Optional[int] = None, min_width: Optional[int] = None, max_width: Optional[int] = None, ratio: Optional[int] = None, no_wrap: bool = False) -> None: ...
    def add_row(self, *renderables: Optional[RenderableType], style: Optional[StyleType] = None, end_section: bool = False) -> None: ...
    def add_section(self) -> None: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
    def _calculate_column_widths(self, console: Console, options: ConsoleOptions) -> List[int]: ...
    @classmethod
    def _collapse_widths(cls, widths: List[int], wrapable: List[bool], max_width: int) -> List[int]: ...
    def _get_cells(self, console: Console, column_index: int, column: Column) -> Iterable[_Cell]: ...
    def _get_padding_width(self, column_index: int) -> int: ...
    def _measure_column(self, console: Console, options: ConsoleOptions, column: Column) -> Measurement: ...
    def _render(self, console: Console, options: ConsoleOptions, widths: List[int]) -> RenderResult: ...