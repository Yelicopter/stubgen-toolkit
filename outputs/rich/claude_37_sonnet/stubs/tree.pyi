from typing import Iterator, List, Optional, Tuple

from ._loop import loop_first, loop_last
from .console import Console, ConsoleOptions, RenderableType, RenderResult
from .jupyter import JupyterMixin
from .measure import Measurement
from .segment import Segment
from .style import Style, StyleStack, StyleType
from .styled import Styled

GuideType = Tuple[str, str, str, str]

class Tree(JupyterMixin):
    ASCII_GUIDES: GuideType
    TREE_GUIDES: List[GuideType]
    def __init__(
        self,
        label: RenderableType,
        *,
        style: StyleType = ...,
        guide_style: StyleType = ...,
        expanded: bool = ...,
        highlight: bool = ...,
        hide_root: bool = ...,
    ) -> None: ...
    label: RenderableType
    style: StyleType
    guide_style: StyleType
    children: List[Tree]
    expanded: bool
    highlight: bool
    hide_root: bool
    def add(
        self,
        label: RenderableType,
        *,
        style: Optional[StyleType] = ...,
        guide_style: Optional[StyleType] = ...,
        expanded: bool = ...,
        highlight: Optional[bool] = ...,
    ) -> "Tree": ...
    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult: ...
    def __rich_measure__(
        self, console: Console, options: ConsoleOptions
    ) -> Measurement: ...