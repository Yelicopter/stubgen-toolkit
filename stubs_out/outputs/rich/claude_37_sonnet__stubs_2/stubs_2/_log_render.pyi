from .console import Console as Console, ConsoleRenderable as ConsoleRenderable, RenderableType as RenderableType
from .text import Text as Text, TextType as TextType
from datetime import datetime
from typing import Callable, Iterable, Optional, Union

FormatTimeCallable = Callable[[datetime], Text]

class LogRender:
    show_time: bool
    show_level: bool
    show_path: bool
    time_format: Union[str, FormatTimeCallable]
    omit_repeated_times: bool
    level_width: int
    def __init__(self, show_time: bool = ..., show_level: bool = ..., show_path: bool = ..., time_format: Union[str, FormatTimeCallable] = ..., omit_repeated_times: bool = ..., level_width: int = ...) -> None: ...
    def __call__(self, console: Console, renderables: Iterable['RenderableType'], log_time: Optional[datetime] = ..., time_format: Optional[Union[str, FormatTimeCallable]] = ..., level: str = ..., path: Optional[str] = ..., line_no: Optional[int] = ..., link_path: Optional[str] = ...) -> ConsoleRenderable: ...
