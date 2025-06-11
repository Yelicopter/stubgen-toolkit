import builtins
import collections
import dataclasses
import inspect
import os
import reprlib
import sys
from array import array
from collections import Counter, UserDict, UserList, defaultdict, deque
from dataclasses import dataclass, fields, is_dataclass
from inspect import isclass
from itertools import islice
from types import MappingProxyType
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    DefaultDict,
    Deque,
    Dict,
    Iterable,
    List,
    Optional,
    Sequence,
    Set,
    Tuple,
    Union,
    TypeVar,
)

from rich.repr import RichReprResult

from . import get_console
from ._loop import loop_last
from ._pick import pick_bool
from .abc import RichRenderable
from .cells import cell_len
from .highlighter import ReprHighlighter
from .jupyter import JupyterMixin, JupyterRenderable
from .measure import Measurement
from .text import Text

if TYPE_CHECKING:
    from .console import (
        Console,
        ConsoleOptions,
        HighlighterType,
        JustifyMethod,
        OverflowMethod,
        RenderResult,
    )

class _attr_module:
    class Attribute(Generic[T]):
        pass

def _is_attr_object(obj: Any) -> bool: ...

def _get_attr_fields(obj: Any) -> Sequence["_attr_module.Attribute[Any]"]: ...

def _is_dataclass_repr(obj: object) -> bool: ...

_dummy_namedtuple = collections.namedtuple("_dummy_namedtuple", [])

def _has_default_namedtuple_repr(obj: object) -> bool: ...

def _ipy_display_hook(
    value: Any,
    console: Optional["Console"] = None,
    overflow: "OverflowMethod" = "ignore",
    crop: bool = False,
    indent_guides: bool = False,
    max_length: Optional[int] = None,
    max_string: Optional[int] = None,
    max_depth: Optional[int] = None,
    expand_all: bool = False,
) -> Union[str, None]: ...

def _safe_isinstance(
    obj: object, class_or_tuple: Union[type, Tuple[type, ...]]
) -> bool: ...

def install(
    console: Optional["Console"] = None,
    overflow: "OverflowMethod" = "ignore",
    crop: bool = False,
    indent_guides: bool = False,
    max_length: Optional[int] = None,
    max_string: Optional[int] = None,
    max_depth: Optional[int] = None,
    expand_all: bool = False,
) -> None: ...

T = TypeVar('T')

class Pretty(JupyterMixin):
    def __init__(
        self,
        _object: Any,
        highlighter: Optional["HighlighterType"] = None,
        *,
        indent_size: int = 4,
        justify: Optional["JustifyMethod"] = None,
        overflow: Optional["OverflowMethod"] = None,
        no_wrap: Optional[bool] = False,
        indent_guides: bool = False,
        max_length: Optional[int] = None,
        max_string: Optional[int] = None,
        max_depth: Optional[int] = None,
        expand_all: bool = False,
        margin: int = 0,
        insert_line: bool = False,
    ) -> None: ...

    def __rich_console__(
        self, console: "Console", options: "ConsoleOptions"
    ) -> "RenderResult": ...

    def __rich_measure__(
        self, console: "Console", options: "ConsoleOptions"
    ) -> "Measurement": ...

def _get_braces_for_defaultdict(_object: DefaultDict[Any, Any]) -> Tuple[str, str, str]: ...

def _get_braces_for_deque(_object: Deque[Any]) -> Tuple[str, str, str]: ...

def _get_braces_for_array(_object: "array[Any]") -> Tuple[str, str, str]: ...

_BRACES: Dict[type, Callable[[Any], Tuple[str, str, str]]]
_CONTAINERS: Tuple[type, ...]
_MAPPING_CONTAINERS: Tuple[type, ...]

def is_expandable(obj: Any) -> bool: ...

@dataclass
class Node:
    key_repr: str
    value_repr: str
    open_brace: str
    close_brace: str
    empty: str
    last: bool
    is_tuple: bool
    is_namedtuple: bool
    children: Optional[List["Node"]]
    key_separator: str
    separator: str

    def iter_tokens(self) -> Iterable[str]: ...

    def check_length(self, start_length: int, max_length: int) -> bool: ...

    def __str__(self) -> str: ...

    def render(
        self, max_width: int = 80, indent_size: int = 4, expand_all: bool = False
    ) -> str: ...

@dataclass
class _Line:
    parent: Optional["_Line"]
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

    def expand(self, indent_size: int) -> Iterable["_Line"]: ...

    def __str__(self) -> str: ...

def _is_namedtuple(obj: Any) -> bool: ...

def traverse(
    _object: Any,
    max_length: Optional[int] = None,
    max_string: Optional[int] = None,
    max_depth: Optional[int] = None,
) -> Node: ...

def pretty_repr(
    _object: Any,
    *,
    max_width: int = 80,
    indent_size: int = 4,
    max_length: Optional[int] = None,
    max_string: Optional[int] = None,
    max_depth: Optional[int] = None,
    expand_all: bool = False,
) -> str: ...

def pprint(
    _object: Any,
    *,
    console: Optional["Console"] = None,
    indent_guides: bool = True,
    max_length: Optional[int] = None,
    max_string: Optional[int] = None,
    max_depth: Optional[int] = None,
    expand_all: bool = False,
) -> None: ...