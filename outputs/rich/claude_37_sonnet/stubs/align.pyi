from typing import TYPE_CHECKING, Iterable, Literal, Optional
from .jupyter import JupyterMixin
from .measure import Measurement
from .style import StyleType

if TYPE_CHECKING:
    from .console import Console, ConsoleOptions, RenderableType, RenderResult

AlignMethod = Literal['left', 'center', 'right']
VerticalAlignMethod = Literal['top', 'middle', 'bottom']

class Align(JupyterMixin):
    renderable: 'RenderableType'
    align: AlignMethod
    style: Optional[StyleType]
    vertical: Optional[VerticalAlignMethod]
    pad: bool
    width: Optional[int]
    height: Optional[int]

    def __init__(
        self,
        renderable: 'RenderableType',
        align: AlignMethod = 'left',
        style: Optional[StyleType] = None,
        *,
        vertical: Optional[VerticalAlignMethod] = None,
        pad: bool = True,
        width: Optional[int] = None,
        height: Optional[int] = None
    ) -> None:
        ...

    def __repr__(self) -> str:
        ...

    @classmethod
    def left(
        cls,
        renderable: 'RenderableType',
        style: Optional[StyleType] = None,
        *,
        vertical: Optional[VerticalAlignMethod] = None,
        pad: bool = True,
        width: Optional[int] = None,
        height: Optional[int] = None
    ) -> 'Align':
        ...

    @classmethod
    def center(
        cls,
        renderable: 'RenderableType',
        style: Optional[StyleType] = None,
        *,
        vertical: Optional[VerticalAlignMethod] = None,
        pad: bool = True,
        width: Optional[int] = None,
        height: Optional[int] = None
    ) -> 'Align':
        ...

    @classmethod
    def right(
        cls,
        renderable: 'RenderableType',
        style: Optional[StyleType] = None,
        *,
        vertical: Optional[VerticalAlignMethod] = None,
        pad: bool = True,
        width: Optional[int] = None,
        height: Optional[int] = None
    ) -> 'Align':
        ...

    def __rich_console__(self, console: 'Console', options: 'ConsoleOptions') -> 'RenderResult':
        ...

    def __rich_measure__(self, console: 'Console', options: 'ConsoleOptions') -> Measurement:
        ...

class VerticalCenter(JupyterMixin):
    renderable: 'RenderableType'
    style: Optional[StyleType]

    def __init__(self, renderable: 'RenderableType', style: Optional[StyleType] = None) -> None:
        ...

    def __repr__(self) -> str:
        ...

    def __rich_console__(self, console: 'Console', options: 'ConsoleOptions') -> 'RenderResult':
        ...

    def __rich_measure__(self, console: 'Console', options: 'ConsoleOptions') -> Measurement:
        ...