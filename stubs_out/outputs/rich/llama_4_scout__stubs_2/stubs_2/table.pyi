from . import box as box, errors as errors
from ._loop import loop_first_last as loop_first_last, loop_last as loop_last
from ._pick import pick_bool as pick_bool
from ._ratio import ratio_distribute as ratio_distribute, ratio_reduce as ratio_reduce
from .align import VerticalAlignMethod as VerticalAlignMethod
from .console import Console as Console, ConsoleOptions as ConsoleOptions, JustifyMethod as JustifyMethod, OverflowMethod as OverflowMethod, RenderResult as RenderResult, RenderableType as RenderableType
from .jupyter import JupyterMixin as JupyterMixin
from .measure import Measurement as Measurement
from .padding import Padding as Padding, PaddingDimensions as PaddingDimensions
from .protocol import is_renderable as is_renderable
from .segment import Segment as Segment
from .style import Style as Style, StyleType as StyleType
from .text import Text as Text, TextType as TextType
from dataclasses import field as field, replace as replace
from typing import NamedTuple, Optional

class Column: ...
class Row: ...
class _Cell(NamedTuple): ...

class Table(JupyterMixin):
    def __init__(self, *, title: Optional[TextType] = ..., title_justify: str = ..., header: Optional[TextType] = ..., header_justify: str = ..., row_justify: str = ..., style: StyleType = ..., border_style: StyleType = ..., box: box.Box = ..., safe_box: bool = ..., show_header: bool = ..., header_style: StyleType = ..., border: bool = ..., expand: bool = ..., padding: PaddingDimensions = ...) -> None: ...
