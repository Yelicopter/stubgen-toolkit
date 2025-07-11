from .color import Color as Color
from .console import Console as Console, ConsoleOptions as ConsoleOptions, RenderResult as RenderResult
from .jupyter import JupyterMixin as JupyterMixin
from .measure import Measurement as Measurement
from .segment import Segment as Segment
from .style import Style as Style
from typing import Optional, Union

class Bar(JupyterMixin):
    def __init__(self, size: float, begin: float, end: float, *, width: Optional[int] = ..., color: Union[Color, str] = ..., bgcolor: Union[Color, str] = ...) -> None: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
    def __rich_measure__(self, console: Console, options: ConsoleOptions) -> Measurement: ...
