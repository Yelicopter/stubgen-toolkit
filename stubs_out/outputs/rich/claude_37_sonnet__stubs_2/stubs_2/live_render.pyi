from ._loop import loop_last as loop_last
from .console import Console as Console, ConsoleOptions as ConsoleOptions, RenderResult as RenderResult, RenderableType as RenderableType
from .control import Control as Control
from .segment import ControlType as ControlType, Segment as Segment
from .style import StyleType as StyleType
from .text import Text as Text
from _typeshed import Incomplete

VerticalOverflowMethod: Incomplete

class LiveRender:
    renderable: RenderableType
    style: StyleType
    vertical_overflow: VerticalOverflowMethod
    def __init__(self, renderable: RenderableType, style: StyleType = ..., vertical_overflow: VerticalOverflowMethod = ...) -> None: ...
    def set_renderable(self, renderable: RenderableType) -> None: ...
    def position_cursor(self) -> Control: ...
    def restore_cursor(self) -> Control: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
