from __future__ import annotations

from dataclasses import dataclass, field
from types import ModuleType, TracebackType
from typing import Any, Callable, Dict, Iterable, List, Optional, Sequence, Tuple, Type, Union

from pygments.token import TokenType

from rich.console import Console, ConsoleOptions, ConsoleRenderable, RenderResult
from rich.highlighter import RegexHighlighter
from rich.pretty import Node
from rich.style import Style
from rich.syntax import Syntax, SyntaxPosition, SyntaxTheme
from rich.text import Text

WINDOWS: bool
LOCALS_MAX_LENGTH: int
LOCALS_MAX_STRING: int

def _iter_syntax_lines(start: SyntaxPosition, end: SyntaxPosition) -> Iterable[Tuple[int, int, int]]: ...
def install(*, console: Optional[Console] = None, width: Optional[int] = 100, code_width: Optional[int] = 88, extra_lines: int = 3, theme: Optional[str] = None, word_wrap: bool = False, show_locals: bool = False, locals_max_length: int = ..., locals_max_string: int = ..., locals_hide_dunder: bool = True, locals_hide_sunder: Optional[bool] = None, indent_guides: bool = True, suppress: Iterable[Union[str, ModuleType]] = (), max_frames: int = 100) -> Callable[[Type[BaseException], BaseException, Optional[TracebackType]], Any]: ...

@dataclass
class Frame:
    filename: str
    lineno: int
    name: str
    line: str
    locals: Optional[Dict[str, Node]]
    last_instruction: Optional[Tuple[Tuple[int, int], Tuple[int, int]]]

@dataclass
class _SyntaxError:
    offset: int
    filename: str
    line: str
    lineno: int
    msg: str
    notes: List[str]

@dataclass
class Stack:
    exc_type: str
    exc_value: str
    syntax_error: Optional[_SyntaxError]
    is_cause: bool
    frames: List[Frame]
    notes: List[str]
    is_group: bool
    exceptions: List[Trace]

@dataclass
class Trace:
    stacks: List[Stack]

class PathHighlighter(RegexHighlighter):
    highlights: List[str]

class Traceback:
    LEXERS: Dict[str, str]
    trace: Trace
    width: Optional[int]
    code_width: Optional[int]
    extra_lines: int
    theme: SyntaxTheme
    word_wrap: bool
    show_locals: bool
    indent_guides: bool
    locals_max_length: int
    locals_max_string: int
    locals_hide_dunder: bool
    locals_hide_sunder: bool
    suppress: Sequence[str]
    max_frames: int
    def __init__(self, trace: Optional[Trace] = None, *, width: Optional[int] = 100, code_width: Optional[int] = 88, extra_lines: int = 3, theme: Optional[str] = None, word_wrap: bool = False, show_locals: bool = False, locals_max_length: int = ..., locals_max_string: int = ..., locals_hide_dunder: bool = True, locals_hide_sunder: bool = False, indent_guides: bool = True, suppress: Iterable[Union[str, ModuleType]] = (), max_frames: int = 100) -> None: ...
    @classmethod
    def from_exception(cls, exc_type: Type[Any], exc_value: BaseException, traceback: Optional[TracebackType], *, width: Optional[int] = 100, code_width: Optional[int] = 88, extra_lines: int = 3, theme: Optional[str] = None, word_wrap: bool = False, show_locals: bool = False, locals_max_length: int = ..., locals_max_string: int = ..., locals_hide_dunder: bool = True, locals_hide_sunder: bool = False, indent_guides: bool = True, suppress: Iterable[Union[str, ModuleType]] = (), max_frames: int = 100) -> Traceback: ...
    @classmethod
    def extract(cls, exc_type: Type[BaseException], exc_value: BaseException, traceback: Optional[TracebackType], *, show_locals: bool = False, locals_max_length: int = ..., locals_max_string: int = ..., locals_hide_dunder: bool = True, locals_hide_sunder: bool = False) -> Trace: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
    def _render_syntax_error(self, syntax_error: _SyntaxError) -> RenderResult: ...
    @classmethod
    def _guess_lexer(cls, filename: str, code: str) -> str: ...
    def _render_stack(self, stack: Stack) -> RenderResult: ...