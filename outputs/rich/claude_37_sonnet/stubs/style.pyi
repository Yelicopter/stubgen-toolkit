import sys
from functools import lru_cache, partial
from marshal import dumps, loads
from random import randint
from typing import Any, Callable, Dict, Iterable, List, Optional, Tuple, Type, Union, cast

from . import errors
from .color import Color, ColorParseError, ColorSystem, blend_rgb
from .repr import Result, rich_repr
from .terminal_theme import DEFAULT_TERMINAL_THEME, TerminalTheme

StyleType = Union[str, "Style"]

class _Bit:
    bit: int
    def __init__(self, bit_no: int) -> None: ...
    def __get__(self, obj: "Style", objtype: Type["Style"]) -> Optional[bool]: ...

@rich_repr
class Style:
    _color: Optional[Color]
    _bgcolor: Optional[Color]
    _attributes: int
    _set_attributes: int
    _hash: Optional[int]
    _null: bool
    _meta: Optional[bytes]
    _style_map: Dict[int, str]
    STYLE_ATTRIBUTES: Dict[str, str]
    def __init__(
        self,
        *,
        color: Optional[Union[Color, str]] = ...,
        bgcolor: Optional[Union[Color, str]] = ...,
        bold: Optional[bool] = ...,
        dim: Optional[bool] = ...,
        italic: Optional[bool] = ...,
        underline: Optional[bool] = ...,
        blink: Optional[bool] = ...,
        blink2: Optional[bool] = ...,
        reverse: Optional[bool] = ...,
        conceal: Optional[bool] = ...,
        strike: Optional[bool] = ...,
        underline2: Optional[bool] = ...,
        frame: Optional[bool] = ...,
        encircle: Optional[bool] = ...,
        overline: Optional[bool] = ...,
        link: Optional[str] = ...,
        meta: Optional[Dict[str, Any]] = ...,
    ) -> None: ...
    _ansi: Optional[str]
    _style_definition: Optional[str]
    _link: Optional[str]
    _link_id: str
    @classmethod
    def null(cls) -> "Style": ...
    @classmethod
    def from_color(
        cls, color: Optional[Color] = ..., bgcolor: Optional[Color] = ...
    ) -> "Style": ...
    @classmethod
    def from_meta(cls, meta: Optional[Dict[str, Any]]) -> "Style": ...
    @classmethod
    def on(cls, meta: Optional[Dict[str, Any]] = ..., **handlers: Any) -> "Style": ...
    bold: Optional[bool]
    dim: Optional[bool]
    italic: Optional[bool]
    underline: Optional[bool]
    blink: Optional[bool]
    blink2: Optional[bool]
    reverse: Optional[bool]
    conceal: Optional[bool]
    strike: Optional[bool]
    underline2: Optional[bool]
    frame: Optional[bool]
    encircle: Optional[bool]
    overline: Optional[bool]
    @property
    def link_id(self) -> str: ...
    def __str__(self) -> str: ...
    def __bool__(self) -> bool: ...
    def _make_ansi_codes(self, color_system: ColorSystem) -> str: ...
    @classmethod
    @lru_cache(maxsize=1024)
    def normalize(cls, style: str) -> str: ...
    @classmethod
    def pick_first(cls, *values: Optional[StyleType]) -> StyleType: ...
    def __rich_repr__(self) -> Result: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    @property
    def color(self) -> Optional[Color]: ...
    @property
    def bgcolor(self) -> Optional[Color]: ...
    @property
    def link(self) -> Optional[str]: ...
    @property
    def transparent_background(self) -> bool: ...
    @property
    def background_style(self) -> "Style": ...
    @property
    def meta(self) -> Dict[str, Any]: ...
    @property
    def without_color(self) -> "Style": ...
    @classmethod
    @lru_cache(maxsize=4096)
    def parse(cls, style_definition: str) -> "Style": ...
    @lru_cache(maxsize=1024)
    def get_html_style(self, theme: Optional[TerminalTheme] = ...) -> str: ...
    @classmethod
    def combine(cls, styles: Iterable["Style"]) -> "Style": ...
    @classmethod
    def chain(cls, *styles: "Style") -> "Style": ...
    def copy(self) -> "Style": ...
    @lru_cache(maxsize=128)
    def clear_meta_and_links(self) -> "Style": ...
    def update_link(self, link: Optional[str] = ...) -> "Style": ...
    def render(
        self,
        text: str = ...,
        *,
        color_system: Optional[ColorSystem] = ...,
        legacy_windows: bool = ...,
    ) -> str: ...
    def test(self, text: Optional[str] = ...) -> None: ...
    @lru_cache(maxsize=1024)
    def _add(self, style: Optional["Style"]) -> "Style": ...
    def __add__(self, style: Optional["Style"]) -> "Style": ...

NULL_STYLE: Style

class StyleStack:
    def __init__(self, default_style: "Style") -> None: ...
    _stack: List[Style]
    def __repr__(self) -> str: ...
    @property
    def current(self) -> Style: ...
    def push(self, style: Style) -> None: ...
    def pop(self) -> Style: ...