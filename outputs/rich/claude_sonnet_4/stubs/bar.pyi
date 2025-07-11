from typing import Optional, Union
from .color import Color
from .console import Console, ConsoleOptions, RenderResult
from .jupyter import JupyterMixin
from .measure import Measurement
from .style import StyleType

class Bar(JupyterMixin):
    def __init__(
        self,
        size: float = 100,
        begin: float = 0,
        end: Optional[float] = None,
        width: Optional[int] = None,
        color: Union[Color, str] = "default",
        bgcolor: Union[Color, str] = "default"
    ) -> None: ...
    
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
    def __rich_measure__(self, console: Console, options: ConsoleOptions) -> Measurement: ...