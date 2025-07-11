from ._loop import loop_first as loop_first, loop_last as loop_last
from .console import Console as Console, ConsoleOptions as ConsoleOptions, RenderResult as RenderResult, RenderableType as RenderableType
from .jupyter import JupyterMixin as JupyterMixin
from .measure import Measurement as Measurement
from .segment import Segment as Segment
from .style import Style as Style, StyleStack as StyleStack, StyleType as StyleType
from .styled import Styled as Styled
from typing import List, Optional, Tuple

GuideType = Tuple[str, str, str, str]

class Tree(JupyterMixin):
    ASCII_GUIDES: GuideType
    TREE_GUIDES: List[GuideType]
    def __init__(self, label: RenderableType, *, style: StyleType = ..., guide_style: StyleType = ..., expanded: bool = ..., highlight: bool = ..., hide_root: bool = ...) -> None: ...
    label: RenderableType
    style: StyleType
    guide_style: StyleType
    children: List[Tree]
    expanded: bool
    highlight: bool
    hide_root: bool
    def add(self, label: RenderableType, *, style: Optional[StyleType] = ..., guide_style: Optional[StyleType] = ..., expanded: bool = ..., highlight: Optional[bool] = ...) -> Tree: ...
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
    def __rich_measure__(self, console: Console, options: ConsoleOptions) -> Measurement: ...
