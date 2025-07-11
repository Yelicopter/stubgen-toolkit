from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict, Iterable, List, NamedTuple, Optional, Sequence, Set, Tuple, Type, Union

from pygments.lexer import Lexer
from pygments.style import Style as PygmentsStyle

from rich.console import Console, ConsoleOptions, RenderResult
from rich.jupyter import JupyterMixin
from rich.measure import Measurement
from rich.padding import PaddingDimensions
from rich.segment import Segment
from rich.style import Style, StyleType
from rich.text import Text
from rich.color import Color

WINDOWS: bool
DEFAULT_THEME: str
NUMBERS_COLUMN_DEFAULT_PADDING: int

class TokenType:
    def __init__(self) -> None: ...

ANSI_LIGHT: Dict[TokenType, Style]
ANSI_DARK: Dict[TokenType, Style]
RICH_SYNTAX_THEMES: Dict[str, Dict[TokenType, Style]]

class SyntaxTheme(ABC):
    @abstractmethod
    def get_style_for_token(self, token_type: TokenType) -> Style: ...
    @abstractmethod
    def get_background_style(self) -> Style: ...

class PygmentsSyntaxTheme(SyntaxTheme):
    _style_cache: Dict[TokenType, Style]
    _pygments_style_class: Type[PygmentsStyle]
    _background_color: str
    _background_style: Style
    def __init__(self, theme: Union[str, Type[PygmentsStyle]]) -> None: ...
    def get_style_for_token(self, token_type: TokenType) -> Style: ...
    def get_background_style(self) -> Style: ...

class ANSISyntaxTheme(SyntaxTheme):
    style_map: Dict[TokenType, Style]
    _missing_style: Style
    _background_style: Style
    _style_cache: Dict[TokenType, Style]
    def __init__(self, style_map: Dict[TokenType, Style]) -> None: ...
    def get_style_for_token(self, token_type: TokenType) -> Style: ...
    def get_background_style(self) -> Style: ...

SyntaxPosition = Tuple[int, int]

class _SyntaxHighlightRange(NamedTuple):
    style: StyleType
    start: SyntaxPosition
    end: SyntaxPosition
    style_before: bool

class Syntax(JupyterMixin):
    _pygments_style_class: Type[PygmentsStyle]
    _theme: SyntaxTheme
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
    def get_theme(cls, name: Union[str, SyntaxTheme]) -> SyntaxTheme: ...
    def __init__(self, code: str, lexer: Union[Lexer, str], *, theme: Union[str, SyntaxTheme] = ..., dedent: bool = False, line_numbers: bool = False, start_line: int = 1, line_range: Optional[Tuple[Optional[int], Optional[int]]] = None, highlight_lines: Optional[Set[int]] = None, code_width: Optional[int] = None, tab_size: int = 4, word_wrap: bool = False, background_color: Optional[str] = None, indent_guides: bool = False, padding: PaddingDimensions = 0) -> None: ...
    @classmethod
    def from_path(cls, path: str, encoding: str = "utf-8", lexer: Optional[Union[Lexer, str]] = None, theme: Union[str, SyntaxTheme] = ..., dedent: bool = False, line_numbers: bool = False, line_range: Optional[Tuple[int, int]] = None, start_line: int = 1, highlight_lines: Optional[Set[int]] = None, code_width: Optional[int] = None, tab_size: int = 4, word_wrap: bool = False, background_color: Optional[str] = None, indent_guides: bool = False, padding: PaddingDimensions = 0) -> Syntax: ...
    @classmethod
    def guess_lexer(cls, path: str, code: Optional[str] = None) -> str: ...
    def _get_base_style(self) -> Style: ...
    def _get_token_color(self, token_type: TokenType) -> Optional[Color]: ...
    @property
    def lexer(self) -> Optional[Lexer]: ...
    @property
    def default_lexer(self) -> Lexer: ...
    def highlight(self, code: str, line_range: Optional[Tuple[Optional[int], Optional[int]]] = None) -> Text: ...
    def stylize_range(self, style: StyleType, start: SyntaxPosition, end: SyntaxPosition, style_before: bool = False) -> None: ...
    def _get_line_numbers_color(self, blend: float = 0.3) -> Color: ...
    @property
    def _numbers_column_width(self) -> int: ...
    def _get_number_styles(self, console: Console) -> Tuple[Style, Style, Style]: ...
    def __rich_measure__(self, console: Console, options: ConsoleOptions) -> Measurement: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
    def _get_syntax(self, console: Console, options: ConsoleOptions) -> Iterable[Segment]: ...
    def _apply_stylized_ranges(self, text: Text) -> None: ...
    def _process_code(self, code: str) -> Tuple[bool, str]: ...

def _get_code_index_for_syntax_position(newlines_offsets: Sequence[int], position: SyntaxPosition) -> Optional[int]: ...