from __future__ import annotations

from typing import Iterable, List, Optional

from rich.console import Console, ConsoleOptions, RenderResult
from rich.jupyter import JupyterMixin
from rich.measure import Measurement
from rich.segment import Segment
from rich.style import Style, StyleType

PULSE_SIZE: int

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
    _pulse_segments: Optional[List[Segment]]
    def __init__(self, total: Optional[float] = 100.0, completed: float = 0, width: Optional[int] = None, pulse: bool = False, style: StyleType = "bar.back", complete_style: StyleType = "bar.complete", finished_style: StyleType = "bar.finished", pulse_style: StyleType = "bar.pulse", animation_time: Optional[float] = None) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def percentage_completed(self) -> Optional[float]: ...
    def _get_pulse_segments(self, fore_style: Style, back_style: Style, color_system: str, no_color: bool, ascii: bool = False) -> List[Segment]: ...
    def update(self, completed: float, total: Optional[float] = None) -> None: ...
    def _render_pulse(self, console: Console, width: int, ascii: bool = False) -> Iterable[Segment]: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
    def __rich_measure__(self, console: Console, options: ConsoleOptions) -> Measurement: ...