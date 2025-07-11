from .console import Console as Console, ConsoleOptions as ConsoleOptions, RenderResult as RenderResult, RenderableType as RenderableType
from .jupyter import JupyterMixin as JupyterMixin
from .measure import Measurement as Measurement
from .style import StyleType as StyleType
from _typeshed import Incomplete
from typing import Optional

AlignMethod: Incomplete
VerticalAlignMethod: Incomplete

class Align(JupyterMixin):
    renderable: RenderableType
    align: AlignMethod
    style: Optional[StyleType]
    vertical: Optional[VerticalAlignMethod]
    pad: bool
    width: Optional[int]
    height: Optional[int]
    def __init__(self, renderable: RenderableType, align: AlignMethod = ..., style: Optional[StyleType] = ..., *, vertical: Optional[VerticalAlignMethod] = ..., pad: bool = ..., width: Optional[int] = ..., height: Optional[int] = ...) -> None: ...
    @classmethod
    def left(cls, renderable: RenderableType, style: Optional[StyleType] = ..., *, vertical: Optional[VerticalAlignMethod] = ..., pad: bool = ..., width: Optional[int] = ..., height: Optional[int] = ...) -> Align: ...
    @classmethod
    def center(cls, renderable: RenderableType, style: Optional[StyleType] = ..., *, vertical: Optional[VerticalAlignMethod] = ..., pad: bool = ..., width: Optional[int] = ..., height: Optional[int] = ...) -> Align: ...
    @classmethod
    def right(cls, renderable: RenderableType, style: Optional[StyleType] = ..., *, vertical: Optional[VerticalAlignMethod] = ..., pad: bool = ..., width: Optional[int] = ..., height: Optional[int] = ...) -> Align: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
    def __rich_measure__(self, console: Console, options: ConsoleOptions) -> Measurement: ...

class VerticalCenter(JupyterMixin):
    renderable: RenderableType
    style: Optional[StyleType]
    def __init__(self, renderable: RenderableType, style: Optional[StyleType] = ...) -> None: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
    def __rich_measure__(self, console: Console, options: ConsoleOptions) -> Measurement: ...
