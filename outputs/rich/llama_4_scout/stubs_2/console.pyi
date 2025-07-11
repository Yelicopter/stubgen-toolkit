import inspect
import os
import sys
import threading
import zlib
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from functools import wraps
from getpass import getpass
from html import escape
from inspect import isclass
from itertools import islice
from math import ceil
from time import monotonic
from types import FrameType, ModuleType, TracebackType
from typing import (
 IO,
 TYPE_CHECKING,
 Any,
 Callable,
 Dict,
 Iterable,
 List,
 Mapping,
 NamedTuple,
 Optional,
 TextIO,
 Tuple,
 Type,
 Union,
 cast,
)

from rich._null_file import NULL_FILE

if sys.version_info >= (3,8):
 from typing import Literal, Protocol, runtime_checkable
else:
 from typing_extensions import (
  Literal,
  Protocol,
  runtime_checkable,
 ) # pragma: no cover

from . import errors, themes
from ._emoji_replace import _emoji_replace
from ._export_format import CONSOLE_HTML_FORMAT, CONSOLE_SVG_FORMAT
from ._fileno import get_fileno
from ._log_render import FormatTimeCallable, LogRender
from .align import Align, AlignMethod
from .color import ColorSystem, blend_rgb
from .control import Control
from .emoji import EmojiVariant
from .highlighter import NullHighlighter, ReprHighlighter
from .markup import render as render_markup
from .measure import Measurement, measure_renderables
from .pager import Pager, SystemPager
from .pretty import Pretty, is_expandable
from .protocol import rich_cast
from .region import Region
from .scope import render_scope
from .screen import Screen
from .segment import Segment
from .style import Style, StyleType
from .styled import Styled
from .terminal_theme import DEFAULT_TERMINAL_THEME, SVG_EXPORT_THEME, TerminalTheme
from .text import Text, TextType
from .theme import Theme, ThemeStack

if TYPE_CHECKING:
 from ._windows import WindowsConsoleFeatures
 from .live import Live
 from .status import Status

JUPYTER_DEFAULT_COLUMNS =115
JUPYTER_DEFAULT_LINES =100
WINDOWS = sys.platform == "win32"

HighlighterType = Callable[[Union[str, "Text"]], "Text"]
JustifyMethod = Literal["default", "left", "center", "right", "full"]
OverflowMethod = Literal["fold", "crop", "ellipsis", "ignore"]


class NoChange:
 pass


NO_CHANGE = NoChange()

try:
 _STDIN_FILENO = sys.__stdin__.fileno() # type: ignore[union-attr]
except Exception:
 _STDIN_FILENO =0
try:
 _STDOUT_FILENO = sys.__stdout__.fileno() # type: ignore[union-attr]
except Exception:
 _STDOUT_FILENO =1
try:
 _STDERR_FILENO = sys.__stderr__.fileno() # type: ignore[union-attr]
except Exception:
 _STDERR_FILENO =2

_STD_STREAMS = (_STDIN_FILENO, _STDOUT_FILENO, _STDERR_FILENO)
_STD_STREAMS_OUTPUT = (_STDOUT_FILENO, _STDERR_FILENO)


_TERM_COLORS = {
 "kitty": ColorSystem.EIGHT_BIT,
 "256color": ColorSystem.EIGHT_BIT,
 "16color": ColorSystem.STANDARD,
}


class ConsoleDimensions(NamedTuple):
 """Size of the terminal."""

 ... #width: int
 """The width of the console in 'cells'."""
 ... #height: int
 """The height of the console in lines."""


@dataclass
class ConsoleOptions:
 """Options for __rich_console__ method."""

 ... #size: ConsoleDimensions
 """Size of console."""
 ... #legacy_windows: bool
 """legacy_windows: flag for legacy windows."""
 ... #min_width: int
 """Minimum width of renderable."""
 ... #max_width: int
 """Maximum width of renderable."""
 ... #is_terminal: bool
 """True if the target is a terminal, otherwise False."""
 ... #encoding: str
 """Encoding of terminal."""
 ... #max_height: int
 """Height of container (starts as terminal)"""
 justify: Optional[str] = None
 """Justify value override for renderable."""
 overflow: Optional[str] = None
 """Overflow value override for renderable."""
 no_wrap: bool = False
 """Disable wrapping for text."""
 highlight: Optional[bool] = None
 """Highlight override for render_str."""
 markup: Optional[bool] = None
 """Enable markup when rendering strings."""
 height: Optional[int] = None

 @property
 def ascii_only(self) -> bool:
  """Check if renderables should use ascii only."""
 ...

 def copy(self) -> "ConsoleOptions":
  """Return a copy of the options.

  Returns:
  ConsoleOptions: a copy of self.
  """
 ...

 def update(
         self,
         *,
         width: Union[NoChange, int] = NO_CHANGE,
         min_width: Union[NoChange, int] = NO_CHANGE,
         max_width: Union[NoChange, int] = NO_CHANGE,
         justify: Union[NoChange, str] = NO_CHANGE,
         overflow: Union[NoChange, str] = NO_CHANGE,
         no_wrap: Union[NoChange, bool] = NO_CHANGE,
         highlight: Union[NoChange, bool] = NO_CHANGE,
         markup: Union[NoChange, bool] = NO_CHANGE,
         height: Union[NoChange, int] = NO_CHANGE,
 ) -> "ConsoleOptions":
  """Update values, return a copy."""
 ...

 def update_width(self, width: int) -> "ConsoleOptions":
  """Update just the width, return a copy.

  Args:
  width (int): New width (sets both min_width and max_width)

  Returns:
  ~ConsoleOptions: New console options instance.
  """
 ...

 def update_height(self, height: int) -> "ConsoleOptions":
  """Update the height, and return a copy.

  Args:
  height (int): New height

  Returns:
  ~ConsoleOptions: New Console options instance.
  """
 ...

 def reset_height(self) -> "ConsoleOptions":
  """Return a copy of the options with height set to ``None``.

  Returns:
  ~ConsoleOptions: New console options instance.
  """
 ...

 def update_dimensions(self, width: int, height: int) -> "ConsoleOptions":
  """Update the width and height, and return a copy.

  Args:
  width (int): New width (sets both min_width and max_width).
  height (int): New height.

  Returns:
  ~ConsoleOptions: New console options instance.
  """
 ...


@runtime_checkable
class RichCast(Protocol):
 """An object that may be 'cast' to a console renderable."""

 def __rich__(
         self,
 ) -> str: # pragma: no cover
  ...


@runtime_checkable
class ConsoleRenderable(Protocol):
 """An object that supports the console protocol."""

 def __rich_console__(
         self, console , options
 ) -> str: # pragma: no cover
  ...


# A type that may be rendered by Console.
RenderableType = Union[ConsoleRenderable, RichCast, str]
"""A string or any object that may be rendered by Rich."""

# The result of calling a __rich_console__ method.
RenderResult = Iterable[Union[RenderableType, Segment]]

_null_highlighter = NullHighlighter()


class CaptureError(Exception):
 """An error in the Capture context manager."""


class NewLine:
 """A renderable to generate new line(s)"""

 def __init__(self, count: int = 1) -> None:
  self.count = count

 def __rich_console__(
         self, console , options
 ) -> str:
  ...


class ScreenUpdate:
 """Render a list of lines at a given offset."""

 def __init__(self, lines: List[List[Segment]], x: int, y: int) -> None:
  self._lines = lines
  self.x = x
  self.y = y

 def __rich_console__(
         self, console , options
 ) -> str:
  ...


class Capture:
 """Context manager to capture the result of printing to the console.
 See :meth:`~rich.console.Console.capture` for how to use.

 Args:
 console (Console): A console instance to capture output.
 """

 def __init__(self, console: "Console") -> None:
  self._console = console
  self._result = None

 def __enter__(self) -> str:
  self._console.begin_capture()
  return self

 def __exit__(
         self,
         exc_type ,
         exc_val ,
         exc_tb ,
 ) -> None:
  self._result = self._console.end_capture()

 def get(self) -> str:
  """Get the result of the capture."""
 ...


class ThemeContext:
 """A context manager to use a temporary theme. See :meth:`~rich.console.Console.use_theme` for usage."""

 def __init__(self, console: "Console", theme: Theme, inherit: bool = True) -> None:
  self.console = console
  self.theme = theme
  self.inherit = inherit

 def __enter__(self) -> str:
  self.console.push_theme(self.theme)
  return self

 def __exit__(
         self,
         exc_type ,
         exc_val ,
         exc_tb ,
 ) -> None:
  self.console.pop_theme()


class PagerContext:
 """A context manager that 'pages' content. See :meth:`~rich.console.Console.pager` for usage."""

 def __init__(
         self,
         console: "Console",
         pager: Optional["Pager"] = None,
         styles: bool = False,
         links: bool = False,
 ) -> None:
  self._console = console
  self.pager = SystemPager() if pager is None else pager
  self.styles = styles
  self.links = links

 def __enter__(self) -> str:
  self._console._enter_buffer()
  return self

 def __exit__(
         self,
         exc_type ,
         exc_val ,
         exc_tb ,
 ) -> None:
  ...


class ScreenContext:
 """A context manager that enables an alternative screen. See :meth:`~rich.console.Console.screen` for usage."""

 def __init__(
         self, console: "Console", hide_cursor: bool, style: str = ""
 ) -> None:
  self.console = console
  self.hide_cursor = hide_cursor
  self.screen = Screen(style=style)
  self._changed = False

 def update(
         self, *renderables: RenderableType, style: Optional[Style] = None
 ) -> None:
  """Update the screen.

  Args:
  renderable (RenderableType, optional): Optional renderable to replace current renderable,
  or None for no change. Defaults to None.
  style: (Style, optional): Replacement style, or None for no change. Defaults to None.
  """
 ...

 def __enter__(self) -> str:
  ...

 def __exit__(
         self,
         exc_type ,
         exc_val ,
         exc_tb ,
 ) -> None:
  ...


class Group:
 """Takes a group of renderables and returns a renderable object that renders the group.

 Args:
 renderables (Iterable[RenderableType]): An iterable of renderable objects.
 fit (bool, optional): Fit dimension of group to contents, or fill available space. Defaults to True.
 """

 def __init__(self, *renderables: RenderableType, fit: bool = True) -> None:
  self._renderables = renderables
  self.fit = fit
  self._render = None

 @property
 def renderables(self) -> List[RenderableType]:
  ...

 def __rich_measure__(
         self, console , options
 ) -> Measurement:
  ...

 def __rich_console__(
         self, console , options
 ) -> str:
  ...


def group(fit: bool = True) -> Callable:
 """A decorator that turns an iterable of renderables in to a group.

 Args:
 fit (bool, optional): Fit dimension of group to contents, or fill available space. Defaults to True.
 """

 def decorator(
         method: Callable[..., Iterable[RenderableType]],
 ) -> Callable[..., Group]:
  """Convert a method that returns an iterable of renderables in to a Group."""

 def _replace(*args: Any, **kwargs: Any) -> Group: ...

 return _replace

 return decorator


def _is_jupyter() -> bool: # pragma: no cover
 """Check if we're running in a Jupyter notebook."""
 ...


COLOR_SYSTEMS = {
 "standard": ColorSystem.STANDARD,
 "256": ColorSystem.EIGHT_BIT,
 "truecolor": ColorSystem.TRUECOLOR,
 "windows": ColorSystem.WINDOWS,
}

_COLOR_SYSTEMS_NAMES = {system: name for name, system in COLOR_SYSTEMS.items()}


@dataclass
class ConsoleThreadLocals(threading.local): ...


class RenderHook(ABC):
 """Provides hooks in to the render process."""

 @abstractmethod
 def process_renderables(
     self, console: "Console", renderables: Iterable[RenderableType]
 ) -> Iterable[RenderableType]:
     """Process renderables before they are rendered.

     Args:
         console (Console): The console instance.
         renderables (Iterable[RenderableType]): The renderables to process.

     Returns:
         Iterable[RenderableType]: Processed renderables.
     """
     ...
 """

 text: str
 style: Optional[Style] = None
 control: Optional[Tuple[ControlType]] = None
"""
 @property
 def cell_length(self) -> int:
     ...


 def __bool__(self) -> bool:
     ...

 @classmethod
 def _split_cells(
     cls, segment: "Segment", cut: int
 ) -> Tuple["Segment", "Segment"]:
     ...

 def split_cells(self, cut: int) -> Tuple["Segment", "Segment"]:
     ...

 @classmethod
 def line(cls) -> "Segment":
     ...

 @classmethod
 def apply_style(
     cls,
     segments: Iterable["Segment"],
     style: Optional[Style] = None,
     post_style: Optional[Style] = None,
 ) -> Iterable["Segment"]:
     ...

 @classmethod
 def filter_control(
     cls,
     segments: Iterable["Segment"],
     is_control: bool = False,
 ) -> Iterable["Segment"]:
     ...

 @classmethod
 def split_lines(
     cls, segments: Iterable["Segment"]
 ) -> Iterable[List["Segment"]]:
     ...

 @classmethod
 def split_and_crop_lines(
     cls,
     segments: Iterable["Segment"],
     length: int,
     style: Optional[Style] = None,
     pad: bool = True,
     include_new_lines: bool = True,
 ) -> Iterable[List["Segment"]]:
     ...

 @classmethod
 def adjust_line_length(
     cls,
     line: List["Segment"],
     length: int,
     style: Optional[Style] = None,
     pad: bool = True,
 ) -> List["Segment"]:
     ...

 @classmethod
 def get_line_length(cls, line: List["Segment"]) -> int:
     ...

 @classmethod
 def get_shape(cls, lines: List[List["Segment"]]) -> Tuple[int, int]:
     ...

 @classmethod
 def set_shape(
     cls,
     lines: List[List["Segment"]],
     width: int,
     height: Optional[int] = None,
     style: Optional[Style] = None,
     new_lines: bool = False,
 ) -> List[List["Segment"]]:
     ...

 @classmethod
 def align_top(
     cls,
     lines: List[List["Segment"]],
     width: int,
     height: Optional[int],
     style: Style,
     new_lines: bool = False,
 ) -> List[List["Segment"]]:
     ...

 @classmethod
 def align_bottom(
     cls,
     lines: List[List["Segment"]],
     width: int,
     height: Optional[int],
     style: Style,
     new_lines: bool = False,
 ) -> List[List["Segment"]]:
     ...

 @classmethod
 def align_middle(
     cls,
     lines: List[List["Segment"]],
     width: int,
     height: Optional[int],
     style: Style,
     new_lines: bool = False,
 ) -> List[List["Segment"]]:
     ...

 @classmethod
 def simplify(
     cls, segments: Iterable["Segment"]
 ) -> Iterable["Segment"]:
     ...

 @classmethod
 def strip_links(
     cls, segments: Iterable["Segment"]
 ) -> Iterable["Segment"]:
     ...

 @classmethod
 def strip_styles(
     cls, segments: Iterable["Segment"]
 ) -> Iterable["Segment"]:
     ...

 @classmethod
 def remove_color(
     cls, segments: Iterable["Segment"]
 ) -> Iterable["Segment"]:
     ...

 @classmethod
 def divide(
     cls,
     segments: Iterable["Segment"],
     cuts: Iterable[int],
 ) -> Iterable[Iterable[List["Segment"]]]:
     ...

class Segments:
 """A simple renderable to render an iterable of segments. This class may be useful if
 you want to print segments outside of a __rich_console__ method.

 Args:
 segments (Iterable[Segment]): An iterable of segments.
 new_lines (bool, optional): Add new lines between segments. Defaults to False.
"""

def __init__(self, segments: Iterable["Segment"], new_lines: bool = False) -> None:
    ...

def __rich_console__(
    self, console: "Console", options: "ConsoleOptions"
) -> "RenderResult":
    ...

class SegmentLines:
 def __init__(self, lines: Iterable[List["Segment"]], new_lines: bool = False) -> None:
    ...

def __rich_console__(
    self, console: "Console", options: "ConsoleOptions"
) -> "RenderResult":
    ...