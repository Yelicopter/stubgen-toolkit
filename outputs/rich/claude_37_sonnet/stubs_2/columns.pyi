from collections import defaultdict
from itertools import chain
from operator import itemgetter
from typing import Dict, Iterable, List, Optional, Tuple

from .align import Align, AlignMethod
from .console import Console, ConsoleOptions, RenderableType, RenderResult
from .constrain import Constrain
from .measure import Measurement
from .padding import Padding, PaddingDimensions
from .table import Table
from .text import TextType
from .jupyter import JupyterMixin

class Columns(JupyterMixin):
    renderables: List[RenderableType]
    width: Optional[int]
    padding: PaddingDimensions
    expand: bool
    equal: bool
    column_first: bool
    right_to_left: bool
    align: Optional[AlignMethod]
    title: Optional[TextType]

    def __init__(
        self,
        renderables: Optional[Iterable[RenderableType]] = None,
        padding: PaddingDimensions = (0, 1),
        *,
        width: Optional[int] = None,
        expand: bool = False,
        equal: bool = False,
        column_first: bool = False,
        right_to_left: bool = False,
        align: Optional[AlignMethod] = None,
        title: Optional[TextType] = None,
    ) -> None: ...

    def add_renderable(self, renderable: RenderableType) -> None: ...

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult: ...