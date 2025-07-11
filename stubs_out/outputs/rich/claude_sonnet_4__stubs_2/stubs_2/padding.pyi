from .console import Console as Console, ConsoleOptions as ConsoleOptions, RenderResult as RenderResult, RenderableType as RenderableType
from .jupyter import JupyterMixin as JupyterMixin
from .measure import Measurement as Measurement
from .segment import Segment as Segment
from .style import Style as Style
from typing import Tuple, Union

PaddingDimensions = Union[int, Tuple[int], Tuple[int, int], Tuple[int, int, int, int]]

class Padding(JupyterMixin):
    def __init__(self, renderable: RenderableType, pad: PaddingDimensions = ..., *, style: str = ..., expand: bool = ...) -> None: ...
    @classmethod
    def indent(cls, renderable: RenderableType, level: int) -> Padding: ...
    @staticmethod
    def unpack(pad: PaddingDimensions) -> Tuple[int, int, int, int]: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
    def __rich_measure__(self, console: Console, options: ConsoleOptions) -> Measurement: ...
