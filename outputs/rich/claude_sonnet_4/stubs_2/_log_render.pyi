from typing import Callable, Iterable, Optional
from datetime import datetime
from .console import Console, ConsoleRenderable

FormatTimeCallable = Callable[[datetime], str]

class LogRender:
    def __init__(
        self,
        show_time: bool = True,
        show_path: bool = True,
        time_format: str = "[%X]"
    ) -> None: ...
    
    def __call__(
        self,
        console: Console,
        renderables: Iterable[ConsoleRenderable],
        log_time: Optional[datetime] = None,
        path: Optional[str] = None,
        line_no: Optional[int] = None,
        link_path: Optional[str] = None
    ) -> ConsoleRenderable: ...