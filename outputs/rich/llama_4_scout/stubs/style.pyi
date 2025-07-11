import sys
from functools import lru_cache
from marshal import dumps, loads
from random import randint
from typing import Any, Dict, Iterable, List, Optional, Type, Union, cast

from . import errors
from .color import Color, ColorParseError, ColorSystem, blend_rgb
from .repr import Result, rich_repr
from .terminal_theme import DEFAULT_TERMINAL_THEME, TerminalTheme

StyleType = Union[str, "Style"]


class _Bit:
    ...

@rich_repr
class Style:
    """A terminal style.

    A terminal style consists of a color (`color`), a background color (`bgcolor`), and a number of attributes, such
    as bold, italic etc. The attributes have 3 states: they can either be on
    (``True``), off (``False``), or not set (``None``).

    Args:
        color (Union[Color, str], optional): Color of terminal text. Defaults to None.
        bgcolor (Union[Color, str], optional): Color of terminal background. Defaults to None.
        bold (bool, optional): Enable bold text. Defaults to None.
        dim (bool, optional): Enable dim text. Defaults to None.
        italic (bool, optional): Enable italic text. Defaults to None.
        underline (bool, optional): Enable underlined text. Defaults to None.
        blink (bool, optional): Enabled blinking text. Defaults to None.
        blink2 (bool, optional): Enable fast blinking text. Defaults to None.
        reverse (bool, optional): Enabled reverse text. Defaults to None.
        conceal (bool, optional): Enable concealed text. Defaults to None.
        strike (bool, optional): Enable strikethrough text. Defaults to None.
        underline2 (bool, optional): Enable doubly underlined text. Defaults to None.
        frame (bool, optional): Enable framed text. Defaults to None.
        encircle (bool, optional): Enable encircled text. Defaults to None.
        overline (bool, optional): Enable overlined text. Defaults to None.
        link (str, link): Link URL. Defaults to None.

    """

    def __init__(
        self,
        *,
        color: Optional[Union[Color, str]] = None,
        bgcolor: Optional[Union[Color, str]] = None,
        bold: Optional[bool] = None,
        dim: Optional[bool] = None,
        italic: Optional[bool] = None,
        underline: Optional[bool] = None,
        blink: Optional[bool] = None,
        blink2: Optional[bool] = None,
        reverse: Optional[bool] = None,
        conceal: Optional[bool] = None,
        strike: Optional[bool] = None,
        underline2: Optional[bool] = None,
        frame: Optional[bool] = None,
        encircle: Optional[bool] = None,
        overline: Optional[bool] = None,
        link: Optional[str] = None,
        meta: Optional[Dict[str, Any]] = None,
    ) -> None:
        ...

    @classmethod
    def null(cls) -> "Style":
        ...

    @classmethod
    def from_color(
        cls, color: Optional[Color] = None, bgcolor: Optional[Color] = None
    ) -> "Style":
        ...

    @classmethod
    def from_meta(cls, meta: Dict[str, Any]) -> "Style":
        ...

    @classmethod
    def on(cls, meta: Optional[Dict[str, Any]], **handlers: Any) -> "Style":
        ...

    @property
    def link_id(self) -> str:
        ...

    def __str__(self) -> str:
        ...

    def __bool__(self) -> bool:
        ...

    def _make_ansi_codes(self, color_system: ColorSystem) -> str:
        ...

    @classmethod
    @lru_cache(maxsize=1024)
    def normalize(cls, style: str) -> str:
        ...

    @classmethod
    def pick_first(cls, *values: Optional[Style]) -> Style:
        ...

    def __rich_repr__(self) -> Result:
        ...

    def __eq__(self, other: object) -> bool:
        ...

    def __ne__(self, other: object) -> bool:
        ...

    def __hash__(self) -> int:
        ...

    @property
    def color(self) -> Optional[Color]:
        ...

    @property
    def bgcolor(self) -> Optional[Color]:
        ...

    @property
    def link(self) -> Optional[str]:
        ...

    @property
    def transparent_background(self) -> bool:
        ...

    @property
    def background_style(self) -> "Style":
        ...

    @property
    def meta(self) -> Dict[str, Any]:
        ...

    @property
    def without_color(self) -> "Style":
        ...

    @classmethod
    @lru_cache(maxsize=4096)
    def parse(cls, style_definition: str) -> "Style":
        ...

    @lru_cache(maxsize=1024)
    def get_html_style(self, theme: Optional["TerminalTheme"] = None) -> str:
        ...

    @classmethod
    def combine(cls, styles: Iterable["Style"]) -> "Style":
        ...

    @classmethod
    def chain(cls, *styles: Style) -> "Style":
        ...

    def copy(self) -> "Style":
        ...

    @lru_cache(maxsize=128)
    def clear_meta_and_links(self) -> "Style":
        ...

    def update_link(self, link: Optional[str] = None) -> "Style":
        ...

    def render(
        self,
        text: str = "",
        *,
        color_system: Optional[ColorSystem] = ColorSystem.TRUECOLOR,
        legacy_windows: bool = False,
    ) -> str:
        ...

    def test(self, text: Optional[str] = None) -> None:
        ...

    @lru_cache(maxsize=1024)
    def _add(self, style: Style) -> "Style":
        ...

    def __add__(self, style: Style) -> Style:
        ...

NULL_STYLE = Style()


class StyleStack:
    """A stack of styles."""

    __slots__ = ["_stack"]

    def __init__(self, default_style: Style) -> None:
        ...

    def __repr__(self) -> str:
        ...

    @property
    def current(self) -> Style:
        ...

    def push(self, style: Style) -> None:
        ...

    def pop(self) -> Style:
        ...

    def __getitem__(self, index: int) -> Style:
        ...