from functools import lru_cache
from typing import Iterable, List, Optional

from .color import Color
from .color_triplet import ColorTriplet
from .console import Console, ConsoleOptions, RenderResult
from .jupyter import JupyterMixin
from .measure import Measurement
from .segment import Segment
from .style import Style, StyleType

PULSE_SIZE: int

class ProgressBar(JupyterMixin):
    def __init__(
        self,
        total: Optional[float] = ...,
        completed: float = ...,
        width: Optional[int] = ...,
        pulse: bool = ...,
        style: StyleType = ...,
        complete_style: StyleType = ...,
        finished_style: StyleType = ...,
        pulse_style: StyleType = ...,
        animation_time: Optional[float] = ...,
    ) -> None: ...
    total: Optional[float]
    completed: float
    width: Optional[int]
    pulse: bool
    style: StyleType
    complete_style: StyleType
    finished_style: StyleType
    pulse_style: StyleType
    animation_time: Optional[float]
    _pulse_segments: Optional[List[Segment]]
    def __repr__(self) -> str: ...
    @property
    def percentage_completed(self) -> Optional[float]: ...
    @lru_cache(maxsize=16)
    def _get_pulse_segments(
        self,
        fore_style: Style,
        back_style: Style,
        color_system: str,
        no_color: bool,
        ascii: bool = ...,
    ) -> List[Segment]: ...
    def update(self, completed: float, total: Optional[float] = ...) -> None: ...
    def _render_pulse(
        self, console: Console, width: int, ascii: bool = ...
    ) -> Iterable[Segment]: ...
    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult: ...
    def __rich_measure__(
        self, console: Console, options: ConsoleOptions
    ) -> Measurement: ...