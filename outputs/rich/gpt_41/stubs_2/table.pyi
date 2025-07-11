from dataclasses import dataclass, field
from typing import Any, Iterable, List, NamedTuple, Optional, Sequence, Tuple, Union

@dataclass
class Column:
    header: Any = ...
    footer: Any = ...
    header_style: Any = ...
    footer_style: Any = ...
    style: Any = ...
    justify: str = ...
    vertical: str = ...
    overflow: str = ...
    width: Optional[int] = ...
    min_width: Optional[int] = ...
    max_width: Optional[int] = ...
    ratio: Optional[int] = ...
    no_wrap: bool = ...
    highlight: bool = ...
    _index: int = ...
    _cells: List[Any] = field(default_factory=list)

    def copy(self) -> "Column": ...
    @property
    def cells(self) -> Iterable[Any]: ...
    @property
    def flexible(self) -> bool: ...

@dataclass
class Row:
    style: Optional[Any] = ...
    end_section: bool = ...

class _Cell(NamedTuple):
    style: Any
    renderable: Any
    vertical: Any

class Table:
    columns: List[Column]
    rows: List[Row]
    title: Optional[Any]
    caption: Optional[Any]
    width: Optional[int]
    min_width: Optional[int]
    box: Any
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
    style: Any
    header_style: Any
    footer_style: Any
    border_style: Optional[Any]
    title_style: Optional[Any]
    caption_style: Optional[Any]
    title_justify: str
    caption_justify: str
    highlight: bool
    row_styles: List[Any]

    def __init__(
        self,
        *headers: Any,
        title: Optional[Any] = ...,
        caption: Optional[Any] = ...,
        width: Optional[int] = ...,
        min_width: Optional[int] = ...,
        box: Any = ...,
        safe_box: Optional[bool] = ...,
        padding: Any = ...,
        collapse_padding: bool = ...,
        pad_edge: bool = ...,
        expand: bool = ...,
        show_header: bool = ...,
        show_footer: bool = ...,
        show_edge: bool = ...,
        show_lines: bool = ...,
        leading: int = ...,
        style: Any = ...,
        row_styles: Optional[Sequence[Any]] = ...,
        header_style: Optional[Any] = ...,
        footer_style: Optional[Any] = ...,
        border_style: Optional[Any] = ...,
        title_style: Optional[Any] = ...,
        caption_style: Optional[Any] = ...,
        title_justify: str = ...,
        caption_justify: str = ...,
        highlight: bool = ...,
    ) -> None: ...
    @classmethod
    def grid(
        cls,
        *headers: Any,
        padding: int = ...,
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
    def get_row_style(self, console: Any, index: int) -> Any: ...
    def __rich_measure__(self, console: Any, options: Any) -> Any: ...
    @property
    def padding(self) -> Tuple[int, int, int, int]: ...
    @padding.setter
    def padding(self, padding: Any) -> "Table": ...
    def add_column(
        self,
        header: Any = ...,
        footer: Any = ...,
        *,
        header_style: Optional[Any] = ...,
        highlight: Optional[bool] = ...,
        footer_style: Optional[Any] = ...,
        style: Optional[Any] = ...,
        justify: str = ...,
        vertical: str = ...,
        overflow: str = ...,
        width: Optional[int] = ...,
        min_width: Optional[int] = ...,
        max_width: Optional[int] = ...,
        ratio: Optional[int] = ...,
        no_wrap: bool = ...,
    ) -> None: ...
    def add_row(self, *renderables: Any, style: Optional[Any] = ..., end_section: bool = ...) -> None: ...
    def add_section(self) -> None: ...
    def __rich_console__(self, console: Any, options: Any) -> Iterable[Any]: ...
    def _calculate_column_widths(self, console: Any, options: Any) -> List[int]: ...
    @classmethod
    def _collapse_widths(cls, widths: List[int], wrapable: List[bool], max_width: int) -> List[int]: ...
    def _get_cells(self, console: Any, column_index: int, column: Column) -> Iterable[_Cell]: ...
    def _get_padding_width(self, column_index: int) -> int: ...
    def _measure_column(self, console: Any, options: Any, column: Column) -> Any: ...
    def _render(self, console: Any, options: Any, widths: List[int]) -> Iterable[Any]: ...