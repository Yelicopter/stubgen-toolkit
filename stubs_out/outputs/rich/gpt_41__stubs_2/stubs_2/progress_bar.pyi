from .color import Color as Color
from .console import Console as Console, ConsoleOptions as ConsoleOptions, RenderResult as RenderResult
from .jupyter import JupyterMixin as JupyterMixin
from .measure import Measurement as Measurement
from .segment import Segment as Segment
from .style import Style as Style, StyleType as StyleType
from typing import Optional

class ProgressBar(JupyterMixin):
    total: Optional[float]
    completed: float
    width: Optional[int]
    pulse: bool
    style: StyleType
    complete_style: StyleType
    finished_style: StyleType
    pulse_style: StyleType
    animation_time: Optional[float]
    def __init__(self, total: Optional[float] = ..., completed: float = ..., width: Optional[int] = ..., pulse: bool = ..., style: StyleType = ..., complete_style: StyleType = ..., finished_style: StyleType = ..., pulse_style: StyleType = ..., animation_time: Optional[float] = ...) -> None: ...
    @property
    def percentage_completed(self) -> Optional[float]: ...
    def update(self, completed: float, total: Optional[float] = ...) -> None: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
    def __rich_measure__(self, console: Console, options: ConsoleOptions) -> Measurement: ...
