import math
from functools import lru_cache
from time import monotonic
from typing import Iterable, List, Optional

from .color import Color, blend_rgb
from .color_triplet import ColorTriplet
from .console import Console, ConsoleOptions, RenderResult
from .jupyter import JupyterMixin
from .measure import Measurement
from .segment import Segment
from .style import Style, StyleType

class ProgressBar(JupyterMixin):
    def __init__(
        self,
        total: Optional[float] = 100.0,
        completed: float = 0,
        width: Optional[int] = None,
        pulse: bool = False,
        style: StyleType = "bar.back",
        complete_style: StyleType = "bar.complete",
        finished_style: StyleType = "bar.finished",
        pulse_style: StyleType = "bar.pulse",
        animation_time: Optional[float] = None,
    ) -> None: ...
    
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
        ascii: bool = False,
    ) -> List[Segment]: ...
    
    def update(self, completed: float, total: Optional[float] = None) -> None: ...
    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult: ...
    def __rich_measure__(
        self, console: Console, options: ConsoleOptions
    ) -> Measurement: ...