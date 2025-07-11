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
from dataclasses import dataclass as dataclass, fields as fields, is_dataclass as is_dataclass
from inspect import isclass as isclass
from itertools import islice as islice
from rich.repr import RichReprResult as RichReprResult
from types import MappingProxyType as MappingProxyType
from typing import Any, Optional

def install(console: Optional['Console'] = ..., overflow: OverflowMethod = ..., crop: bool = ..., indent_guides: bool = ..., max_length: Optional[int] = ..., max_string: Optional[int] = ..., max_depth: Optional[int] = ..., expand_all: bool = ...) -> None: ...
def pprint(_object: Any, *, console: Optional['Console'] = ..., indent_guides: bool = ..., max_length: Optional[int] = ..., max_string: Optional[int] = ..., max_depth: Optional[int] = ..., expand_all: bool = ...) -> None: ...
def pretty_repr(_object: Any, *, max_width: int = ..., indent_size: int = ..., max_length: Optional[int] = ..., max_string: Optional[int] = ..., max_depth: Optional[int] = ..., expand_all: bool = ...) -> str: ...

class Pretty: ...
