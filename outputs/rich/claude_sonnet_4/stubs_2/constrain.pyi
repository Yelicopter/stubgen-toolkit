from typing import TYPE_CHECKING, Optional

from .jupyter import JupyterMixin
from .measure import Measurement

if TYPE_CHECKING:
    from .console import Console, ConsoleOptions, RenderableType, RenderResult

class Constrain(JupyterMixin):
    def __init__(self, renderable: "RenderableType", width: Optional[int] = None) -> None: ...
    def __rich_console__(self, console: "Console", options: "ConsoleOptions") -> "RenderResult": ...
    def __rich_measure__(self, console: "Console", options: "ConsoleOptions") -> Measurement: ...