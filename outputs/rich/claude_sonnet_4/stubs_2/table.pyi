from dataclasses import dataclass, field, replace
from typing import TYPE_CHECKING, Dict, Iterable, List, NamedTuple, Optional, Sequence, Tuple, Union

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

if TYPE_CHECKING:
    from .console import Console, ConsoleOptions, JustifyMethod, OverflowMethod, RenderableType, RenderResult

@dataclass
class Column:
    header: "RenderableType" = ""
    footer: "RenderableType" = ""
    header_style: StyleType = ""
    footer_style: StyleType = ""
    style: StyleType = ""
    justify: "JustifyMethod" = "left"
    vertical: VerticalAlignMethod = "top"
    overflow: "OverflowMethod" = "ellipsis"
    width: Optional[int] = None
    min_width: Optional[int] = None
    max_width: Optional[int] = None
    ratio: Optional[int] = None
    no_wrap: bool = False
    highlight: bool = False
    _index: int = 0
    _cells: List["RenderableType"] = field(default_factory=list)
    
    def copy(self) -> "Column": ...
    
    @property
    def cells(self) -> Iterable["RenderableType"]: ...
    
    @property
    def flexible(self) -> bool: ...

@dataclass
class Row:
    style: Optional[StyleType] = None
    end_section: bool = False

class _Cell(NamedTuple):
    style: StyleType
    renderable: "RenderableType"
    vertical: VerticalAlignMethod

class Table(JupyterMixin):
    def __init__(
        self,
        *headers: Union[Column, str],
        title: Optional["RenderableType"] = None,
        caption: Optional["RenderableType"] = None,
        width: Optional[int] = None,
        min_width: Optional[int] = None,
        box: Optional[box.Box] = box.HEAVY_HEAD,
        safe_box: Optional[bool] = None,
        padding: PaddingDimensions = (0, 1),
        collapse_padding: bool = False,
        pad_edge: bool = True,
        expand: bool = False,
        show_header: bool = True,
        show_footer: bool = False,
        show_edge: bool = True,
        show_lines: bool = False,
        leading: int = 0,
        style: StyleType = "none",
        row_styles: Optional[Iterable[StyleType]] = None,
        header_style: Optional[StyleType] = "table.header",
        footer_style: Optional[StyleType] = "table.footer",
        border_style: Optional[StyleType] = None,
        title_style: Optional[StyleType] = None,
        caption_style: Optional[StyleType] = None,
        title_justify: "JustifyMethod" = "center",
        caption_justify: "JustifyMethod" = "center",
        highlight: bool = False,
    ) -> None: ...
    
    @classmethod
    def grid(
        cls,
        *headers: Union[Column, str],
        padding: PaddingDimensions = 0,
        collapse_padding: bool = True,
        pad_edge: bool = False,
        expand: bool = False,
    ) -> "Table": ...
    
    @property
    def expand(self) -> bool: ...
    
    @expand.setter
    def expand(self, expand: bool) -> None: ...
    
    @property
    def row_count(self) -> int: ...
    
    def get_row_style(self, console: "Console", index: int) -> Style: ...
    
    def __rich_measure__(self, console: "Console", options: "ConsoleOptions") -> Measurement: ...
    
    @property
    def padding(self) -> Tuple[int, int, int, int]: ...
    
    @padding.setter
    def padding(self, padding: PaddingDimensions) -> "Table": ...
    
    def add_column(
        self,
        header: "RenderableType" = "",
        footer: "RenderableType" = "",
        *,
        header_style: Optional[StyleType] = None,
        highlight: Optional[bool] = None,
        footer_style: Optional[StyleType] = None,
        style: Optional[StyleType] = None,
        justify: "JustifyMethod" = "left",
        vertical: VerticalAlignMethod = "top",
        overflow: "OverflowMethod" = "ellipsis",
        width: Optional[int] = None,
        min_width: Optional[int] = None,
        max_width: Optional[int] = None,
        ratio: Optional[int] = None,
        no_wrap: bool = False,
    ) -> None: ...
    
    def add_row(
        self,
        *renderables: Optional["RenderableType"],
        style: Optional[StyleType] = None,
        end_section: bool = False,
    ) -> None: ...
    
    def add_section(self) -> None: ...
    
    def __rich_console__(self, console: "Console", options: "ConsoleOptions") -> "RenderResult": ...