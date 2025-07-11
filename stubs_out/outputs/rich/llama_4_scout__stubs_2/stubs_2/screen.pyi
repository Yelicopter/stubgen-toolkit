from ._loop import loop_last as loop_last
from .console import Console as Console, ConsoleOptions as ConsoleOptions, Group as Group, RenderResult as RenderResult, RenderableType as RenderableType
from .segment import Segment as Segment
from .style import StyleType as StyleType
from typing import Optional

class Screen:
    def __init__(self, *renderables: RenderableType, style: Optional[StyleType] = ..., application_mode: bool = ...) -> None: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
