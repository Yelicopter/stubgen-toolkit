import inspect
import linecache
import os
import sys
from dataclasses import dataclass, field
from itertools import islice
from traceback import walk_tb
from types import ModuleType, TracebackType
from typing import Any, Callable, Dict, Iterable, List, NamedTuple, Optional, Sequence, Tuple, Type, Union

from pygments.lexers import guess_lexer_for_filename
from pygments.token import Comment, Keyword, Name, Number, Operator, String, Text as TextToken, Token
from pygments.util import ClassNotFound

from . import pretty
from ._loop import loop_first_last, loop_last
from .columns import Columns
from .console import Console, ConsoleOptions, ConsoleRenderable, Group, RenderResult, group
from .constrain import Constrain
from .highlighter import RegexHighlighter, ReprHighlighter
from .panel import Panel
from .scope import render_scope
from .style import Style
from .syntax import Syntax, SyntaxPosition
from .text import Text
from .theme import Theme

WINDOWS: bool
LOCALS_MAX_LENGTH: int
LOCALS_MAX_STRING: int

def _iter_syntax_lines(
    start: SyntaxPosition, end: SyntaxPosition
) -> Iterable[Tuple[int, int, int]]: ...

def install(
    *,
    console: Optional[Console] = ...,
    width: Optional[int] = ...,
    code_width: Optional[int] = ...,
    extra_lines: int = ...,
    theme: Optional[str] = ...,
    word_wrap: bool = ...,
    show_locals: bool = ...,
    locals_max_length: int = ...,
    locals_max_string: int = ...,
    locals_hide_dunder: bool = ...,
    locals_hide_sunder: Optional[bool] = ...,
    indent_guides: bool = ...,
    suppress: Iterable[Union[str, ModuleType]] = ...,
    max_frames: int = ...,
) -> Callable[[Type[BaseException], BaseException, Optional[TracebackType]], Any]: ...

@dataclass
class Frame:
    filename: str
    lineno: int
    name: str
    line: str = ...
    locals: Optional[Dict[str, pretty.Node]] = ...
    last_instruction: Optional[Tuple[Tuple[int, int], Tuple[int, int]]] = ...

@dataclass
class _SyntaxError:
    offset: int
    filename: str
    line: str
    lineno: int
    msg: str
    notes: List[str] = field(default_factory=list)

@dataclass
class Stack:
    exc_type: str
    exc_value: str
    syntax_error: Optional[_SyntaxError] = ...
    is_cause: bool = ...
    frames: List[Frame] = field(default_factory=list)
    notes: List[str] = field(default_factory=list)
    is_group: bool = ...
    exceptions: List["Trace"] = field(default_factory=list)

@dataclass
class Trace:
    stacks: List[Stack]

class PathHighlighter(RegexHighlighter):
    highlights: List[str]

class Traceback:
    LEXERS: Dict[str, str]
    def __init__(
        self,
        trace: Optional[Trace] = ...,
        *,
        width: Optional[int] = ...,
        code_width: Optional[int] = ...,
        extra_lines: int = ...,
        theme: Optional[str] = ...,
        word_wrap: bool = ...,
        show_locals: bool = ...,
        locals_max_length: int = ...,
        locals_max_string: int = ...,
        locals_hide_dunder: bool = ...,
        locals_hide_sunder: bool = ...,
        indent_guides: bool = ...,
        suppress: Iterable[Union[str, ModuleType]] = ...,
        max_frames: int = ...,
    ) -> None: ...
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
    @classmethod
    def from_exception(
        cls,
        exc_type: Type[Any],
        exc_value: BaseException,
        traceback: Optional[TracebackType],
        *,
        width: Optional[int] = ...,
        code_width: Optional[int] = ...,
        extra_lines: int = ...,
        theme: Optional[str] = ...,
        word_wrap: bool = ...,
        show_locals: bool = ...,
        locals_max_length: int = ...,
        locals_max_string: int = ...,
        locals_hide_dunder: bool = ...,
        locals_hide_sunder: bool = ...,
        indent_guides: bool = ...,
        suppress: Iterable[Union[str, ModuleType]] = ...,
        max_frames: int = ...,
    ) -> "Traceback": ...
    @classmethod
    def extract(
        cls,
        exc_type: Type[BaseException],
        exc_value: BaseException,
        traceback: Optional[TracebackType],
        *,
        show_locals: bool = ...,
        locals_max_length: int = ...,
        locals_max_string: int = ...,
        locals_hide_dunder: bool = ...,
        locals_hide_sunder: bool = ...,
    ) -> Trace: ...
    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult: ...
    @group()
    def _render_syntax_error(self, syntax_error: _SyntaxError) -> RenderResult: ...
    @classmethod
    def _guess_lexer(cls, filename: str, code: str) -> str: ...
    @group()
    def _render_stack(self, stack: Stack) -> RenderResult: ...