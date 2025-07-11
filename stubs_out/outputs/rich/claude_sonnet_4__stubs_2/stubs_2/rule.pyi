from .align import AlignMethod as AlignMethod
from .cells import cell_len as cell_len, set_cell_size as set_cell_size
from .console import Console as Console, ConsoleOptions as ConsoleOptions, RenderResult as RenderResult
from .jupyter import JupyterMixin as JupyterMixin
from .measure import Measurement as Measurement
from .segment import Segment as Segment
from .style import Style as Style, StyleType as StyleType
from .text import Text as Text
from typing import Union

class Rule(JupyterMixin):
    def __init__(self, title: Union[str, Text] = ..., *, characters: str = ..., style: StyleType = ..., end: str = ..., align: AlignMethod = ...) -> None: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
    def __rich_measure__(self, console: Console, options: ConsoleOptions) -> Measurement: ...
