from collections import Counter as Counter, UserDict as UserDict, UserList as UserList
from rich.console import Console as Console, ConsoleOptions as ConsoleOptions, HighlighterType as HighlighterType, JustifyMethod as JustifyMethod, OverflowMethod as OverflowMethod, RenderResult as RenderResult
from rich.jupyter import JupyterMixin
from rich.measure import Measurement as Measurement
from types import MappingProxyType as MappingProxyType
from typing import Any, Iterable, List, Optional

def install(console: Optional[Console] = ..., overflow: OverflowMethod = ..., crop: bool = ..., indent_guides: bool = ..., max_length: Optional[int] = ..., max_string: Optional[int] = ..., max_depth: Optional[int] = ..., expand_all: bool = ...) -> None: ...

class Pretty(JupyterMixin):
    highlighter: HighlighterType
    indent_size: int
    justify: Optional[JustifyMethod]
    overflow: Optional[OverflowMethod]
    no_wrap: bool
    indent_guides: bool
    max_length: Optional[int]
    max_string: Optional[int]
    max_depth: Optional[int]
    expand_all: bool
    margin: int
    insert_line: bool
    def __init__(self, _object: Any, highlighter: Optional[HighlighterType] = ..., *, indent_size: int = ..., justify: Optional[JustifyMethod] = ..., overflow: Optional[OverflowMethod] = ..., no_wrap: bool = ..., indent_guides: bool = ..., max_length: Optional[int] = ..., max_string: Optional[int] = ..., max_depth: Optional[int] = ..., expand_all: bool = ..., margin: int = ..., insert_line: bool = ...) -> None: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
    def __rich_measure__(self, console: Console, options: ConsoleOptions) -> Measurement: ...

def is_expandable(obj: Any) -> bool: ...

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

class _Line:
    parent: Optional['_Line']
    is_root: bool
    node: Optional[Node]
    text: str
    suffix: str
    whitespace: str
    expanded: bool
    last: bool
    @property
    def expandable(self) -> bool: ...
    def check_length(self, max_length: int) -> bool: ...
    def expand(self, indent_size: int) -> Iterable['_Line']: ...
    def __init__(self, parent, is_root, node, text, suffix, whitespace, expanded, last) -> None: ...

def traverse(_object: Any, max_length: Optional[int] = ..., max_string: Optional[int] = ..., max_depth: Optional[int] = ...) -> Node: ...
def pretty_repr(_object: Any, *, max_width: int = ..., indent_size: int = ..., max_length: Optional[int] = ..., max_string: Optional[int] = ..., max_depth: Optional[int] = ..., expand_all: bool = ...) -> str: ...
def pprint(_object: Any, *, console: Optional[Console] = ..., indent_guides: bool = ..., max_length: Optional[int] = ..., max_string: Optional[int] = ..., max_depth: Optional[int] = ..., expand_all: bool = ...) -> None: ...
