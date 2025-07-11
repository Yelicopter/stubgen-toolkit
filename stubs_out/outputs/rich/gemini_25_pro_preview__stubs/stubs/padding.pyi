from rich.console import Console as Console, ConsoleOptions as ConsoleOptions, RenderResult as RenderResult, RenderableType as RenderableType
from rich.jupyter import JupyterMixin
from rich.measure import Measurement as Measurement
from rich.style import StyleType as StyleType
from typing import Tuple, Union

PaddingDimensions = Union[int, Tuple[int], Tuple[int, int], Tuple[int, int, int, int]]

class Padding(JupyterMixin):
    renderable: RenderableType
    top: int
    right: int
    bottom: int
    left: int
    style: StyleType
    expand: bool
    def __init__(self, renderable: RenderableType, pad: PaddingDimensions = ..., *, style: StyleType = ..., expand: bool = ...) -> None: ...
    @classmethod
    def indent(cls, renderable: RenderableType, level: int) -> Padding: ...
    @staticmethod
    def unpack(pad: PaddingDimensions) -> Tuple[int, int, int, int]: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
    def __rich_measure__(self, console: Console, options: ConsoleOptions) -> Measurement: ...
