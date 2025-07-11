from typing import Dict, List, Optional, Union, cast

from .console import Console, ConsoleOptions, RenderResult
from .jupyter import JupyterMixin
from .measure import Measurement
from .style import StyleType
from .text import Text

class Spinner(JupyterMixin):
    def __init__(
        self,
        name: str = "dots",
        text: str = "",
        *,
        style: Optional[StyleType] = None,
        speed: float = 1.0
    ) -> None: ...
    
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
    def __rich_measure__(self, console: Console, options: ConsoleOptions) -> Measurement: ...
    def render(self, time: float) -> Text: ...
    def update(
        self,
        *,
        text: Optional[str] = None,
        style: Optional[StyleType] = None,
        speed: Optional[float] = None
    ) -> None: ...