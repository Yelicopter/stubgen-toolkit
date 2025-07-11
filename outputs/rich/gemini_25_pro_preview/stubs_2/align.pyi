from __future__ import annotations

from typing import Iterable, Optional

from typing_extensions import Literal

from rich.console import Console, ConsoleOptions, RenderResult, RenderableType
from rich.jupyter import JupyterMixin
from rich.measure import Measurement
from rich.style import StyleType

AlignMethod = Literal["left", "center", "right"]
VerticalAlignMethod = Literal["top", "middle", "bottom"]

class Align(JupyterMixin):
    renderable: RenderableType
    align: AlignMethod
    style: Optional[StyleType]
    vertical: Optional[VerticalAlignMethod]
    pad: bool
    width: Optional[int]
    height: Optional[int]
    def __init__(self, renderable: RenderableType, align: AlignMethod = "left", style: Optional[StyleType] = None, *, vertical: Optional[VerticalAlignMethod] = None, pad: bool = True, width: Optional[int] = None, height: Optional[int] = None) -> None: ...
    def __repr__(self) -> str: ...
    @classmethod
    def left(cls, renderable: RenderableType, style: Optional[StyleType] = None, *, vertical: Optional[VerticalAlignMethod] = None, pad: bool = True, width: Optional[int] = None, height: Optional[int] = None) -> Align: ...
    @classmethod
    def center(cls, renderable: RenderableType, style: Optional[StyleType] = None, *, vertical: Optional[VerticalAlignMethod] = None, pad: bool = True, width: Optional[int] = None, height: Optional[int] = None) -> Align: ...
    @classmethod
    def right(cls, renderable: RenderableType, style: Optional[StyleType] = None, *, vertical: Optional[VerticalAlignMethod] = None, pad: bool = True, width: Optional[int] = None, height: Optional[int] = None) -> Align: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
    def __rich_measure__(self, console: Console, options: ConsoleOptions) -> Measurement: ...

class VerticalCenter(JupyterMixin):
    renderable: RenderableType
    style: Optional[StyleType]
    def __init__(self, renderable: RenderableType, style: Optional[StyleType] = None) -> None: ...
    def __repr__(self) -> str: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
    def __rich_measure__(self, console: Console, options: ConsoleOptions) -> Measurement: ...