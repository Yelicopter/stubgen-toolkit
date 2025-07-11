from typing import Optional, TYPE_CHECKING

from .segment import Segment
from .style import StyleType
from ._loop import loop_last


if TYPE_CHECKING:
    from .console import (
        Console,
        ConsoleOptions,
        RenderResult,
        RenderableType,
        Group,
    )


class Screen:
    """A renderable that fills the terminal screen and crops excess.

    Args:
        renderable (RenderableType): Child renderable.
        style (StyleType, optional): Optional background style. Defaults to None.
    """

    def __init__(
        self,
        *renderables: "RenderableType",
        style: Optional[StyleType] = None,
        application_mode: bool = False,
    ) -> None:
        ...

    def __rich_console__(
        self, console: "Console", options: "ConsoleOptions"
    ) -> "RenderResult":
        ...