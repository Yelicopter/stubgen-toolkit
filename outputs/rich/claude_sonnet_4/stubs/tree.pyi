from typing import Iterator, List, Optional, Union

from .console import Console, ConsoleOptions, RenderResult
from .jupyter import JupyterMixin
from .measure import Measurement
from .segment import Segment
from .style import StyleType
from .text import Text, TextType

class Tree(JupyterMixin):
    def __init__(
        self,
        label: TextType,
        *,
        style: StyleType = "tree",
        guide_style: StyleType = "tree.line",
        expanded: bool = True,
        highlight: bool = False,
    ) -> None: ...
    
    @classmethod
    def from_data(
        cls,
        data: Union[dict, list],
        *,
        name: str = "data",
        style: StyleType = "tree",
        guide_style: StyleType = "tree.line",
        expanded: bool = True,
        highlight: bool = False,
    ) -> "Tree": ...
    
    def add(
        self,
        label: TextType,
        *,
        style: Optional[StyleType] = None,
        guide_style: Optional[StyleType] = None,
        expanded: bool = True,
        highlight: Optional[bool] = None,
    ) -> "Tree": ...
    
    def add_tree(
        self,
        tree: "Tree",
        *,
        style: Optional[StyleType] = None,
        guide_style: Optional[StyleType] = None,
        expanded: bool = True,
        highlight: Optional[bool] = None,
    ) -> "Tree": ...
    
    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult: ...
    def __rich_measure__(self, console: Console, options: ConsoleOptions) -> Measurement: ...