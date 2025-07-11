import inspect
import linecache
import os
import sys
from dataclasses import dataclass, field
from itertools import islice
from traceback import walk_tb
from types import ModuleType, TracebackType
from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    List,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
)

from pygments.lexers import guess_lexer_for_filename
from pygments.token import Comment, Keyword, Name, Number, Operator, String
from pygments.token import Text as TextToken
from pygments.token import Token
from pygments.util import ClassNotFound

from . import pretty
from ._loop import loop_first_last, loop_last
from .columns import Columns
from .console import (
    Console,
    ConsoleOptions,
    ConsoleRenderable,
    Group,
    RenderResult,
    group,
)
from .constrain import Constrain
from .highlighter import RegexHighlighter, ReprHighlighter
from .panel import Panel
from .scope import render_scope
from .style import Style
from .syntax import Syntax, SyntaxPosition
from .text import Text
from .theme import Theme

WINDOWS = sys.platform == "win32"

LOCALS_MAX_LENGTH = 10
LOCALS_MAX_STRING = 80


def _iter_syntax_lines(
    start                , end                
)                                  :
    ...

def install(
    *,
    console                    = None,
    width                = 100,
    code_width                = 88,
    extra_lines      = 3,
    theme                = None,
    word_wrap       = False,
    show_locals       = False,
    locals_max_length      = LOCALS_MAX_LENGTH,
    locals_max_string      = LOCALS_MAX_STRING,
    locals_hide_dunder       = True,
    locals_hide_sunder                 = None,
    indent_guides       = True,
    suppress                                   = (),
    max_frames      = 100,
)                                                                                :
    ...

class PathHighlighter(RegexHighlighter):
    ...

class Traceback:
    ...