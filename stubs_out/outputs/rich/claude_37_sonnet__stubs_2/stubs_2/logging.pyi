from . import get_console as get_console
from ._log_render import FormatTimeCallable as FormatTimeCallable, LogRender as LogRender
from .console import Console as Console, ConsoleRenderable as ConsoleRenderable
from .highlighter import Highlighter as Highlighter, ReprHighlighter as ReprHighlighter
from .text import Text as Text
from .traceback import Traceback as Traceback
from datetime import datetime as datetime
from logging import Handler, LogRecord
from pathlib import Path as Path
from rich._null_file import NullFile as NullFile
from types import ModuleType
from typing import ClassVar, Iterable, List, Optional, Type, Union

class RichHandler(Handler):
    KEYWORDS: ClassVar[Optional[List[str]]]
    HIGHLIGHTER_CLASS: ClassVar[Type[Highlighter]]
    def __init__(self, level: Union[int, str] = ..., console: Optional[Console] = ..., *, show_time: bool = ..., omit_repeated_times: bool = ..., show_level: bool = ..., show_path: bool = ..., enable_link_path: bool = ..., highlighter: Optional[Highlighter] = ..., markup: bool = ..., rich_tracebacks: bool = ..., tracebacks_width: Optional[int] = ..., tracebacks_code_width: int = ..., tracebacks_extra_lines: int = ..., tracebacks_theme: Optional[str] = ..., tracebacks_word_wrap: bool = ..., tracebacks_show_locals: bool = ..., tracebacks_suppress: Iterable[Union[str, ModuleType]] = ..., tracebacks_max_frames: int = ..., locals_max_length: int = ..., locals_max_string: int = ..., log_time_format: Union[str, FormatTimeCallable] = ..., keywords: Optional[List[str]] = ...) -> None: ...
    def get_level_text(self, record: LogRecord) -> Text: ...
    def emit(self, record: LogRecord) -> None: ...
    def render_message(self, record: LogRecord, message: str) -> ConsoleRenderable: ...
    def render(self, *, record: LogRecord, traceback: Optional[Traceback], message_renderable: ConsoleRenderable) -> ConsoleRenderable: ...
