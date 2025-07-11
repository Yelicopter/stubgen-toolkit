from .align import Align as Align, AlignMethod as AlignMethod
from .console import Console as Console, ConsoleOptions as ConsoleOptions, RenderResult as RenderResult, RenderableType as RenderableType
from .constrain import Constrain as Constrain
from .jupyter import JupyterMixin as JupyterMixin
from .measure import Measurement as Measurement
from .padding import Padding as Padding, PaddingDimensions as PaddingDimensions
from .table import Table as Table
from .text import TextType as TextType
from collections import defaultdict as defaultdict
from itertools import chain as chain
from operator import itemgetter as itemgetter
from typing import Iterable, Optional

class Columns(JupyterMixin):
    def __init__(self, renderables: Optional[Iterable[RenderableType]] = ..., padding: PaddingDimensions = ..., *, width: Optional[int] = ..., expand: bool = ..., equal: bool = ..., column_first: bool = ..., right_to_left: bool = ..., align: Optional[str] = ..., title: Optional[TextType] = ...) -> None: ...
    def add_renderable(self, renderable: RenderableType) -> None: ...
    def __rich_console__(self, console, options) -> RenderResult: ...
