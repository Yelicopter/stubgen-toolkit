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
SyntaxPosition = Tuple[int, int]

class SyntaxTheme(ABC):
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
    style_before: bool = False

class Syntax(JupyterMixin):
    def __init__(
        self,
        code: str,
        lexer: Union[Lexer, str],
        *,
        theme: Union[str, SyntaxTheme] = "monokai",
        dedent: bool = False,
        line_numbers: bool = False,
        start_line: int = 1,
        line_range: Optional[Tuple[Optional[int], Optional[int]]] = None,
        highlight_lines: Optional[Set[int]] = None,
        code_width: Optional[int] = None,
        tab_size: int = 4,
        word_wrap: bool = False,
        background_color: Optional[str] = None,
        indent_guides: bool = False,
        padding: PaddingDimensions = 0,
    ) -> None: ...
    
    @classmethod
    def get_theme(cls, name: Union[str, SyntaxTheme]) -> SyntaxTheme: ...
    
    @classmethod
    def from_path(
        cls,
        path: str,
        encoding: str = "utf-8",
        lexer: Optional[Union[Lexer, str]] = None,
        theme: Union[str, SyntaxTheme] = "monokai",
        dedent: bool = False,
        line_numbers: bool = False,
        line_range: Optional[Tuple[int, int]] = None,
        start_line: int = 1,
        highlight_lines: Optional[Set[int]] = None,
        code_width: Optional[int] = None,
        tab_size: int = 4,
        word_wrap: bool = False,
        background_color: Optional[str] = None,
        indent_guides: bool = False,
        padding: PaddingDimensions = 0,
    ) -> "Syntax": ...
    
    @classmethod
    def guess_lexer(cls, path: str, code: Optional[str] = None) -> str: ...
    
    @property
    def lexer(self) -> Optional[Lexer]: ...
    
    @property
    def default_lexer(self) -> Lexer: ...
    
    def highlight(
        self,
        code: str,
        line_range: Optional[Tuple[Optional[int], Optional[int]]] = None,
    ) -> Text: ...
    
    def stylize_range(
        self,
        style: StyleType,
        start: SyntaxPosition,
        end: SyntaxPosition,
        style_before: bool = False,
    ) -> None: ...
    
    def __rich_measure__(
        self, console: "Console", options: "ConsoleOptions"
    ) -> "Measurement": ...
    
    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult: ...