import os.path
import re
import sys
import textwrap
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict, Iterable, List, NamedTuple, Optional, Sequence, Set, Tuple, Type, Union

from pygments.lexer import Lexer
from pygments.lexers import get_lexer_by_name, guess_lexer_for_filename
from pygments.style import Style as PygmentsStyle
from pygments.styles import get_style_by_name
from pygments.token import Comment, Error, Generic, Keyword, Name, Number, Operator, String, Token, Whitespace
from pygments.util import ClassNotFound

from rich.containers import Lines
from rich.padding import Padding, PaddingDimensions

from ._loop import loop_first_last, loop_last
from .cells import cell_len
from .color import Color, blend_rgb
from .console import Console, ConsoleOptions, JustifyMethod, RenderResult
from .jupyter import JupyterMixin
from .measure import Measurement
from .segment import Segment, Segments
from .style import Style, StyleType
from .text import Text

TokenType = Tuple[str, ...]

WINDOWS: bool
DEFAULT_THEME: str
ANSI_LIGHT: Dict[TokenType, Style]
ANSI_DARK: Dict[TokenType, Style]
RICH_SYNTAX_THEMES: Dict[str, Dict[TokenType, Style]]
NUMBERS_COLUMN_DEFAULT_PADDING: int

class SyntaxTheme(ABC):
    @abstractmethod
    def get_style_for_token(self, token_type: TokenType) -> Style: ...
    @abstractmethod
    def get_background_style(self) -> Style: ...

class PygmentsSyntaxTheme(SyntaxTheme):
    def __init__(self, theme: Union[str, Type[PygmentsStyle]]) -> None: ...
    _style_cache: Dict[TokenType, Style]
    _pygments_style_class: Type[PygmentsStyle]
    _background_color: str
    _background_style: Style
    def get_style_for_token(self, token_type: TokenType) -> Style: ...
    def get_background_style(self) -> Style: ...

class ANSISyntaxTheme(SyntaxTheme):
    def __init__(self, style_map: Dict[TokenType, Style]) -> None: ...
    style_map: Dict[TokenType, Style]
    _missing_style: Style
    _background_style: Style
    _style_cache: Dict[TokenType, Style]
    def get_style_for_token(self, token_type: TokenType) -> Style: ...
    def get_background_style(self) -> Style: ...

SyntaxPosition = Tuple[int, int]

class _SyntaxHighlightRange(NamedTuple):
    style: StyleType
    start: SyntaxPosition
    end: SyntaxPosition
    style_before: bool = ...

class Syntax(JupyterMixin):
    _pygments_style_class: Type[PygmentsStyle]
    _theme: SyntaxTheme
    LEXERS: Dict[str, str]
    @classmethod
    def get_theme(cls, name: Union[str, SyntaxTheme]) -> SyntaxTheme: ...
    def __init__(
        self,
        code: str,
        lexer: Union[Lexer, str],
        *,
        theme: Union[str, SyntaxTheme] = ...,
        dedent: bool = ...,
        line_numbers: bool = ...,
        start_line: int = ...,
        line_range: Optional[Tuple[Optional[int], Optional[int]]] = ...,
        highlight_lines: Optional[Set[int]] = ...,
        code_width: Optional[int] = ...,
        tab_size: int = ...,
        word_wrap: bool = ...,
        background_color: Optional[str] = ...,
        indent_guides: bool = ...,
        padding: PaddingDimensions = ...,
    ) -> None: ...
    code: str
    _lexer: Union[Lexer, str]
    dedent: bool
    line_numbers: bool
    start_line: int
    line_range: Optional[Tuple[Optional[int], Optional[int]]]
    highlight_lines: Set[int]
    code_width: Optional[int]
    tab_size: int
    word_wrap: bool
    background_color: Optional[str]
    background_style: Style
    indent_guides: bool
    padding: PaddingDimensions
    _stylized_ranges: List[_SyntaxHighlightRange]
    @classmethod
    def from_path(
        cls,
        path: str,
        encoding: str = ...,
        lexer: Optional[Union[Lexer, str]] = ...,
        theme: Union[str, SyntaxTheme] = ...,
        dedent: bool = ...,
        line_numbers: bool = ...,
        line_range: Optional[Tuple[int, int]] = ...,
        start_line: int = ...,
        highlight_lines: Optional[Set[int]] = ...,
        code_width: Optional[int] = ...,
        tab_size: int = ...,
        word_wrap: bool = ...,
        background_color: Optional[str] = ...,
        indent_guides: bool = ...,
        padding: PaddingDimensions = ...,
    ) -> "Syntax": ...
    @classmethod
    def guess_lexer(cls, path: str, code: Optional[str] = ...) -> str: ...
    def _get_base_style(self) -> Style: ...
    def _get_token_color(self, token_type: TokenType) -> Optional[Color]: ...
    @property
    def lexer(self) -> Optional[Lexer]: ...
    @property
    def default_lexer(self) -> Lexer: ...
    def highlight(
        self,
        code: str,
        line_range: Optional[Tuple[Optional[int], Optional[int]]] = ...,
    ) -> Text: ...
    def stylize_range(
        self,
        style: StyleType,
        start: SyntaxPosition,
        end: SyntaxPosition,
        style_before: bool = ...,
    ) -> None: ...
    def _get_line_numbers_color(self, blend: float = ...) -> Color: ...
    @property
    def _numbers_column_width(self) -> int: ...
    def _get_number_styles(self, console: Console) -> Tuple[Style, Style, Style]: ...
    def __rich_measure__(
        self, console: Console, options: ConsoleOptions
    ) -> Measurement: ...
    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult: ...
    def _get_syntax(
        self,
        console: Console,
        options: ConsoleOptions,
    ) -> Iterable[Segment]: ...
    def _apply_stylized_ranges(self, text: Text) -> None: ...
    def _process_code(self, code: str) -> Tuple[bool, str]: ...

def _get_code_index_for_syntax_position(
    newlines_offsets: Sequence[int], position: SyntaxPosition
) -> Optional[int]: ...