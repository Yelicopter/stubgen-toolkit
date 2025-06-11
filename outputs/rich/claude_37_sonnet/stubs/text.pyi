import re
from functools import partial, reduce
from math import gcd
from operator import itemgetter
from typing import Any, Callable, Dict, Iterable, List, NamedTuple, Optional, Pattern, Tuple, Union

from ._loop import loop_last
from ._pick import pick_bool
from ._wrap import divide_line
from .align import AlignMethod
from .cells import cell_len, set_cell_size
from .containers import Lines
from .control import strip_control_codes
from .emoji import EmojiVariant
from .jupyter import JupyterMixin
from .measure import Measurement
from .segment import Segment
from .style import Style, StyleType

from .console import Console, ConsoleOptions, JustifyMethod, OverflowMethod, RenderResult

DEFAULT_JUSTIFY: JustifyMethod
DEFAULT_OVERFLOW: OverflowMethod

_re_whitespace: Pattern[str]

TextType = Union[str, "Text"]
GetStyleCallable = Callable[[str], Optional[StyleType]]

class Span(NamedTuple):
    start: int
    end: int
    style: Union[str, Style]
    def __repr__(self) -> str: ...
    def __bool__(self) -> bool: ...
    def split(self, offset: int) -> Tuple["Span", Optional["Span"]]: ...
    def move(self, offset: int) -> "Span": ...
    def right_crop(self, offset: int) -> "Span": ...
    def extend(self, cells: int) -> "Span": ...

class Text(JupyterMixin):
    def __init__(
        self,
        text: str = ...,
        style: Union[str, Style] = ...,
        *,
        justify: Optional[JustifyMethod] = ...,
        overflow: Optional[OverflowMethod] = ...,
        no_wrap: Optional[bool] = ...,
        end: str = ...,
        tab_size: Optional[int] = ...,
        spans: Optional[List[Span]] = ...,
    ) -> None: ...
    _text: List[str]
    style: Union[str, Style]
    justify: Optional[JustifyMethod]
    overflow: Optional[OverflowMethod]
    no_wrap: Optional[bool]
    end: str
    tab_size: Optional[int]
    _spans: List[Span]
    _length: int
    def __len__(self) -> int: ...
    def __bool__(self) -> bool: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __add__(self, other: Any) -> "Text": ...
    def __eq__(self, other: object) -> bool: ...
    def __contains__(self, other: object) -> bool: ...
    def __getitem__(self, slice: Union[int, slice]) -> "Text": ...
    @property
    def cell_len(self) -> int: ...
    @property
    def markup(self) -> str: ...
    @classmethod
    def from_markup(
        cls,
        text: str,
        *,
        style: Union[str, Style] = ...,
        emoji: bool = ...,
        emoji_variant: Optional[EmojiVariant] = ...,
        justify: Optional[JustifyMethod] = ...,
        overflow: Optional[OverflowMethod] = ...,
        end: str = ...,
    ) -> "Text": ...
    @classmethod
    def from_ansi(
        cls,
        text: str,
        *,
        style: Union[str, Style] = ...,
        justify: Optional[JustifyMethod] = ...,
        overflow: Optional[OverflowMethod] = ...,
        no_wrap: Optional[bool] = ...,
        end: str = ...,
        tab_size: Optional[int] = ...,
    ) -> "Text": ...
    @classmethod
    def styled(
        cls,
        text: str,
        style: StyleType = ...,
        *,
        justify: Optional[JustifyMethod] = ...,
        overflow: Optional[OverflowMethod] = ...,
    ) -> "Text": ...
    @classmethod
    def assemble(
        cls,
        *parts: Union[str, "Text", Tuple[str, StyleType]],
        style: Union[str, Style] = ...,
        justify: Optional[JustifyMethod] = ...,
        overflow: Optional[OverflowMethod] = ...,
        no_wrap: Optional[bool] = ...,
        end: str = ...,
        tab_size: int = ...,
        meta: Optional[Dict[str, Any]] = ...,
    ) -> "Text": ...
    @property
    def plain(self) -> str: ...
    @plain.setter
    def plain(self, new_text: str) -> None: ...
    @property
    def spans(self) -> List[Span]: ...
    @spans.setter
    def spans(self, spans: List[Span]) -> None: ...
    def blank_copy(self, plain: str = ...) -> "Text": ...
    def copy(self) -> "Text": ...
    def stylize(
        self,
        style: Union[str, Style],
        start: int = ...,
        end: Optional[int] = ...,
    ) -> None: ...
    def stylize_before(
        self,
        style: Union[str, Style],
        start: int = ...,
        end: Optional[int] = ...,
    ) -> None: ...
    def apply_meta(
        self, meta: Dict[str, Any], start: int = ..., end: Optional[int] = ...
    ) -> None: ...
    def on(self, meta: Optional[Dict[str, Any]] = ..., **handlers: Any) -> "Text": ...
    def remove_suffix(self, suffix: str) -> None: ...
    def get_style_at_offset(self, console: Console, offset: int) -> Style: ...
    def extend_style(self, spaces: int) -> None: ...
    def highlight_regex(
        self,
        re_highlight: Union[Pattern[str], str],
        style: Optional[Union[GetStyleCallable, StyleType]] = ...,
        *,
        style_prefix: str = ...,
    ) -> int: ...
    def highlight_words(
        self,
        words: Iterable[str],
        style: Union[str, Style],
        *,
        case_sensitive: bool = ...,
    ) -> int: ...
    def rstrip(self) -> None: ...
    def rstrip_end(self, size: int) -> None: ...
    def set_length(self, new_length: int) -> None: ...
    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> Iterable[Segment]: ...
    def __rich_measure__(
        self, console: Console, options: ConsoleOptions
    ) -> Measurement: ...
    def render(self, console: Console, end: str = ...) -> Iterable[Segment]: ...
    def join(self, lines: Iterable["Text"]) -> "Text": ...
    def expand_tabs(self, tab_size: Optional[int] = ...) -> None: ...
    def truncate(
        self,
        max_width: int,
        *,
        overflow: Optional[OverflowMethod] = ...,
        pad: bool = ...,
    ) -> None: ...
    def _trim_spans(self) -> None: ...
    def pad(self, count: int, character: str = ...) -> None: ...
    def pad_left(self, count: int, character: str = ...) -> None: ...
    def pad_right(self, count: int, character: str = ...) -> None: ...
    def align(self, align: AlignMethod, width: int, character: str = ...) -> None: ...
    def append(
        self, text: Union["Text", str], style: Optional[Union[str, Style]] = ...
    ) -> "Text": ...
    def append_text(self, text: "Text") -> "Text": ...
    def append_tokens(
        self, tokens: Iterable[Tuple[str, Optional[StyleType]]]
    ) -> "Text": ...
    def copy_styles(self, text: "Text") -> None: ...
    def split(
        self,
        separator: str = ...,
        *,
        include_separator: bool = ...,
        allow_blank: bool = ...,
    ) -> Lines: ...
    def divide(self, offsets: Iterable[int]) -> Lines: ...
    def right_crop(self, amount: int = ...) -> None: ...
    def wrap(
        self,
        console: Console,
        width: int,
        *,
        justify: Optional[JustifyMethod] = ...,
        overflow: Optional[OverflowMethod] = ...,
        tab_size: int = ...,
        no_wrap: Optional[bool] = ...,
    ) -> Lines: ...
    def fit(self, width: int) -> Lines: ...
    def detect_indentation(self) -> int: ...
    def with_indent_guides(
        self,
        indent_size: Optional[int] = ...,
        *,
        character: str = ...,
        style: StyleType = ...,
    ) -> "Text": ...