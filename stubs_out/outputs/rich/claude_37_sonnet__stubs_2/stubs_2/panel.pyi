from .align import AlignMethod as AlignMethod
from .box import Box as Box, ROUNDED as ROUNDED
from .cells import cell_len as cell_len
from .console import Console as Console, ConsoleOptions as ConsoleOptions, RenderResult as RenderResult, RenderableType as RenderableType
from .jupyter import JupyterMixin as JupyterMixin
from .measure import Measurement as Measurement, measure_renderables as measure_renderables
from .padding import Padding as Padding, PaddingDimensions as PaddingDimensions
from .segment import Segment as Segment
from .style import Style as Style, StyleType as StyleType
from .text import Text as Text, TextType as TextType
from typing import Optional

class Panel(JupyterMixin):
    def __init__(self, renderable: RenderableType, box: Box = ..., *, title: Optional[TextType] = ..., title_align: AlignMethod = ..., subtitle: Optional[TextType] = ..., subtitle_align: AlignMethod = ..., safe_box: Optional[bool] = ..., expand: bool = ..., style: StyleType = ..., border_style: StyleType = ..., width: Optional[int] = ..., height: Optional[int] = ..., padding: PaddingDimensions = ..., highlight: bool = ...) -> None: ...
    @classmethod
    def fit(cls, renderable: RenderableType, box: Box = ..., *, title: Optional[TextType] = ..., title_align: AlignMethod = ..., subtitle: Optional[TextType] = ..., subtitle_align: AlignMethod = ..., safe_box: Optional[bool] = ..., style: StyleType = ..., border_style: StyleType = ..., width: Optional[int] = ..., height: Optional[int] = ..., padding: PaddingDimensions = ..., highlight: bool = ...) -> Panel: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
    def __rich_measure__(self, console: Console, options: ConsoleOptions) -> Measurement: ...
