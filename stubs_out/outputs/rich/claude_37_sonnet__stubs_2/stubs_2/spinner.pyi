from .console import Console as Console, ConsoleOptions as ConsoleOptions, RenderResult as RenderResult, RenderableType as RenderableType
from .measure import Measurement as Measurement
from .style import StyleType as StyleType
from .table import Table as Table
from .text import Text as Text
from typing import List, Optional, Union

class Spinner:
    def __init__(self, name: str, text: RenderableType = ..., *, style: Optional[StyleType] = ..., speed: float = ...) -> None: ...
    text: Union[RenderableType, Text]
    name: str
    frames: List[str]
    interval: float
    start_time: Optional[float]
    style: Optional[StyleType]
    speed: float
    frame_no_offset: float
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
    def __rich_measure__(self, console: Console, options: ConsoleOptions) -> Measurement: ...
    def render(self, time: float) -> RenderableType: ...
    def update(self, *, text: RenderableType = ..., style: Optional[StyleType] = ..., speed: Optional[float] = ...) -> None: ...
