from . import box as box
from .align import AlignMethod as AlignMethod
from .console import Console as Console, ConsoleOptions as ConsoleOptions, RenderResult as RenderResult, RenderableType as RenderableType
from .jupyter import JupyterMixin as JupyterMixin
from .measure import Measurement as Measurement
from .padding import PaddingDimensions as PaddingDimensions
from .segment import Segment as Segment
from .style import StyleType as StyleType
from typing import Optional

class Panel(JupyterMixin):
    def __init__(self, renderable: RenderableType, box: box.Box = ..., *, safe_box: Optional[bool] = ..., expand: bool = ..., style: StyleType = ..., border_style: StyleType = ..., width: Optional[int] = ..., height: Optional[int] = ..., padding: PaddingDimensions = ..., highlight: bool = ..., title: Optional['RenderableType'] = ..., title_align: AlignMethod = ..., subtitle: Optional['RenderableType'] = ..., subtitle_align: AlignMethod = ...) -> None: ...
    @classmethod
    def fit(cls, renderable: RenderableType, box: box.Box = ..., *, safe_box: Optional[bool] = ..., style: StyleType = ..., border_style: StyleType = ..., width: Optional[int] = ..., padding: PaddingDimensions = ..., title: Optional['RenderableType'] = ..., title_align: AlignMethod = ..., subtitle: Optional['RenderableType'] = ..., subtitle_align: AlignMethod = ...) -> Panel: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
    def __rich_measure__(self, console: Console, options: ConsoleOptions) -> Measurement: ...
