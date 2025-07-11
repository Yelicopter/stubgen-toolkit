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
    """Renders a (progress) bar. Used by rich.progress.

    Args:
        total (float, optional): Number of steps in the bar. Defaults to 100. Set to None to render a pulsing animation.
        completed (float, optional): Number of steps completed. Defaults to 0.
        width (int, optional): Width of the bar, or ``None`` for maximum width. Defaults to None.
        pulse (bool, optional): Enable pulse effect. Defaults to False. Will pulse if a None total was passed.
        style (StyleType, optional): Style for the bar background. Defaults to "bar.back".
        complete_style (StyleType, optional): Style for the completed bar. Defaults to "bar.complete".
        finished_style (StyleType, optional): Style for a finished bar. Defaults to "bar.finished".
        pulse_style (StyleType, optional): Style for pulsing bars. Defaults to "bar.pulse".
        animation_time (Optional[float], optional): Time in seconds to use for animation, or None to use system time.
    """

    def __init__(
        self,
        total: float = 100.0,
        completed: float = 0,
        width: Optional[int] = None,
        pulse: bool = False,
        style: StyleType = "bar.back",
        complete_style: StyleType = "bar.complete",
        finished_style: StyleType = "bar.finished",
        pulse_style: StyleType = "bar.pulse",
        animation_time: Optional[float] = None,
    ) -> None:
        ...

    def __repr__(self) -> str:
        ...

    @property
    def percentage_completed(self) -> Optional[float]:
        ...

    @lru_cache(maxsize=16)
    def _get_pulse_segments(
        self,
        fore_style: Style,
        back_style: Style,
        color_system: str,
        no_color: bool,
        ascii: bool = False,
    ) -> List[Segment]:
        ...

    def update(self, completed: float, total: Optional[float] = None) -> None:
        ...

    def _render_pulse(
        self, console: Console, width: int, ascii: bool = False
    ) -> Iterable[Segment]:
        ...

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult:
        ...

    def __rich_measure__(
        self, console: Console, options: ConsoleOptions
    ) -> Measurement:
        ...