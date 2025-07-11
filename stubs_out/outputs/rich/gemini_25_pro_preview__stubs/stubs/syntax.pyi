import abc
from abc import ABC, abstractmethod
from pathlib import Path as Path
from pygments.lexer import Lexer
from pygments.style import Style as PygmentsStyle
from pygments.token import TokenType as TokenType
from rich.console import Console as Console, ConsoleOptions as ConsoleOptions, RenderResult as RenderResult
from rich.jupyter import JupyterMixin
from rich.measure import Measurement as Measurement
from rich.padding import PaddingDimensions as PaddingDimensions
from rich.style import Style, StyleType as StyleType
from rich.text import Text as Text
from typing import Dict, NamedTuple, Optional, Set, Tuple, Type, Union

WINDOWS: bool
DEFAULT_THEME: str
ANSI_LIGHT: Dict[TokenType, Style]
ANSI_DARK: Dict[TokenType, Style]
RICH_SYNTAX_THEMES: Dict[str, Dict[TokenType, Style]]
NUMBERS_COLUMN_DEFAULT_PADDING: int

class SyntaxTheme(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def get_style_for_token(self, token_type: TokenType) -> Style: ...
    @abstractmethod
    def get_background_style(self) -> Style: ...

class PygmentsSyntaxTheme(SyntaxTheme):
    def __init__(self, theme: Union[str, Type[PygmentsStyle]]) -> None: ...
    def get_style_for_token(self, token_type: TokenType) -> Style: ...
    def get_background_style(self) -> Style: ...

class ANSISyntaxTheme(SyntaxTheme):
    style_map: Dict[TokenType, Style]
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
    code: str
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
    @classmethod
    def get_theme(cls, name: Union[str, SyntaxTheme]) -> SyntaxTheme: ...
    def __init__(self, code: str, lexer: Union[Lexer, str], *, theme: Union[str, SyntaxTheme] = ..., dedent: bool = ..., line_numbers: bool = ..., start_line: int = ..., line_range: Optional[Tuple[Optional[int], Optional[int]]] = ..., highlight_lines: Optional[Set[int]] = ..., code_width: Optional[int] = ..., tab_size: int = ..., word_wrap: bool = ..., background_color: Optional[str] = ..., indent_guides: bool = ..., padding: PaddingDimensions = ...) -> None: ...
    @classmethod
    def from_path(cls, path: str, encoding: str = ..., lexer: Optional[Union[Lexer, str]] = ..., theme: Union[str, SyntaxTheme] = ..., dedent: bool = ..., line_numbers: bool = ..., line_range: Optional[Tuple[int, int]] = ..., start_line: int = ..., highlight_lines: Optional[Set[int]] = ..., code_width: Optional[int] = ..., tab_size: int = ..., word_wrap: bool = ..., background_color: Optional[str] = ..., indent_guides: bool = ..., padding: PaddingDimensions = ...) -> Syntax: ...
    @classmethod
    def guess_lexer(cls, path: str, code: Optional[str] = ...) -> str: ...
    @property
    def lexer(self) -> Optional[Lexer]: ...
    @property
    def default_lexer(self) -> Lexer: ...
    def highlight(self, code: str, line_range: Optional[Tuple[Optional[int], Optional[int]]] = ...) -> Text: ...
    def stylize_range(self, style: StyleType, start: SyntaxPosition, end: SyntaxPosition, style_before: bool = ...) -> None: ...
    def __rich_measure__(self, console: Console, options: ConsoleOptions) -> Measurement: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
