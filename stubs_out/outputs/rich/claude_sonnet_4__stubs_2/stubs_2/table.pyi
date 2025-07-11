from . import box as box, errors as errors
from ._loop import loop_first_last as loop_first_last, loop_last as loop_last
from ._pick import pick_bool as pick_bool
from ._ratio import ratio_distribute as ratio_distribute, ratio_reduce as ratio_reduce
from .align import VerticalAlignMethod as VerticalAlignMethod
from .console import Console as Console, ConsoleOptions as ConsoleOptions, JustifyMethod as JustifyMethod, OverflowMethod as OverflowMethod, RenderResult as RenderResult, RenderableType as RenderableType
from .jupyter import JupyterMixin as JupyterMixin
from .measure import Measurement as Measurement
from .padding import Padding as Padding, PaddingDimensions as PaddingDimensions
from .protocol import is_renderable as is_renderable
from .segment import Segment as Segment
from .style import Style as Style, StyleType as StyleType
from .text import Text as Text, TextType as TextType
from dataclasses import replace as replace
from typing import Iterable, NamedTuple, Optional, Tuple, Union

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
    def copy(self) -> Column: ...
    @property
    def cells(self) -> Iterable['RenderableType']: ...
    @property
    def flexible(self) -> bool: ...
    def __init__(self, header, footer, header_style, footer_style, style, justify, vertical, overflow, width, min_width, max_width, ratio, no_wrap, highlight, _index, _cells) -> None: ...

class Row:
    style: Optional[StyleType]
    end_section: bool
    def __init__(self, style, end_section) -> None: ...

class _Cell(NamedTuple):
    style: StyleType
    renderable: RenderableType
    vertical: VerticalAlignMethod

class Table(JupyterMixin):
    def __init__(self, *headers: Union[Column, str], title: Optional['RenderableType'] = ..., caption: Optional['RenderableType'] = ..., width: Optional[int] = ..., min_width: Optional[int] = ..., box: Optional[box.Box] = ..., safe_box: Optional[bool] = ..., padding: PaddingDimensions = ..., collapse_padding: bool = ..., pad_edge: bool = ..., expand: bool = ..., show_header: bool = ..., show_footer: bool = ..., show_edge: bool = ..., show_lines: bool = ..., leading: int = ..., style: StyleType = ..., row_styles: Optional[Iterable[StyleType]] = ..., header_style: Optional[StyleType] = ..., footer_style: Optional[StyleType] = ..., border_style: Optional[StyleType] = ..., title_style: Optional[StyleType] = ..., caption_style: Optional[StyleType] = ..., title_justify: JustifyMethod = ..., caption_justify: JustifyMethod = ..., highlight: bool = ...) -> None: ...
    @classmethod
    def grid(cls, *headers: Union[Column, str], padding: PaddingDimensions = ..., collapse_padding: bool = ..., pad_edge: bool = ..., expand: bool = ...) -> Table: ...
    @property
    def expand(self) -> bool: ...
    @property
    def row_count(self) -> int: ...
    def get_row_style(self, console: Console, index: int) -> Style: ...
    def __rich_measure__(self, console: Console, options: ConsoleOptions) -> Measurement: ...
    @property
    def padding(self) -> Tuple[int, int, int, int]: ...
    def add_column(self, header: RenderableType = ..., footer: RenderableType = ..., *, header_style: Optional[StyleType] = ..., highlight: Optional[bool] = ..., footer_style: Optional[StyleType] = ..., style: Optional[StyleType] = ..., justify: JustifyMethod = ..., vertical: VerticalAlignMethod = ..., overflow: OverflowMethod = ..., width: Optional[int] = ..., min_width: Optional[int] = ..., max_width: Optional[int] = ..., ratio: Optional[int] = ..., no_wrap: bool = ...) -> None: ...
    def add_row(self, *renderables: Optional['RenderableType'], style: Optional[StyleType] = ..., end_section: bool = ...) -> None: ...
    def add_section(self) -> None: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
