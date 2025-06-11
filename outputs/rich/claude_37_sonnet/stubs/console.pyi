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

if sys.version_info >= (3, 8):
    from typing import Literal, Protocol, runtime_checkable
else:
    from typing_extensions import (
        Literal,
        Protocol,
        runtime_checkable,
    )  # pragma: no cover

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

HighlighterType = Callable[[Union[str, "Text"]], "Text"]
JustifyMethod = Literal["default", "left", "center", "right", "full"]
OverflowMethod = Literal["fold", "crop", "ellipsis", "ignore"]

class NoChange: ...

NO_CHANGE: NoChange

class ConsoleDimensions(NamedTuple):
    width: int
    height: int

@dataclass
class ConsoleOptions:
    size: ConsoleDimensions
    legacy_windows: bool
    min_width: int
    max_width: int
    is_terminal: bool
    encoding: str
    max_height: int
    justify: Optional[JustifyMethod]
    overflow: Optional[OverflowMethod]
    no_wrap: Optional[bool]
    highlight: Optional[bool]
    markup: Optional[bool]
    height: Optional[int]

    @property
    def ascii_only(self) -> bool: ...

    def copy(self) -> "ConsoleOptions": ...

    def update(
        self,
        *,
        width: Union[int, NoChange] = NO_CHANGE,
        min_width: Union[int, NoChange] = NO_CHANGE,
        max_width: Union[int, NoChange] = NO_CHANGE,
        justify: Union[Optional[JustifyMethod], NoChange] = NO_CHANGE,
        overflow: Union[Optional[OverflowMethod], NoChange] = NO_CHANGE,
        no_wrap: Union[Optional[bool], NoChange] = NO_CHANGE,
        highlight: Union[Optional[bool], NoChange] = NO_CHANGE,
        markup: Union[Optional[bool], NoChange] = NO_CHANGE,
        height: Union[Optional[int], NoChange] = NO_CHANGE,
    ) -> "ConsoleOptions": ...

    def update_width(self, width: int) -> "ConsoleOptions": ...

    def update_height(self, height: int) -> "ConsoleOptions": ...

    def reset_height(self) -> "ConsoleOptions": ...

    def update_dimensions(self, width: int, height: int) -> "ConsoleOptions": ...

@runtime_checkable
class RichCast(Protocol):
    def __rich__(
        self,
    ) -> Union["ConsoleRenderable", "RichCast", str]: ...

@runtime_checkable
class ConsoleRenderable(Protocol):
    def __rich_console__(
        self, console: "Console", options: "ConsoleOptions"
    ) -> "RenderResult": ...

RenderableType = Union[ConsoleRenderable, RichCast, str]
RenderResult = Iterable[Union[RenderableType, Segment]]

class CaptureError(Exception): ...

class NewLine:
    count: int
    def __init__(self, count: int = 1) -> None: ...
    def __rich_console__(
        self, console: "Console", options: "ConsoleOptions"
    ) -> Iterable[Segment]: ...

class ScreenUpdate:
    def __init__(self, lines: List[List[Segment]], x: int, y: int) -> None: ...
    def __rich_console__(
        self, console: "Console", options: ConsoleOptions
    ) -> RenderResult: ...

class Capture:
    def __init__(self, console: "Console") -> None: ...
    def __enter__(self) -> "Capture": ...
    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None: ...
    def get(self) -> str: ...

class ThemeContext:
    def __init__(self, console: "Console", theme: Theme, inherit: bool = True) -> None: ...
    def __enter__(self) -> "ThemeContext": ...
    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None: ...

class PagerContext:
    def __init__(
        self,
        console: "Console",
        pager: Optional[Pager] = None,
        styles: bool = False,
        links: bool = False,
    ) -> None: ...
    def __enter__(self) -> "PagerContext": ...
    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None: ...

class ScreenContext:
    def __init__(
        self, console: "Console", hide_cursor: bool, style: StyleType = ""
    ) -> None: ...
    def update(
        self, *renderables: RenderableType, style: Optional[StyleType] = None
    ) -> None: ...
    def __enter__(self) -> "ScreenContext": ...
    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_val: Optional[BaseException],
        exc_tb: Optional[TracebackType],
    ) -> None: ...

class Group:
    def __init__(self, *renderables: "RenderableType", fit: bool = True) -> None: ...
    @property
    def renderables(self) -> List["RenderableType"]: ...
    def __rich_measure__(
        self, console: "Console", options: "ConsoleOptions"
    ) -> "Measurement": ...
    def __rich_console__(
        self, console: "Console", options: "ConsoleOptions"
    ) -> RenderResult: ...

def group(fit: bool = True) -> Callable[..., Callable[..., Group]]: ...

def _is_jupyter() -> bool: ...

COLOR_SYSTEMS: Dict[str, ColorSystem]
_COLOR_SYSTEMS_NAMES: Dict[ColorSystem, str]

@dataclass
class ConsoleThreadLocals(threading.local):
    theme_stack: ThemeStack
    buffer: List[Segment]
    buffer_index: int

class RenderHook(ABC):
    @abstractmethod
    def process_renderables(
        self, renderables: List[ConsoleRenderable]
    ) -> List[ConsoleRenderable]: ...

def get_windows_console_features() -> "WindowsConsoleFeatures": ...

class Console:
    _environ: Mapping[str, str]

    def __init__(
        self,
        *,
        color_system: Optional[
            Literal["auto", "standard", "256", "truecolor", "windows"]
        ] = "auto",
        force_terminal: Optional[bool] = None,
        force_jupyter: Optional[bool] = None,
        force_interactive: Optional[bool] = None,
        soft_wrap: bool = False,
        theme: Optional[Theme] = None,
        stderr: bool = False,
        file: Optional[IO[str]] = None,
        quiet: bool = False,
        width: Optional[int] = None,
        height: Optional[int] = None,
        style: Optional[StyleType] = None,
        no_color: Optional[bool] = None,
        tab_size: int = 8,
        record: bool = False,
        markup: bool = True,
        emoji: bool = True,
        emoji_variant: Optional[EmojiVariant] = None,
        highlight: bool = True,
        log_time: bool = True,
        log_path: bool = True,
        log_time_format: Union[str, FormatTimeCallable] = "[%X]",
        highlighter: Optional["HighlighterType"] = ReprHighlighter(),
        legacy_windows: Optional[bool] = None,
        safe_box: bool = True,
        get_datetime: Optional[Callable[[], datetime]] = None,
        get_time: Optional[Callable[[], float]] = None,
        _environ: Optional[Mapping[str, str]] = None,
    ) -> None: ...

    def __repr__(self) -> str: ...

    @property
    def file(self) -> IO[str]: ...

    @file.setter
    def file(self, new_file: IO[str]) -> None: ...

    @property
    def _buffer(self) -> List[Segment]: ...

    @property
    def _buffer_index(self) -> int: ...

    @_buffer_index.setter
    def _buffer_index(self, value: int) -> None: ...

    @property
    def _theme_stack(self) -> ThemeStack: ...

    def _detect_color_system(self) -> Optional[ColorSystem]: ...

    def _enter_buffer(self) -> None: ...

    def _exit_buffer(self) -> None: ...

    def set_live(self, live: "Live") -> None: ...

    def clear_live(self) -> None: ...

    def push_render_hook(self, hook: RenderHook) -> None: ...

    def pop_render_hook(self) -> None: ...

    def __enter__(self) -> "Console": ...

    def __exit__(
        self, exc_type: Any, exc_value: Any, traceback: Any
    ) -> None: ...

    def begin_capture(self) -> None: ...

    def end_capture(self) -> str: ...

    def push_theme(self, theme: Theme, *, inherit: bool = True) -> None: ...

    def pop_theme(self) -> None: ...

    def use_theme(self, theme: Theme, *, inherit: bool = True) -> ThemeContext: ...

    @property
    def color_system(self) -> Optional[str]: ...

    @property
    def encoding(self) -> str: ...

    @property
    def is_terminal(self) -> bool: ...

    @property
    def is_dumb_terminal(self) -> bool: ...

    @property
    def options(self) -> ConsoleOptions: ...

    @property
    def size(self) -> ConsoleDimensions: ...

    @size.setter
    def size(self, new_size: Tuple[int, int]) -> None: ...

    @property
    def width(self) -> int: ...

    @width.setter
    def width(self, width: int) -> None: ...

    @property
    def height(self) -> int: ...

    @height.setter
    def height(self, height: int) -> None: ...

    def bell(self) -> None: ...

    def capture(self) -> Capture: ...

    def pager(
        self, pager: Optional[Pager] = None, styles: bool = False, links: bool = False
    ) -> PagerContext: ...

    def line(self, count: int = 1) -> None: ...

    def clear(self, home: bool = True) -> None: ...

    def status(
        self,
        status: RenderableType,
        *,
        spinner: str = "dots",
        spinner_style: StyleType = "status.spinner",
        speed: float = 1.0,
        refresh_per_second: float = 12.5,
    ) -> "Status": ...

    def show_cursor(self, show: bool = True) -> bool: ...

    def set_alt_screen(self, enable: bool = True) -> bool: ...

    @property
    def is_alt_screen(self) -> bool: ...

    def set_window_title(self, title: str) -> bool: ...

    def screen(
        self, hide_cursor: bool = True, style: Optional[StyleType] = None
    ) -> "ScreenContext": ...

    def measure(
        self, renderable: RenderableType, *, options: Optional[ConsoleOptions] = None
    ) -> Measurement: ...

    def render(
        self, renderable: RenderableType, options: Optional[ConsoleOptions] = None
    ) -> Iterable[Segment]: ...

    def render_lines(
        self,
        renderable: RenderableType,
        options: Optional[ConsoleOptions] = None,
        *,
        style: Optional[Style] = None,
        pad: bool = True,
        new_lines: bool = False,
    ) -> List[List[Segment]]: ...

    def render_str(
        self,
        text: str,
        *,
        style: Union[str, Style] = "",
        justify: Optional[JustifyMethod] = None,
        overflow: Optional[OverflowMethod] = None,
        emoji: Optional[bool] = None,
        markup: Optional[bool] = None,
        highlight: Optional[bool] = None,
        highlighter: Optional[HighlighterType] = None,
    ) -> "Text": ...

    def get_style(
        self, name: Union[str, Style], *, default: Optional[Union[Style, str]] = None
    ) -> Style: ...

    def _collect_renderables(
        self,
        objects: Iterable[Any],
        sep: str,
        end: str,
        *,
        justify: Optional[JustifyMethod] = None,
        emoji: Optional[bool] = None,
        markup: Optional[bool] = None,
        highlight: Optional[bool] = None,
    ) -> List[ConsoleRenderable]: ...

    def rule(
        self,
        title: TextType = "",
        *,
        characters: str = "─",
        style: Union[str, Style] = "rule.line",
        align: AlignMethod = "center",
    ) -> None: ...

    def control(self, *control: Control) -> None: ...

    def out(
        self,
        *objects: Any,
        sep: str = " ",
        end: str = "\n",
        style: Optional[Union[str, Style]] = None,
        highlight: Optional[bool] = None,
    ) -> None: ...

    def print(
        self,
        *objects: Any,
        sep: str = " ",
        end: str = "\n",
        style: Optional[Union[str, Style]] = None,
        justify: Optional[JustifyMethod] = None,
        overflow: Optional[OverflowMethod] = None,
        no_wrap: Optional[bool] = None,
        emoji: Optional[bool] = None,
        markup: Optional[bool] = None,
        highlight: Optional[bool] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        crop: bool = True,
        soft_wrap: Optional[bool] = None,
        new_line_start: bool = False,
    ) -> None: ...

    def print_json(
        self,
        json: Optional[str] = None,
        *,
        data: Any = None,
        indent: Union[None, int, str] = 2,
        highlight: bool = True,
        skip_keys: bool = False,
        ensure_ascii: bool = False,
        check_circular: bool = True,
        allow_nan: bool = True,
        default: Optional[Callable[[Any], Any]] = None,
        sort_keys: bool = False,
    ) -> None: ...

    def update_screen(
        self,
        renderable: RenderableType,
        *,
        region: Optional[Region] = None,
        options: Optional[ConsoleOptions] = None,
    ) -> None: ...

    def update_screen_lines(
        self, lines: List[List[Segment]], x: int = 0, y: int = 0
    ) -> None: ...

    def print_exception(
        self,
        *,
        width: Optional[int] = 100,
        extra_lines: int = 3,
        theme: Optional[str] = None,
        word_wrap: bool = False,
        show_locals: bool = False,
        suppress: Iterable[Union[str, ModuleType]] = (),
        max_frames: int = 100,
    ) -> None: ...

    @staticmethod
    def _caller_frame_info(
        offset: int,
        currentframe: Callable[[], Optional[FrameType]] = inspect.currentframe,
    ) -> Tuple[str, int, Dict[str, Any]]: ...

    def log(
        self,
        *objects: Any,
        sep: str = " ",
        end: str = "\n",
        style: Optional[Union[str, Style]] = None,
        justify: Optional[JustifyMethod] = None,
        emoji: Optional[bool] = None,
        markup: Optional[bool] = None,
        highlight: Optional[bool] = None,
        log_locals: bool = False,
        _stack_offset: int = 1,
    ) -> None: ...

    def on_broken_pipe(self) -> None: ...

    def _check_buffer(self) -> None: ...

    def _write_buffer(self) -> None: ...

    def _render_buffer(self, buffer: Iterable[Segment]) -> str: ...

    def input(
        self,
        prompt: TextType = "",
        *,
        markup: bool = True,
        emoji: bool = True,
        password: bool = False,
        stream: Optional[TextIO] = None,
    ) -> str: ...

    def export_text(self, *, clear: bool = True, styles: bool = False) -> str: ...

    def save_text(self, path: str, *, clear: bool = True, styles: bool = False) -> None: ...

    def export_html(
        self,
        *,
        theme: Optional[TerminalTheme] = None,
        clear: bool = True,
        code_format: Optional[str] = None,
        inline_styles: bool = False,
    ) -> str: ...

    def save_html(
        self,
        path: str,
        *,
        theme: Optional[TerminalTheme] = None,
        clear: bool = True,
        code_format: str = CONSOLE_HTML_FORMAT,
        inline_styles: bool = False,
    ) -> None: ...

    def export_svg(
        self,
        *,
        title: str = "Rich",
        theme: Optional[TerminalTheme] = None,
        clear: bool = True,
        code_format: str = CONSOLE_SVG_FORMAT,
        font_aspect_ratio: float = 0.61,
        unique_id: Optional[str] = None,
    ) -> str: ...

    def save_svg(
        self,
        path: str,
        *,
        title: str = "Rich",
        theme: Optional[TerminalTheme] = None,
        clear: bool = True,
        code_format: str = CONSOLE_SVG_FORMAT,
        font_aspect_ratio: float = 0.61,
        unique_id: Optional[str] = None,
    ) -> None: ...

def _svg_hash(svg_main_code: str) -> str: ...