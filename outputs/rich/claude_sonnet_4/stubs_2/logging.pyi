import logging
from datetime import datetime
from typing import ClassVar, Iterable, List, Optional, Type, Union

from . import get_console
from ._log_render import FormatTimeCallable
from .console import Console, ConsoleRenderable
from .highlighter import Highlighter, ReprHighlighter
from .text import Text, TextType
from .traceback import Traceback

class RichHandler(logging.Handler):
    def __init__(
        self,
        level: Union[int, str] = logging.NOTSET,
        console: Optional[Console] = None,
        *,
        show_time: bool = True,
        omit_repeated_times: bool = True,
        show_level: bool = True,
        show_path: bool = True,
        enable_link_path: bool = True,
        highlighter: Optional[Highlighter] = None,
        markup: bool = False,
        rich_tracebacks: bool = False,
        tracebacks_width: Optional[int] = None,
        tracebacks_extra_lines: int = 3,
        tracebacks_theme: Optional[str] = None,
        tracebacks_word_wrap: bool = True,
        tracebacks_show_locals: bool = False,
        tracebacks_suppress: Iterable[Union[str, object]] = (),
        locals_max_length: int = 10,
        locals_max_string: int = 80,
        log_time_format: Union[str, FormatTimeCallable] = "[%x %X]",
        keywords: Optional[List[str]] = None
    ) -> None: ...
    
    def get_level_text(self, record: logging.LogRecord) -> Text: ...
    def emit(self, record: logging.LogRecord) -> None: ...
    def render_message(self, record: logging.LogRecord, message: str) -> ConsoleRenderable: ...
    def render(
        self,
        *,
        record: logging.LogRecord,
        traceback: Optional[Traceback],
        message_renderable: ConsoleRenderable
    ) -> ConsoleRenderable: ...