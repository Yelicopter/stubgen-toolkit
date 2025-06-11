from typing import TYPE_CHECKING

from .measure import Measurement
from .segment import Segment
from .style import StyleType

from .console import Console, ConsoleOptions, RenderResult, RenderableType

class Styled:
    def __init__(self, renderable: RenderableType, style: StyleType) -> None: ...
    renderable: RenderableType
    style: StyleType
    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult: ...
    def __rich_measure__(
        self, console: Console, options: ConsoleOptions
    ) -> Measurement: ...