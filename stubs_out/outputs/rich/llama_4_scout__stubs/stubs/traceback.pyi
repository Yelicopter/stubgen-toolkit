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
from _typeshed import Incomplete
from dataclasses import dataclass as dataclass, field as field
from itertools import islice as islice
from pygments.lexers import guess_lexer_for_filename as guess_lexer_for_filename
from pygments.token import Comment as Comment, Keyword as Keyword, Name as Name, Number as Number, Operator as Operator, String as String, Token as Token
from pygments.util import ClassNotFound as ClassNotFound
from traceback import walk_tb as walk_tb
from types import ModuleType as ModuleType, TracebackType as TracebackType

WINDOWS: Incomplete
LOCALS_MAX_LENGTH: int
LOCALS_MAX_STRING: int

def install(*, console: Incomplete | None = ..., width: int = ..., code_width: int = ..., extra_lines: int = ..., theme: Incomplete | None = ..., word_wrap: bool = ..., show_locals: bool = ..., locals_max_length=..., locals_max_string=..., locals_hide_dunder: bool = ..., locals_hide_sunder: Incomplete | None = ..., indent_guides: bool = ..., suppress=..., max_frames: int = ...) -> None: ...

class PathHighlighter(RegexHighlighter): ...
class Traceback: ...
