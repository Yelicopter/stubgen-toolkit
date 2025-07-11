from .console import Console as Console, ConsoleRenderable as ConsoleRenderable
from datetime import datetime
from typing import Callable, Iterable, Optional

FormatTimeCallable = Callable[[datetime], str]

class LogRender:
    def __init__(self, show_time: bool = ..., show_path: bool = ..., time_format: str = ...) -> None: ...
    def __call__(self, console: Console, renderables: Iterable[ConsoleRenderable], log_time: Optional[datetime] = ..., path: Optional[str] = ..., line_no: Optional[int] = ..., link_path: Optional[str] = ...) -> ConsoleRenderable: ...
