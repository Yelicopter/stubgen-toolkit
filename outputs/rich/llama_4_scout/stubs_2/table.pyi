from dataclasses import dataclass, field, replace
from typing import (
    TYPE_CHECKING,
    Dict,
    Iterable,
    List,
    NamedTuple,
    Optional,
    Sequence,
    Tuple,
    Union,
)

from . import box, errors
from ._loop import loop_first_last, loop_last
from ._pick import pick_bool
from ._ratio import ratio_distribute, ratio_reduce
from .align import VerticalAlignMethod
from .jupyter import JupyterMixin
from .measure import Measurement
from .padding import Padding, PaddingDimensions
from .protocol import is_renderable
from .segment import Segment
from .style import Style, StyleType
from .text import Text, TextType

if TYPE_CHECKING:
    from .console import (
        Console,
        ConsoleOptions,
        JustifyMethod,
        OverflowMethod,
        RenderableType,
        RenderResult,
    )


@dataclass
class Column:
    ...

@dataclass
class Row:
    ...

class _Cell(NamedTuple):
    ...

class Table(JupyterMixin):
    def __init__(
        self,
        *,
        title: Optional[TextType] = None,
        title_justify: str = "left",
        header: Optional[TextType] = None,
        header_justify: str = "left",
        row_justify: str = "left",
        style: StyleType = "none",
        border_style: StyleType = "none",
        box: box.Box = box.SIMPLE,
        safe_box: bool = True,
        show_header: bool = True,
        header_style: StyleType = "table.header",
        border: bool = True,
        expand: bool = False,
        padding: PaddingDimensions = (0, 1),
    ) -> None:
        ...