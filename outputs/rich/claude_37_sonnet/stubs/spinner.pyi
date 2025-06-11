from typing import List, Optional, Union

from .measure import Measurement
from .table import Table
from .text import Text

from .console import Console, ConsoleOptions, RenderResult, RenderableType
from .style import StyleType

class Spinner:
    def __init__(
        self,
        name: str,
        text: RenderableType = ...,
        *,
        style: Optional[StyleType] = ...,
        speed: float = ...,
    ) -> None: ...
    text: Union[RenderableType, Text]
    name: str
    frames: List[str]
    interval: float
    start_time: Optional[float]
    style: Optional[StyleType]
    speed: float
    frame_no_offset: float
    _update_speed: float
    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult: ...
    def __rich_measure__(
        self, console: Console, options: ConsoleOptions
    ) -> Measurement: ...
    def render(self, time: float) -> RenderableType: ...
    def update(
        self,
        *,
        text: RenderableType = ...,
        style: Optional[StyleType] = ...,
        speed: Optional[float] = ...,
    ) -> None: ...