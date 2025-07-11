import abc
from ._loop import loop_first as loop_first
from .cells import cell_len as cell_len
from .color import Color as Color, blend_rgb as blend_rgb
from .console import Console as Console, ConsoleOptions as ConsoleOptions, JustifyMethod as JustifyMethod, RenderResult as RenderResult
from .jupyter import JupyterMixin as JupyterMixin
from .measure import Measurement as Measurement
from .segment import Segment as Segment, Segments as Segments
from .style import Style as Style, StyleType as StyleType
from .text import Text as Text
from abc import ABC, abstractmethod
from pathlib import Path as Path
from pygments.lexer import Lexer
from pygments.lexers import get_lexer_by_name as get_lexer_by_name, guess_lexer_for_filename as guess_lexer_for_filename
from pygments.style import Style as PygmentsStyle
from pygments.styles import get_style_by_name as get_style_by_name
from pygments.token import Comment as Comment, Error as Error, Generic as Generic, Keyword as Keyword, Name as Name, Number as Number, Operator as Operator, String as String, Token as Token, Whitespace as Whitespace
from pygments.util import ClassNotFound as ClassNotFound
from rich.containers import Lines as Lines
from rich.padding import Padding as Padding, PaddingDimensions as PaddingDimensions
from typing import Dict, NamedTuple, Optional, Set, Tuple, Type, Union

TokenType = Tuple[str, ...]
SyntaxPosition = Tuple[int, int]

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
    def __init__(self, style_map: Dict[TokenType, Style]) -> None: ...
    def get_style_for_token(self, token_type: TokenType) -> Style: ...
    def get_background_style(self) -> Style: ...

class _SyntaxHighlightRange(NamedTuple):
    style: StyleType
    start: SyntaxPosition
    end: SyntaxPosition
    style_before: bool

class Syntax(JupyterMixin):
    def __init__(self, code: str, lexer: Union[Lexer, str], *, theme: Union[str, SyntaxTheme] = ..., dedent: bool = ..., line_numbers: bool = ..., start_line: int = ..., line_range: Optional[Tuple[Optional[int], Optional[int]]] = ..., highlight_lines: Optional[Set[int]] = ..., code_width: Optional[int] = ..., tab_size: int = ..., word_wrap: bool = ..., background_color: Optional[str] = ..., indent_guides: bool = ..., padding: PaddingDimensions = ...) -> None: ...
    @classmethod
    def get_theme(cls, name: Union[str, SyntaxTheme]) -> SyntaxTheme: ...
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
