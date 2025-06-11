from typing import Optional

from .segment import Segment
from .style import StyleType
from ._loop import loop_last

from .console import Console, ConsoleOptions, RenderResult, RenderableType, Group

class Screen:
    def __init__(
        self,
        *renderables: RenderableType,
        style: Optional[StyleType] = ...,
        application_mode: bool = ...,
    ) -> None: ...
    renderable: RenderableType
    style: Optional[StyleType]
    application_mode: bool
    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult: ...