from typing import TYPE_CHECKING

from .measure import Measurement
from .segment import Segment
from .style import StyleType

if TYPE_CHECKING:
    from .console import Console, ConsoleOptions, RenderResult, RenderableType


class Styled:
    """Apply a style to a renderable.

    Args:
        renderable (RenderableType): Any renderable.
        style (StyleType): A style to apply across the entire renderable.
    """

    def __init__(self, renderable: "RenderableType", style: StyleType) -> None:
        ...

    def __rich_console__(
        self, console: "Console", options: "ConsoleOptions"
    ) -> "RenderResult":
        ...

    def __rich_measure__(
        self, console: "Console", options: "ConsoleOptions"
    ) -> Measurement:
        ...