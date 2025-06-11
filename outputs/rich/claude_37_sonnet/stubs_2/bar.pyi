from typing import Optional, Union
from .color import Color
from .console import Console, ConsoleOptions, RenderResult
from .jupyter import JupyterMixin
from .measure import Measurement
from .style import Style

class Bar(JupyterMixin):
    size: float
    begin: float
    end: float
    width: Optional[int]
    style: Style

    def __init__(
        self,
        size: float,
        begin: float,
        end: float,
        *,
        width: Optional[int] = None,
        color: Union[str, Color] = 'default',
        bgcolor: Union[str, Color] = 'default'
    ) -> None:
        ...

    def __repr__(self) -> str:
        ...

    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult:
        ...

    def __rich_measure__(self, console: Console, options: ConsoleOptions) -> Measurement:
        ...