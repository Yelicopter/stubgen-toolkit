from dataclasses import dataclass, field, replace
from typing import Dict, Iterable, List, NamedTuple, Optional, Sequence, Tuple, Union

from . import box, errors
from ._loop import loop_first_last, loop_last
from ._pick import pick_bool
from ._ratio import ratio_distribute, ratio_reduce
from .align import VerticalAlignMethod
from .jupyter import JupyterMixin
from .measure import Measurement
from .padding import Padding, PaddingDimensions
from .protocol import is_renderable
from .segment import Segment
from .style import Style, StyleType
from .text import Text, TextType

from .console import Console, ConsoleOptions, JustifyMethod, OverflowMethod, RenderableType, RenderResult

@dataclass
class Column:
    header: RenderableType = ...
    footer: RenderableType = ...
    header_style: StyleType = ...
    footer_style: StyleType = ...
    style: StyleType = ...
    justify: JustifyMethod = ...
    vertical: VerticalAlignMethod = ...
    overflow: OverflowMethod = ...
    width: Optional[int] = ...
    min_width: Optional[int] = ...
    max_width: Optional[int] = ...
    ratio: Optional[int] = ...
    no_wrap: bool = ...
    highlight: bool = ...
    _index: int = ...
    _cells: List[RenderableType] = field(default_factory=list)
    def copy(self) -> "Column": ...
    @property
    def cells(self) -> Iterable[RenderableType]: ...
    @property
    def flexible(self) -> bool: ...

@dataclass
class Row:
    style: Optional[StyleType] = ...
    end_section: bool = ...

class _Cell(NamedTuple):
    style: StyleType
    renderable: RenderableType
    vertical: VerticalAlignMethod

class Table(JupyterMixin):
    columns: List[Column]
    rows: List[Row]
    def __init__(
        self,
        *headers: Union[Column, str],
        title: Optional[TextType] = ...,
        caption: Optional[TextType] = ...,
        width: Optional[int] = ...,
        min_width: Optional[int] = ...,
        box: Optional[box.Box] = ...,
        safe_box: Optional[bool] = ...,
        padding: PaddingDimensions = ...,
        collapse_padding: bool = ...,
        pad_edge: bool = ...,
        expand: bool = ...,
        show_header: bool = ...,
        show_footer: bool = ...,
        show_edge: bool = ...,
        show_lines: bool = ...,
        leading: int = ...,
        style: StyleType = ...,
        row_styles: Optional[Iterable[StyleType]] = ...,
        header_style: Optional[StyleType] = ...,
        footer_style: Optional[StyleType] = ...,
        border_style: Optional[StyleType] = ...,
        title_style: Optional[StyleType] = ...,
        caption_style: Optional[StyleType] = ...,
        title_justify: JustifyMethod = ...,
        caption_justify: JustifyMethod = ...,
        highlight: bool = ...,
    ) -> None: ...
    title: Optional[TextType]
    caption: Optional[TextType]
    width: Optional[int]
    min_width: Optional[int]
    box: Optional[box.Box]
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
    row_styles: Sequence[StyleType]
    @classmethod
    def grid(
        cls,
        *headers: Union[Column, str],
        padding: PaddingDimensions = ...,
        collapse_padding: bool = ...,
        pad_edge: bool = ...,
        expand: bool = ...,
    ) -> "Table": ...
    @property
    def expand(self) -> bool: ...
    @expand.setter
    def expand(self, expand: bool) -> None: ...
    @property
    def _extra_width(self) -> int: ...
    @property
    def row_count(self) -> int: ...
    def get_row_style(self, console: Console, index: int) -> StyleType: ...
    def __rich_measure__(
        self, console: Console, options: ConsoleOptions
    ) -> Measurement: ...
    @property
    def padding(self) -> Tuple[int, int, int, int]: ...
    @padding.setter
    def padding(self, padding: PaddingDimensions) -> "Table": ...
    def add_column(
        self,
        header: RenderableType = ...,
        footer: RenderableType = ...,
        *,
        header_style: Optional[StyleType] = ...,
        highlight: Optional[bool] = ...,
        footer_style: Optional[StyleType] = ...,
        style: Optional[StyleType] = ...,
        justify: JustifyMethod = ...,
        vertical: VerticalAlignMethod = ...,
        overflow: OverflowMethod = ...,
        width: Optional[int] = ...,
        min_width: Optional[int] = ...,
        max_width: Optional[int] = ...,
        ratio: Optional[int] = ...,
        no_wrap: bool = ...,
    ) -> None: ...
    def add_row(
        self,
        *renderables: Optional[RenderableType],
        style: Optional[StyleType] = ...,
        end_section: bool = ...,
    ) -> None: ...
    def add_section(self) -> None: ...
    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult: ...
    def _calculate_column_widths(
        self, console: Console, options: ConsoleOptions
    ) -> List[int]: ...
    @classmethod
    def _collapse_widths(
        cls, widths: List[int], wrapable: List[bool], max_width: int
    ) -> List[int]: ...
    def _get_cells(
        self, console: Console, column_index: int, column: Column
    ) -> Iterable[_Cell]: ...
    def _get_padding_width(self, column_index: int) -> int: ...
    def _measure_column(
        self,
        console: Console,
        options: ConsoleOptions,
        column: Column,
    ) -> Measurement: ...
    def _render(
        self, console: Console, options: ConsoleOptions, widths: List[int]
    ) -> RenderResult: ...