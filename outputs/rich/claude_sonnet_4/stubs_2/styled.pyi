from typing import TYPE_CHECKING

from .jupyter import JupyterMixin
from .measure import Measurement
from .segment import Segment
from .style import Style, StyleType

if TYPE_CHECKING:
    from .console import Console, ConsoleOptions, RenderableType, RenderResult

class Styled(JupyterMixin):
    def __init__(self, renderable: "RenderableType", style: StyleType) -> None: ...
    def __rich_console__(self, console: "Console", options: "ConsoleOptions") -> "RenderResult": ...
    def __rich_measure__(self, console: "Console", options: "ConsoleOptions") -> Measurement: ...