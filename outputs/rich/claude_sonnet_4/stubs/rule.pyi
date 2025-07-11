from typing import TYPE_CHECKING, Union

from .align import AlignMethod
from .cells import cell_len, set_cell_size
from .jupyter import JupyterMixin
from .measure import Measurement
from .segment import Segment
from .style import Style, StyleType
from .text import Text

if TYPE_CHECKING:
    from .console import Console, ConsoleOptions, RenderResult

class Rule(JupyterMixin):
    def __init__(
        self,
        title: Union[str, Text] = "",
        *,
        characters: str = "─",
        style: StyleType = "rule.line",
        end: str = "\n",
        align: AlignMethod = "center"
    ) -> None: ...
    
    def __repr__(self) -> str: ...
    def __rich_console__(self, console: "Console", options: "ConsoleOptions") -> "RenderResult": ...
    def __rich_measure__(self, console: "Console", options: "ConsoleOptions") -> Measurement: ...