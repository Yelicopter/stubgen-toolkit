import sys
from typing import Optional, Tuple

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal  # pragma: no cover

from ._loop import loop_last
from .console import Console, ConsoleOptions, RenderableType, RenderResult
from .control import Control
from .segment import ControlType, Segment
from .style import StyleType
from .text import Text

VerticalOverflowMethod = Literal["crop", "ellipsis", "visible"]

class LiveRender:
    renderable: RenderableType
    style: StyleType
    vertical_overflow: VerticalOverflowMethod
    _shape: Optional[Tuple[int, int]]

    def __init__(
        self,
        renderable: RenderableType,
        style: StyleType = "",
        vertical_overflow: VerticalOverflowMethod = "ellipsis",
    ) -> None: ...

    def set_renderable(self, renderable: RenderableType) -> None: ...

    def position_cursor(self) -> Control: ...

    def restore_cursor(self) -> Control: ...

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult: ...