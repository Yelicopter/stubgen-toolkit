from . import pretty as pretty
from ._loop import loop_first_last as loop_first_last, loop_last as loop_last
from .columns import Columns as Columns
from .console import Console as Console, ConsoleOptions as ConsoleOptions, ConsoleRenderable as ConsoleRenderable, Group as Group, RenderResult as RenderResult, group as group
from .constrain import Constrain as Constrain
from .highlighter import RegexHighlighter as RegexHighlighter, ReprHighlighter as ReprHighlighter
from .panel import Panel as Panel
from .scope import render_scope as render_scope
from .style import Style as Style
from .syntax import Syntax as Syntax, SyntaxPosition as SyntaxPosition
from .text import Text as Text
from .theme import Theme as Theme
from itertools import islice as islice
from pygments.lexers import guess_lexer_for_filename as guess_lexer_for_filename
from pygments.token import Comment as Comment, Keyword as Keyword, Name as Name, Number as Number, Operator as Operator, String as String, Token as Token
from pygments.util import ClassNotFound as ClassNotFound
from traceback import walk_tb as walk_tb
from types import ModuleType, TracebackType
from typing import Any, Callable, Dict, Iterable, List, Optional, Tuple, Type, Union

def install(*, console: Optional[Console] = ..., width: Optional[int] = ..., code_width: Optional[int] = ..., extra_lines: int = ..., theme: Optional[str] = ..., word_wrap: bool = ..., show_locals: bool = ..., locals_max_length: int = ..., locals_max_string: int = ..., locals_hide_dunder: bool = ..., locals_hide_sunder: Optional[bool] = ..., indent_guides: bool = ..., suppress: Iterable[Union[str, ModuleType]] = ..., max_frames: int = ...) -> Callable[[Type[BaseException], BaseException, Optional[TracebackType]], Any]: ...

class Frame:
    filename: str
    lineno: int
    name: str
    line: str
    locals: Optional[Dict[str, pretty.Node]]
    last_instruction: Optional[Tuple[Tuple[int, int], Tuple[int, int]]]
    def __init__(self, filename, lineno, name, line, locals, last_instruction) -> None: ...

class _SyntaxError:
    offset: int
    filename: str
    line: str
    lineno: int
    msg: str
    notes: List[str]
    def __init__(self, offset, filename, line, lineno, msg, notes) -> None: ...

class Stack:
    exc_type: str
    exc_value: str
    syntax_error: Optional[_SyntaxError]
    is_cause: bool
    frames: List[Frame]
    notes: List[str]
    is_group: bool
    exceptions: List['Trace']
    def __init__(self, exc_type, exc_value, syntax_error, is_cause, frames, notes, is_group, exceptions) -> None: ...

class Trace:
    stacks: List[Stack]
    def __init__(self, stacks) -> None: ...

class PathHighlighter(RegexHighlighter):
    highlights: List[str]

class Traceback:
    def __init__(self, trace: Optional[Trace] = ..., *, width: Optional[int] = ..., code_width: Optional[int] = ..., extra_lines: int = ..., theme: Optional[str] = ..., word_wrap: bool = ..., show_locals: bool = ..., locals_max_length: int = ..., locals_max_string: int = ..., locals_hide_dunder: bool = ..., locals_hide_sunder: bool = ..., indent_guides: bool = ..., suppress: Iterable[Union[str, ModuleType]] = ..., max_frames: int = ...) -> None: ...
    @classmethod
    def from_exception(cls, exc_type: Type[Any], exc_value: BaseException, traceback: Optional[TracebackType], *, width: Optional[int] = ..., code_width: Optional[int] = ..., extra_lines: int = ..., theme: Optional[str] = ..., word_wrap: bool = ..., show_locals: bool = ..., locals_max_length: int = ..., locals_max_string: int = ..., locals_hide_dunder: bool = ..., locals_hide_sunder: bool = ..., indent_guides: bool = ..., suppress: Iterable[Union[str, ModuleType]] = ..., max_frames: int = ...) -> Traceback: ...
    @classmethod
    def extract(cls, exc_type: Type[BaseException], exc_value: BaseException, traceback: Optional[TracebackType], *, show_locals: bool = ..., locals_max_length: int = ..., locals_max_string: int = ..., locals_hide_dunder: bool = ..., locals_hide_sunder: bool = ...) -> Trace: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
