import os.path
import re
import sys
import textwrap
from abc import ABC, abstractmethod
from pathlib import Path
from typing import (
    Any,
    Dict,
    Iterable,
    List,
    NamedTuple,
    Optional,
    Sequence,
    Set,
    Tuple,
    Type,
    Union,
)

from pygments.lexer import Lexer
from pygments.lexers import get_lexer_by_name, guess_lexer_for_filename
from pygments.style import Style as PygmentsStyle
from pygments.styles import get_style_by_name
from pygments.token import (
    Comment,
    Error,
    Generic,
    Keyword,
    Name,
    Number,
    Operator,
    String,
    Token,
    Whitespace,
)
from pygments.util import ClassNotFound

from rich.containers import Lines
from rich.padding import Padding, PaddingDimensions

from ._loop import loop_first
from .cells import cell_len
from .color import Color, blend_rgb
from .console import Console, ConsoleOptions, JustifyMethod, RenderResult
from .jupyter import JupyterMixin
from .measure import Measurement
from .segment import Segment, Segments
from .style import Style, StyleType
from .text import Text

TokenType = Tuple[str, ...]

WINDOWS = sys.platform == "win32"
DEFAULT_THEME = "monokai"

# The following styles are based on https://github.com/pygments/pygments/blob/master/pygments/formatters/terminal.py
# A few modifications were made

ANSI_LIGHT                         = {
    Token: Style(),
    Whitespace: Style(color="white"),
    Comment: Style(dim=True),
    Comment.Preproc: Style(color="cyan"),
    Keyword: Style(color="blue"),
    Keyword.Type: Style(color="cyan"),
    Operator.Word: Style(color="magenta"),
    Name.Builtin: Style(color="cyan"),
    Name.Function: Style(color="green"),
    Name.Namespace: Style(color="cyan", underline=True),
    Name.Class: Style(color="green", underline=True),
    Name.Exception: Style(color="cyan"),
    Name.Decorator: Style(color="magenta", bold=True),
    Name.Variable: Style(color="red"),
    Name.Constant: Style(color="red"),
    Name.Attribute: Style(color="cyan"),
    Name.Tag: Style(color="bright_blue"),
    String: Style(color="yellow"),
    Number: Style(color="blue"),
    Generic.Deleted: Style(color="bright_red"),
    Generic.Inserted: Style(color="green"),
    Generic.Heading: Style(bold=True),
    Generic.Subheading: Style(color="magenta", bold=True),
    Generic.Prompt: Style(bold=True),
    Generic.Error: Style(color="bright_red"),
    Error: Style(color="red", underline=True),
}

ANSI_DARK                         = {
    Token: Style(),
    Whitespace: Style(color="bright_black"),
    Comment: Style(dim=True),
    Comment.Preproc: Style(color="bright_cyan"),
    Keyword: Style(color="bright_blue"),
    Keyword.Type: Style(color="bright_cyan"),
    Operator.Word: Style(color="bright_magenta"),
    Name.Builtin: Style(color="bright_cyan"),
    Name.Function: Style(color="bright_green"),
    Name.Namespace: Style(color="bright_cyan", underline=True),
    Name.Class: Style(color="bright_green", underline=True),
    Name.Exception: Style(color="bright_cyan"),
    Name.Decorator: Style(color="bright_magenta", bold=True),
    Name.Variable: Style(color="bright_red"),
    Name.Constant: Style(color="bright_red"),
    Name.Attribute: Style(color="bright_cyan"),
    Name.Tag: Style(color="bright_blue"),
    String: Style(color="yellow"),
    Number: Style(color="bright_blue"),
    Generic.Deleted: Style(color="bright_red"),
    Generic.Inserted: Style(color="green"),
    Generic.Heading: Style(bold=True),
    Generic.Subheading: Style(color="magenta", bold=True),
    Generic.Prompt: Style(bold=True),
    Generic.Error: Style(color="bright_red"),
    Error: Style(color="red", underline=True),
}

RICH_SYNTAX_THEMES = {"ansi_light": ANSI_LIGHT, "ansi_dark": ANSI_DARK}
NUMBERS_COLUMN_DEFAULT_PADDING = 2


class SyntaxTheme(ABC):
    """Base class for a syntax theme."""

    @abstractmethod
    def get_style_for_token(self, token_type: TokenType) -> Style:
        """Get a style for a given Pygments token."""
        ...

    @abstractmethod
    def get_background_style(self) -> Style:
        """Get the background color."""
        ...


class PygmentsSyntaxTheme(SyntaxTheme):
    """Syntax theme that delegates to Pygments theme."""

    def __init__(self, theme: str) -> None:
        self._style_cache: Dict[TokenType, Style] = {}
        if isinstance(theme, str):
            try:
                self._pygments_style_class = get_style_by_name(theme)
            except ClassNotFound:
                self._pygments_style_class = get_style_by_name("default")
        else:
            self._pygments_style_class = theme

        self._background_color = self._pygments_style_class.background_color
        self._background_style = Style(bgcolor=self._background_color)

    def get_style_for_token(self, token_type: TokenType) -> Style:
        """Get a style from a Pygments class."""
        try:
            return self._style_cache[token_type]
        except KeyError:
            try:
                pygments_style = self._pygments_style_class.style_for_token(token_type)
            except KeyError:
                style = Style.null()
            else:
                color = pygments_style["color"]
                bgcolor = pygments_style["bgcolor"]
                style = Style(
                    color="#" + color if color else "#000000",
                    bgcolor="#" + bgcolor if bgcolor else self._background_color,
                    bold=pygments_style["bold"],
                    italic=pygments_style["italic"],
                    underline=pygments_style["underline"],
                )
            self._style_cache[token_type] = style
        return style

    def get_background_style(self) -> Style:
        return self._background_style


class ANSISyntaxTheme(SyntaxTheme):
    """Syntax theme to use standard colors."""

    def __init__(self, style_map: Dict[TokenType, Style]) -> None:
        self.style_map = style_map
        self._missing_style = Style.null()
        self._background_style = Style.null()
        self._style_cache: Dict[TokenType, Style] = {}

    def get_style_for_token(self, token_type: TokenType) -> Style:
        """Look up style in the style map."""
        try:
            return self._style_cache[token_type]
        except KeyError:
            # Styles form a hierarchy
            # We need to go from most to least specific
            # e.g. ("foo", "bar", "baz") to ("foo", "bar")  to ("foo",)
            get_style = self.style_map.get
            token = tuple(token_type)
            style = self._missing_style
            while token:
                _style = get_style(token)
                if _style is not None:
                    style = _style
                    break
                token = token[:-1]
            self._style_cache[token_type] = style
            return style

    def get_background_style(self) -> Style:
        return self._background_style


SyntaxPosition = Tuple[int, int]


class _SyntaxHighlightRange(NamedTuple):
    """
    A range to highlight in a Syntax object.
    `start` and `end` are 2-integers tuples, where the first integer is the line number
    (starting from 1) and the second integer is the column index (starting from 0).
    """

    style: StyleType
    start: SyntaxPosition
    end: SyntaxPosition
    style_before: bool = False


class Syntax(JupyterMixin):
    """Construct a Syntax object to render syntax highlighted code.

    Args:
        code (str): Code to highlight.
        lexer (Lexer | str): Lexer to use (see https://pygments.org/docs/lexers/)
        theme (str, optional): Color theme, aka Pygments style (see https://pygments.org/docs/styles/#getting-a-list-of-available-styles). Defaults to "monokai".
        dedent (bool, optional): Enable stripping of initial whitespace. Defaults to False.
        line_numbers (bool, optional): Enable rendering of line numbers. Defaults to False.
        start_line (int, optional): Starting number for line numbers. Defaults to 1.
        line_range (Tuple[int | None, int | None], optional): If given should be a tuple of the start and end line to render.
            A value of None in the tuple indicates the range is open in that direction.
        highlight_lines (Set[int]): A set of line numbers to highlight.
        code_width: Width of code to render (not including line numbers), or ``None`` to use all available width.
        tab_size (int, optional): Size of tabs. Defaults to 4.
        word_wrap (bool, optional): Enable word wrapping.
        background_color (str, optional): Optional background color, or None to use theme color. Defaults to None.
        indent_guides (bool, optional): Show indent guides. Defaults to False.
        padding (PaddingDimensions): Padding to apply around the syntax. Defaults to 0 (no padding).
    """

    def __init__(
        self,
        code: str,
        lexer: Union[Lexer, str],
        *,
        theme: str = DEFAULT_THEME,
        dedent: bool = False,
        line_numbers: bool = False,
        start_line: int = 1,
        line_range: Optional[Tuple[int, int]] = None,
        highlight_lines: Optional[Set[int]] = None,
        code_width: Optional[int] = None,
        tab_size: int = 4,
        word_wrap: bool = False,
        background_color: Optional[str] = None,
        indent_guides: bool = False,
        padding: PaddingDimensions = 0,
    ) -> None:
        ...

    @classmethod
    def get_theme(cls, name: str) -> SyntaxTheme:
        ...

    def _get_base_style(self) -> Style:
        ...

    def _get_token_color(self, token_type: TokenType) -> Optional[Color]:
        ...

    @property
    def lexer(self) -> Optional[Lexer]:
        ...

    @property
    def default_lexer(self) -> Lexer:
        ...

    def highlight(
        self,
        code: str,
        line_range: Optional[Tuple[int, int]] = None,
    ) -> Text:
        ...

    def stylize_range(
        self,
        style: StyleType,
        start: Tuple[int, int],
        end: Tuple[int, int],
        style_before: bool = False,
    ) -> None:
        ...

    def _apply_stylized_ranges(self, text: Text) -> None:
        ...

    def _process_code(self, code: str) -> Tuple[bool, str]:
        ...

    def __rich_measure__(
        self, console: Console, options: ConsoleOptions
    ) -> Measurement:
        ...

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult:
        ...