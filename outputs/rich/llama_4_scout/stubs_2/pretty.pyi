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
)

from rich.repr import RichReprResult

try:
    import attr as _attr_module

    _has_attrs = hasattr(_attr_module, "ib")
except ImportError:  # pragma: no cover
    _has_attrs = False

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


def _is_attr_object(obj: Any) -> bool:
    """Check if an object was created with attrs module."""
    ...

def _get_attr_fields(obj: Any) -> Iterable:
    """Get fields for an attrs object."""
    ...

def _is_dataclass_repr(obj: Any) -> bool:
    """Check if an instance of a dataclass contains the default repr.

    Args:
        obj (object): A dataclass instance.

    Returns:
        bool: True if the default repr is used, False if there is a custom repr.
    """
    ...

def _dummy_namedtuple() : collections.namedtuple("_dummy_namedtuple", [])


def _has_default_namedtuple_repr(obj: Any) -> bool:
    """Check if an instance of namedtuple contains the default repr

    Args:
        obj (object): A namedtuple

    Returns:
        bool: True if the default repr is used, False if there's a custom repr.
    """
    ...

def _safe_isinstance(
        obj: Any, 
        class_or_tuple: Union[type, Tuple[type, ...]]
) -> bool:
    """isinstance can fail in rare cases, for example types with no __class__"""
    ...

def install(
        console: Optional["Console"] = None,
        overflow: OverflowMethod = "ignore",
        crop: bool = False,
        indent_guides: bool = False,
        max_length: Optional[int] = None,
        max_string: Optional[int] = None,
        max_depth: Optional[int] = None,
        expand_all: bool = False,
) -> None:
    """Install automatic pretty printing in the Python REPL.

    Args:
        console (Console, optional): Console instance or ``None`` to use global console. Defaults to None.
        overflow (Optional[OverflowMethod], optional): Overflow method. Defaults to "ignore".
        crop (Optional[bool], optional): Enable cropping of long lines. Defaults to False.
        indent_guides (bool, optional): Enable indentation guides. Defaults to False.
        max_length (int, optional): Maximum length of containers before abbreviating, or None for no abbreviation.
            Defaults to None.
        max_string (int, optional): Maximum length of string before truncating, or None to disable. Defaults to None.
        max_depth (int, optional): Maximum depth of nested data structures, or None for no maximum. Defaults to None.
        expand_all (bool, optional): Expand all containers. Defaults to False.
        max_frames (int): Maximum number of frames to show in a traceback, 0 for no maximum. Defaults to 100.
    """
    ...

def pprint(
        _object: Any,
        *,
        console: Optional["Console"] = None,
        indent_guides: bool = True,
        max_length: Optional[int] = None,
        max_string: Optional[int] = None,
        max_depth: Optional[int] = None,
        expand_all: bool = False,
) -> None:
    ...

def pretty_repr(
        _object: Any,
        *,
        max_width: int = 80,
        indent_size: int = 4,
        max_length: Optional[int] = None,
        max_string: Optional[int] = None,
        max_depth: Optional[int] = None,
        expand_all: bool = False,
) -> str:
    ...

class Pretty:
    ...