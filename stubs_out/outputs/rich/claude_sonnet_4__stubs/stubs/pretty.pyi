from . import get_console as get_console
from ._loop import loop_last as loop_last
from ._pick import pick_bool as pick_bool
from .abc import RichRenderable as RichRenderable
from .cells import cell_len as cell_len
from .console import Console as Console, ConsoleOptions as ConsoleOptions, HighlighterType as HighlighterType, JustifyMethod as JustifyMethod, OverflowMethod as OverflowMethod, RenderResult as RenderResult
from .highlighter import ReprHighlighter as ReprHighlighter
from .jupyter import JupyterMixin as JupyterMixin, JupyterRenderable as JupyterRenderable
from .measure import Measurement as Measurement
from .text import Text as Text
from array import array as array
from collections import Counter as Counter, UserDict as UserDict, UserList as UserList, defaultdict as defaultdict, deque as deque
from dataclasses import fields as fields, is_dataclass as is_dataclass
from inspect import isclass as isclass
from itertools import islice as islice
from rich.repr import RichReprResult as RichReprResult
from types import MappingProxyType as MappingProxyType
from typing import Any, Iterable, List, Optional

def install(console: Optional['Console'] = ..., overflow: str = ..., crop: bool = ..., indent_guides: bool = ..., max_length: Optional[int] = ..., max_string: Optional[int] = ..., max_depth: Optional[int] = ..., expand_all: bool = ...) -> None: ...

class Pretty(JupyterMixin):
    def __init__(self, _object: Any, highlighter: Optional['HighlighterType'] = ..., *, indent_size: int = ..., justify: Optional['JustifyMethod'] = ..., overflow: Optional['OverflowMethod'] = ..., no_wrap: bool = ..., indent_guides: bool = ..., max_length: Optional[int] = ..., max_string: Optional[int] = ..., max_depth: Optional[int] = ..., expand_all: bool = ..., margin: int = ..., insert_line: bool = ...) -> None: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
    def __rich_measure__(self, console: Console, options: ConsoleOptions) -> Measurement: ...

class Node:
    key_repr: str
    value_repr: str
    open_brace: str
    close_brace: str
    empty: str
    last: bool
    is_tuple: bool
    is_namedtuple: bool
    children: Optional[List['Node']]
    key_separator: str
    separator: str
    def iter_tokens(self) -> Iterable[str]: ...
    def check_length(self, start_length: int, max_length: int) -> bool: ...
    def render(self, max_width: int = ..., indent_size: int = ..., expand_all: bool = ...) -> str: ...
    def __init__(self, key_repr, value_repr, open_brace, close_brace, empty, last, is_tuple, is_namedtuple, children, key_separator, separator) -> None: ...

def is_expandable(obj: Any) -> bool: ...
def traverse(_object: Any, max_length: Optional[int] = ..., max_string: Optional[int] = ..., max_depth: Optional[int] = ...) -> Node: ...
def pretty_repr(_object: Any, *, max_width: int = ..., indent_size: int = ..., max_length: Optional[int] = ..., max_string: Optional[int] = ..., max_depth: Optional[int] = ..., expand_all: bool = ...) -> str: ...
def pprint(_object: Any, *, console: Optional['Console'] = ..., indent_guides: bool = ..., max_length: Optional[int] = ..., max_string: Optional[int] = ..., max_depth: Optional[int] = ..., expand_all: bool = ...) -> None: ...
