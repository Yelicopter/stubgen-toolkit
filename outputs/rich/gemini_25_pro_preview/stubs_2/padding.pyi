from __future__ import annotations

from typing import Tuple, Union

from rich.console import Console, ConsoleOptions, RenderResult, RenderableType
from rich.jupyter import JupyterMixin
from rich.measure import Measurement
from rich.style import StyleType

PaddingDimensions = Union[int, Tuple[int], Tuple[int, int], Tuple[int, int, int, int]]

class Padding(JupyterMixin):
    renderable: RenderableType
    top: int
    right: int
    bottom: int
    left: int
    style: StyleType
    expand: bool
    def __init__(self, renderable: RenderableType, pad: PaddingDimensions = (0, 0, 0, 0), *, style: StyleType = "none", expand: bool = True) -> None: ...
    @classmethod
    def indent(cls, renderable: RenderableType, level: int) -> Padding: ...
    @staticmethod
    def unpack(pad: PaddingDimensions) -> Tuple[int, int, int, int]: ...
    def __repr__(self) -> str: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
    def __rich_measure__(self, console: Console, options: ConsoleOptions) -> Measurement: ...