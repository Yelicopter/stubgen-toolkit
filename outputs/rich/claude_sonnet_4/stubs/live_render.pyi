import sys
from typing import TYPE_CHECKING, Optional, Tuple

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

from .control import Control
from .segment import Segment
from .style import StyleType

if TYPE_CHECKING:
    from .console import Console, ConsoleOptions, RenderableType, RenderResult

VerticalOverflowMethod = Literal["crop", "ellipsis", "visible"]

class LiveRender:
    def __init__(
        self,
        renderable: "RenderableType",
        vertical_overflow: VerticalOverflowMethod = "ellipsis"
    ) -> None: ...
    
    def set_renderable(self, renderable: "RenderableType") -> None: ...
    def position_cursor(self) -> Control: ...
    def restore_cursor(self) -> Control: ...
    def __rich_console__(self, console: "Console", options: "ConsoleOptions") -> "RenderResult": ...